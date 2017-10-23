import mysql.connector
from mysql.connector import errorcode


class MySqlParser(object):

    def __init__(self, user: str='root', password: str='toor', host: str='127.0.0.1', database: str=None, err: bool=False):

        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self._err = err

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


def main():
    q = '''; select * from t;'''
    a = MySqlParser()
    print(a.check_syntax(q))


if __name__ == "__main__":
    main()
