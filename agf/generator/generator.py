import re
import os

from mysql.connector.errors import InterfaceError

from agf.antlr4_parser import ScannerAntl
from agf.antlr4_parser import Parser
from agf.checkgrammar import CheckMySQLAntlr, CheckTSQLAntlr
from agf.checkoriginal import MySqlParser, TSQlParser
from agf.my_error import SettingFuzzerError

from .abstract_generator import AbstractGeneratorFactory, AbstractGenerator
from .generator_mode import SqlForms, RandomQuery


PASS_LIN = "mypass\n"


class SQLGenerator(AbstractGenerator):
    """
    SQLGenerator for generate query
    """

    def __init__(self, parser_file: str, lexer_file: str, grammar_type: str) -> None:
        super().__init__()
        self._parser_file = parser_file
        self._lexer_file = lexer_file
        self._grammar_type = grammar_type
        self._rule_dictionary = {}
        self._multiplication_scale = 1
        self._random_scale = 1
        self.exception_rule = []
        self._access_rule_in_lexer_file = []
        self._combined_mutate_rule = []
        self._read_grammar_file()
        self._mutate_mode = False
        self._mutate_chance = 1
        self._fuzzing_mode = 'random_query'
        self._sql_forms = None
        self._start_position = 0
        self._end_position = 1
        self._count_to_generate = 1
        self._status_original = bool
        self._status_antlr4 = bool
        # original parser setting
        self._user = None
        self._password = None
        self._host = None
        self._database = None
        self._err = None
        self._dict_with_param = {}

    @property
    def mutate_mode(self):
        return self._mutate_mode

    @mutate_mode.setter
    def mutate_mode(self, mutate_mode):
        assert isinstance(mutate_mode, bool)
        self._mutate_mode = mutate_mode

    @property
    def mutate_chance(self):
        return self._mutate_chance

    @mutate_chance.setter
    def mutate_chance(self, mutate_chance):
        assert isinstance(mutate_chance, int)
        self._mutate_chance = mutate_chance

    def generate_and_check_query(self, query: str = '', parent_node: str = '', check: bool = False, start_rule: str = 'root'):
        query_generator = self.generate_query(query=query, parent_node=parent_node, check=check, start_rule=start_rule)
        antlr = self._check_antlr4_parser()
        original = self._check_original_parser(user=self._user, password=self._password, host=self._host, database=self._database, err=self._err)
        antlr.send(None), original.send(None)

        for query in query_generator:
            antlr.send(query), original.send(query)
            yield (query, self._status_original, self._status_antlr4)

        antlr.close()
        original.close()

    def generate_query(self, query: str = '', parent_node: str = '', check: bool = False, start_rule: str = 'root'):
        if self._fuzzing_mode == 'random_query':
            generator_mode = RandomQuery(**self.__dict__, start_rule=start_rule)
        elif self._fuzzing_mode == 'fuzzing_sql_forms':
            generator_mode = SqlForms(**self.__dict__, query=query, parent_node=parent_node, check=check)
        else:
            raise SettingFuzzerError('Unknown fuzzing mode {}'.format(self._fuzzing_mode))
        return generator_mode.generate()

    def set_position(self, position_type: str = 'single', start_position: int = 0, end_position: int = 1) -> None:
        if position_type == 'single':
            self._start_position = start_position
            self._end_position = start_position + 1
        elif position_type == 'custom_range':
            self._start_position = start_position
            self._end_position = end_position
        elif position_type == 'default range':
            pass
        else:
            raise SettingFuzzerError("wrong value position_type")

    def _read_grammar_file(self) -> None:
        regular_expression = re.compile(r'(\w*\n?\s*):([^\n][^;]*)')  # need fix for support:  "SEMI: ';'; "
        with open(self._parser_file, 'r') as grammar_file:
            result = re.findall(regular_expression, grammar_file.read())
        if self._lexer_file is not None:
            with open(self._lexer_file, 'r') as grammar_file:
                self.exception_rule = re.findall(regular_expression, grammar_file.read())
                result += self.exception_rule
        self.exception_rule = list(map(lambda x: x[0].replace('\n', '').replace('  ', ''), self.exception_rule))
        for delete_rule in self._access_rule_in_lexer_file:
            self.exception_rule.remove(delete_rule)
        for i in result:
            scanner = ScannerAntl(i[1])
            tokens = scanner.scan_tokens()
            parser = Parser(tokens)
            tree = parser.parse()
            self._rule_dictionary[i[0].replace('\n', '').replace('  ', '').rstrip(' ')] = tree

    def set_probability(self, multiplication_scale: int = 1, random_scale: int = 1) -> None:
        if all(map(lambda scale: scale >= 0, [multiplication_scale, random_scale])):
            self._multiplication_scale = multiplication_scale
            self._random_scale = random_scale
        else:
            raise SettingFuzzerError('wrong value multiplication_scale or random_scale')

    def _check_original_parser(self, user: str, password: str, host: str, database=None, err=None):
        pass

    def _check_antlr4_parser(self):
        pass

    def set_combined_mutate_rule(self, combined_mutate_rule=None):
        self._combined_mutate_rule = combined_mutate_rule

    def set_access_rule_in_lexer_file(self, access_rule_in_lexer_file=None):
        self._access_rule_in_lexer_file = access_rule_in_lexer_file


