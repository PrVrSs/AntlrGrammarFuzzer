"""checker"""
import pyodbc
import mysql.connector
from mysql.connector import errorcode


class SQLParser:
    def __init__(self, user: str = 'root', password: str = 'toor', host: str = '127.0.0.1', database: str = None, err: bool = False):

        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self._err = err

    def check_syntax(self, input_data: str) -> bool:
        pass


class MySqlParser(SQLParser):

    def __init__(self, user: str = 'root', password: str = 'toor', host: str = '127.0.0.1', database: str = None, err: bool = False):
        super().__init__(user=user, password=password, host=host, database=database, err=err)

    def check_syntax(self, input_data: str) -> bool:
        if self.database is None:
            cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host)
        else:
            cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
        cursor = cnx.cursor()
        try:
            cursor.execute(input_data)
        except mysql.connector.Error as err:
            if self._err:
                print('error :{}\n query: {}'.format(err, input_data))
            if err.errno == errorcode.ER_PARSE_ERROR:
                cnx.close()
                return False
        cnx.close()
        return True


class TSQlParser(SQLParser):

    def __init__(self, user: str = 'sa', password: str = 'toor', host: str = 'localhost', database: str = 'SampleDB', err: bool = False):
        super().__init__(user=user, password=password, host=host, database=database, err=err)

    def check_syntax(self, input_data: str) -> bool:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + self.host + ';PORT=1443;DATABASE=' + self.database + ';UID=' + self.user + ';PWD=' + self.password)
        cursor = cnxn.cursor()
        try:
            cursor.execute(input_data)
        except pyodbc.ProgrammingError as exc:
            if self._err:
                print(f'error :{exc}\nquery: {input_data}')
            if 'Incorrect syntax near' in str(exc):
                return False
        except pyodbc.OperationalError:
            return False
        except pyodbc.DataError:
            return False
        return True


def main():
    query = '''; select * from t;'''
    parser = MySqlParser()
    print(parser.check_syntax(query))


if __name__ == "__main__":
    main()
