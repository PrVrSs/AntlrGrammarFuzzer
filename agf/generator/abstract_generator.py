"""Abstract Generator"""
import abc


class AbstractGenerator(abc.ABC):
    """
    Generator for generate sentence
    """
    def __init__(self):
        if isinstance(self, AbstractGenerator):
            raise NotImplementedError()

    @abc.abstractmethod
    def generate_and_check_query(self, query: str, parent_node: str, check: bool, start_rule: str):
        """
        :param query:
        :param parent_node:
        :param check:
        :param start_rule:
        :return:
        """

    @abc.abstractmethod
    def generate_query(self, query: str, parent_node: str, check: bool, start_rule: str):
        """
        :param query:
        :param parent_node:
        :param check:
        :param start_rule:
        :return:
        """

    @abc.abstractmethod
    def set_position(self, position_type: str, start_position: int, end_position: int) -> None:
        """
        :param position_type:
        :param start_position:
        :param end_position:
        :return:
        """

    @abc.abstractmethod
    def _read_grammar_file(self):
        """
        :return:
        """


class AbstractGeneratorFactory(abc.ABC):
    """Generator Factory"""

    @staticmethod
    @abc.abstractmethod
    def create(parser_file: str, lexer_file: str, sql: str):
        """
        :param parser_file: path to parser_file
        :param lexer_file: path to lexer_file
        :param sql: sql type: mysql/tsql
        :return: SQLGenerator
        """
