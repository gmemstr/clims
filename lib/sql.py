import MySQLdb

class SqlHandler:
    def __init__(self):
        self.db = MySQLdb.connect(user="root",db="blog")
        self.c = self.db.cursor()

    def NewPost(self, title,text):
        self.c.execute("INSERT INTO blog (title, body) VALUES (%s,%s)",
            (title, text))
        self.db.commit()

    def GetPost(self,post="all"):
        self.c.execute("SELECT * FROM blog")
        return self.c.fetchall()