class MySqlGenerator(SQLGenerator):
    """
    MySql Generator.
    """

    def __init__(self, parser_file: str, lexer_file: str) -> None:
        super().__init__(parser_file, lexer_file, 'mysql')

    def _check_original_parser(self, user: str = 'root', password: str = 'toor', host: str = '127.0.0.1', database=None, err: bool = False):
        original_parser = MySqlParser(user=user, password=password, host=host, database=database, err=err)
        try:
            while 1:
                query = yield
                try:
                    self._status_original = original_parser.check_syntax(input_data=query)
                except InterfaceError:  # mysql.connector.errors.InterfaceError: 2003: Can't connect to MySQL server on '127.0.0.1:3306' (111 Connection refused)
                    print("DOWN")
                    os.popen("sudo -S /etc/init.d/mysql restart", 'w').write(PASS_LIN)
                    os.wait()
                    self._status_original = original_parser.check_syntax(input_data=query)
        except GeneratorExit:
            pass

    def _check_antlr4_parser(self):
        antlr4_parser = CheckMySQLAntlr()
        try:
            while 1:
                query = yield
                self._status_antlr4 = antlr4_parser.check_syntax(input_data=query)
        except GeneratorExit:
            pass


class TransactSqlGenerator(SQLGenerator):
    """
    T-Sql Generator.
    """
    def __init__(self, parser_file: str, lexer_file: str) -> None:
        super().__init__(parser_file, lexer_file, 'tsql')

    def _check_original_parser(self, user: str = 'root', password: str = 'toor', host: str = '127.0.0.1', database=None, err: bool = False):
        original_parser = TSQlParser(user=user, password=password, host=host, database=database, err=err)
        try:
            while True:
                query = yield
                self._status_original = original_parser.check_syntax(input_data=query)
        except GeneratorExit:
            pass

    def _check_antlr4_parser(self):
        antlr4_parser = CheckTSQLAntlr()
        try:
            while True:
                query = yield
                self._status_antlr4 = antlr4_parser.check_syntax(input_data=query)
        except GeneratorExit:
            pass


class GeneratorFactory(AbstractGeneratorFactory):

    @staticmethod
    def create(parser_file: str, lexer_file: str, sql: str) -> SQLGenerator:
        if sql == "mysql":
            return MySqlGenerator(parser_file, lexer_file)
        elif sql == "tsql":
            return TransactSqlGenerator(parser_file, lexer_file)
        else:
            raise SettingFuzzerError('Unknown sql type: {}'.format(sql))
