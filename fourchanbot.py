import requests
import json
from io import StringIO
from html.parser import HTMLParser
import time
import sqlite3
import atexit

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

conn = sqlite3.connect('posts.db')
c = conn.cursor()

def exit_handler():
    conn.close()
    return

atexit.register(exit_handler)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

r = requests.get('https://a.4cdn.org/b/catalog.json')
r_d = r.json()
request_status = r.ok

def get_threads(key: str, default='NaN'):
    return threads.get(key, default)


def gen_chan():
    for idx, page in enumerate(r_d):
        for thread in r_d[idx]['threads']:
            yield thread


while request_status:
    conn = sqlite3.connect('posts.db')
    c = conn.cursor()

    for threads in gen_chan():
        

        text = strip_tags(get_threads('com'))
        number = int(get_threads('no'))
        
        c.execute('SELECT * FROM thread WHERE (post_text=? AND no=?)', (text, number))
        entry = c.fetchone()

        if entry is None:
            c.execute('INSERT INTO thread(post_text, no) VALUES (?, ?)', (text, number))
        else:
            pass
        if 'last_replies' in threads:
            for comment in threads['last_replies']:
                com = strip_tags(comment.get('com', 'NaN'))
                c.execute('SELECT * FROM comment WHERE (com=? AND no=?)', (com, number))
                db_com = c.fetchone()
                if db_com is None:
                    c.execute('INSERT INTO comment(com, no) VALUES (?, ?)', (com, number))
        else:
            pass
        conn.commit()
        
    time.sleep(2)




