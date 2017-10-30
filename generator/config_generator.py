from .generator import GeneratorFactory
import configparser

from .my_error import ConfigFileError, SettingFuzzerError


class ConfigGenerator(object):

    def __init__(self, config_file: str):
        self.check_original = None
        # self.check_antlr = None
        self._config_file = configparser.ConfigParser()
        self._config_file.read(config_file)
        self._init_fuzzer()
        self.pprint()

    def _init_fuzzer(self):
        try:
            parser_file = self._config_file['antlr4_parser_setting']['parser_file']
            lexer_file = self._config_file['antlr4_parser_setting']['lexer_file']
            grammar_type = self._config_file['antlr4_parser_setting']['sql_type']
        except KeyError as e:
            raise ConfigFileError("Config file KeyError: Unknown antlr4 setting {}".format(e))
        try:
            self.generator = GeneratorFactory.create(parser_file, lexer_file, grammar_type)
            # self._init_antlr4_parser()
            self._init_original_parser()
            self._set_fuzzer_parameters()
        except SettingFuzzerError as e:
            print(e)
        self._init_print_parameters()

    def _init_original_parser(self):
        try:
            original_parser_setting = self._config_file['original_parser_setting']
            try:
                self.generator._user = original_parser_setting['user']
            except KeyError:
                print('not found user field! used default value: root')
                self.generator._user = 'root'
            try:
                self.generator._password = original_parser_setting['password']
            except KeyError:
                print('not found password field! used default value: toor')
                self.generator._password = 'toor'
            try:
                self.generator._host = original_parser_setting['host']
            except KeyError:
                print('not found host field! used default value: 127.0.0.1')
                self.generator._host = '127.0.0.1'
            try:
                self.generator._database = original_parser_setting['database']
            except KeyError:
                print('not found database field! used without database')
                self.generator._database = None

            try:
                self.generator._err = True if original_parser_setting['error_info'].lower() == 'true' else False
            except KeyError:
                print('not found error_info field! used default value: False')
                self.generator._err = False
        except KeyError:
            print('not found original_parser_setting field! used default value')

    def _set_fuzzer_parameters(self):

        # fuzzer probability
        try:
            multiplication_scale = int(self._config_file['fuzzing_setting']['multiplication_scale'])
        except KeyError:
            print('not found multiplication_scale field! used default value: {}'.format(self.generator._multiplication_scale))
            multiplication_scale = self.generator._multiplication_scale

        try:
            random_scale = int(self._config_file['fuzzing_setting']['random_scale'])
        except KeyError:
            print('not found random_scale field! used default value: {}'.format(self.generator._random_scale))
            random_scale = self.generator._random_scale
        self.generator.set_probability(multiplication_scale=multiplication_scale, random_scale=random_scale)

        # fuzzer mutate_mode
        try:
            self.generator.mutate_mode = True if self._config_file['fuzzing_setting']['mutate_mode'].lower() == 'true' else False
        except KeyError:
            print('not found mutate_mode field! used default value: {}'.format(self.generator.mutate_mode))
        try:
            self.generator.mutate_chance = int(self._config_file['fuzzing_setting']['mutate_chance'])
        except KeyError:
            print('not found mutate_chance field! used default value: {}'.format(self.generator.mutate_chance))

        # fuzzer mode
        try:
            self.generator._fuzzing_mode = self._config_file['fuzzing_setting']['fuzzing_mode']
        except KeyError:
            print('not found fuzzing_mode field! used default value: {}'.format(self.generator._fuzzing_mode))

        # if mode fuzzing_sql_forms then need set sql_forms_file
        try:
            self.generator._sql_forms = self._config_file['fuzzing_setting']['sql_forms_file']

        except KeyError:
            if self.generator._fuzzing_mode == 'fuzzing_sql_forms':
                raise ConfigFileError("Config file KeyError: If use mode fuzzing_sql_forms then need set sql_forms_file field")

        try:
            position_type = self._config_file['fuzzing_setting']['position_type']
        except KeyError:
            position_type = 'single'
            print('not found position_type field! used default value: {}'.format(position_type))

        try:
            start_position = int(self._config_file['fuzzing_setting']['start_position'])
        except KeyError:
            start_position = 0
            print('not found start_position field! used default value: {}'.format(start_position))

        try:
            end_position = int(self._config_file['fuzzing_setting']['end_position'])
        except KeyError:
            end_position = 1
            print('not found end_position field! used default value: {}'.format(end_position))

        self.generator.set_position(position_type=position_type, start_position=start_position, end_position=end_position)

        try:
            count_to_generate = int(self._config_file['fuzzing_setting']['count_to_generate'])
        except KeyError:
            count_to_generate = 1
            print('not found count_to_generate field! used default value: {}'.format(count_to_generate))
        self.generator._count_to_generate = count_to_generate

    def _init_print_parameters(self):
        try:
            self._log_brut = self._config_file['print_setting']['file_name']
        except KeyError:
            self._log_brut = None

        try:
            self._print_mode = int(self._config_file['print_setting']['print_mode'])
        except KeyError:
            self._print_mode = 0
            print('not found _print_mode field! used default value: {}'.format(self._print_mode))

        try:
            self.print_in_file = True if self._config_file['print_setting']['print_in_file'].lower() == 'true' else False
        except KeyError:
            self.print_in_file = False

        try:
            self.print_in_console = True if self._config_file['print_setting']['print_in_console'].lower() == 'true' else False
        except KeyError:
            self.print_in_console = False

    def pprint(self):
        if self.generator._fuzzing_mode.lower() == 'fuzzing_sql_forms':
            try:
                insert_node_name = self._config_file['fuzzing_setting']['insert_node_name']
            except KeyError:
                insert_node_name = 'root'
                print('not found insert_node_name field! used default value: {}'.format(insert_node_name))

            with open(self.generator._sql_forms, 'r') as forms:
                brut_query = [line[:-2] for line in forms]
            if self.print_in_file:
                try:
                    with open(self._log_brut, 'w') as _:
                        pass
                except TypeError:
                    raise ConfigFileError('if use print_in_file then need add field file_name in config file')

            try:
                start_query = int(self._config_file['fuzzing_setting']['start_query'])
            except KeyError:
                start_query = 0
            brut_query = brut_query[start_query:]

            for brut in brut_query:
                if self.print_in_file:
                    with open(self._log_brut, 'a') as log_brut_file:
                        log_brut_file.write('************************' + brut + '***************************************' + '\n')
                if self.print_in_console:
                    print('************************' + brut + '***************************************')

                list_sentence = self.generator.generate_and_check_query(query=brut, parent_node=insert_node_name, check=False)
                for sentence in list_sentence:
                    self._print(sentence)

        elif self.generator._fuzzing_mode.lower() == 'random_query':
            try:
                start_grammar_rule = self._config_file['fuzzing_setting']['start_grammar_rule']
            except KeyError:
                start_grammar_rule = 'root'
            list_sentence = self.generator.generate_and_check_query(start_rule=start_grammar_rule)
            for sentence in list_sentence:
                self._print(sentence)
        else:
            raise ConfigFileError('ValueError: not found {} in config file'.format(self.generator._fuzzing_mode.lower()))

    def _print(self, sentence: tuple):
        if not self._sentence_in_file(sentence[0]):
            if self._print_mode == 0:
                if not sentence[1] and not sentence[2]:
                    if self.print_in_file:
                        with open(self._log_brut, 'a') as log_brut_file:
                            log_brut_file.write("{}\n".format(sentence[0]))
                    if self.print_in_console:
                        print("{}".format(sentence[0]))

            elif self._print_mode == 1:
                if sentence[1] and sentence[2]:
                    if self.print_in_file:
                        with open(self._log_brut, 'a') as log_brut_file:
                            log_brut_file.write("{}\n".format(sentence[0]))
                if self.print_in_console:
                    print("{}".format(sentence[0]))

            elif self._print_mode == 2:
                if sentence[1] and not sentence[2]:
                    if self.print_in_file:
                        with open(self._log_brut, 'a') as log_brut_file:
                            log_brut_file.write("{}\n".format("original: {} antlr: {} sentence: {}\n".format(sentence[1], sentence[2], sentence[0])))
                    if self.print_in_console:
                        print("{}".format("original: {} antlr: {} sentence: {}\n".format(sentence[1], sentence[2], sentence[0])))

            elif self._print_mode == 3:
                if not sentence[1] and sentence[2]:
                    if self.print_in_file:
                        with open(self._log_brut, 'a') as log_brut_file:
                            log_brut_file.write("{}\n".format(sentence[0]))
                    if self.print_in_console:
                        print("{}".format(sentence[0]))

            elif self._print_mode == 4:
                if self.print_in_file:
                    with open(self._log_brut, 'a') as log_brut_file:
                        if sentence[0]:
                            log_brut_file.write("original: {} antlr: {} sentence: {}\n".format(sentence[1], sentence[2], sentence[0]))
                if self.print_in_console:
                    if sentence[0]:
                        print("original: {} antlr: {} sentence: {}".format(sentence[1], sentence[2], sentence[0]))

    def _sentence_in_file(self, sentence) -> bool:
        try:
            with open(self._log_brut, 'r') as file:
                for line in file:
                    if line[:-1] == sentence:
                        return True
        except FileNotFoundError:
            return False
        return False
