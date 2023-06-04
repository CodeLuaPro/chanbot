import requests
import json
from io import StringIO
from html.parser import HTMLParser
import time
import sqlite3

conn = sqlite3.connect('posts.db')

c = conn.cursor()

'''
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

r = requests.get('https://a.4cdn.org/b/catalog.json')
r_d = r.json()
request_status = r.ok
'''
#text = strip_tags(r_d[0]['threads'][0]['com'])
#id = int(r_d[0]['threads'][0]['no'])

#c.execute("INSERT INTO thread VALUES (?, ?)", (comment, id))

'''
c.execute("""CREATE TABLE thread (
            post_text text,
            no integer
            )""")
'''

#can use 'with conn:' to avoid conn.commit()

#c.execute("INSERT INTO thread VALUES ('This is a test of 4chanbot', 0)")

#c.execute("SELECT * FROM thread WHERE (com=? AND no=?)", ('This is a test of 4chanbot', 0))
c.execute("SELECT * FROM comment")
#c.execute('INSERT INTO thread(com, no) VALUES (?, ?)', ('heheheha', 1))
print(c.fetchall())


conn.commit()
conn.close()