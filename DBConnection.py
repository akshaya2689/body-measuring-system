import mysql.connector


class Db:
    def __init__(self):
        self.cnx = mysql.connector.connect(host="localhost",user="root",password="",database="capturemeasure")
        self.cur = self.cnx.cursor(dictionary=True)


    def select(self, q):
        print()
        self.cur.execute(q)
        return self.cur.fetchall()

    def selectOne(self, q):
        self.cur.execute(q)
        return self.cur.fetchone()


    def insert(self, q):

        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.lastrowid

    def update(self, q):
        print()
        a=self.cur.execute(q)
        self.cnx.commit()
        return a

    def delete(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount

