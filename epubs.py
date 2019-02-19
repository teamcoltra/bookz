import os
import sqlite3
import collections

dirs = ['./test']
exts = ['.txt']
formats = ['epub']
servers = ['!Ook', '!vadi']
variables = {}
database = "epubs.db"
global line

def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return None


def select_author(conn, author):
    sql = ''' SELECT ? FROM Authors '''
    cur = conn.cursor()
    cur.execute("SELECT ? FROM Authors", (author,))
    return cur.lastrowid


def insert_author(conn, author):
    sql = ''' INSERT INTO Authors(Name) VALUES(?) '''
    cur = conn.cursor()
    cur.execute("INSERT INTO Authors(Name) VALUES(?)", (author,))
    return cur.lastrowid


def select_series(conn, series):
    sql = ''' SELECT ? FROM Series '''
    cur = conn.cursor()
    cur.execute("SELECT ? FROM Series", (series,))
    return cur.lastrowid


def insert_series(conn, series):
    sql = ''' INSERT INTO Series(Name) VALUES(?) '''
    cur = conn.cursor()
    cur.execute("INSERT INTO Series(Name) VALUES(?)", (series,))
    return cur.lastrowid


def select_server(conn, server):
    #sql = 'SELECT ServerId FROM Servers WHERE handle = "' + str(server) + '";'
    sql = "SELECT ServerId FROM Servers WHERE handle = ?", (str(server),)
    cur = conn.cursor()
    #cur.execute(sql, server)
    cur.execute("SELECT ServerId FROM Servers WHERE handle = ?", (server,))
    return cur.lastrowid


def insert_server(conn, server):
    sql = ''' INSERT INTO Servers(Handle) VALUES(?) '''
    cur = conn.cursor()
    #cur.execute(sql, server)
    cur.execute("INSERT INTO Servers(Handle) VALUES(?)", (server,))
    return cur.lastrowid


def select_book(conn, title):
    sql = ''' SELECT ? FROM Books '''
    cur = conn.cursor()
    cur.execute("SELECT ? FROM Books", (title,))
    return cur.lastrowid


def insert_book(conn, server, author, series, title):
    #sql = ''' INSERT INTO Books(ServerId, AuthorId, SeriesId, Title) VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute("INSERT INTO Books(ServerId, AuthorId, SeriesId, Title) VALUES(?,?,?,?)", (server,author,series,title))
    return cur.lastrowid


def save_book(string):
    section = string.split('|')
    server=section[0].split(':')
    server_id=select_server(conn, server[1])
    if not server_id:
        server_id=insert_server(conn, server[1])

    author=section[1].split(':')
    author_id=select_author(conn, author[1])
    if not author_id:
        author_id=insert_author(conn, author[1])

    title=section[2].split(':')
    title_id=select_book(conn, title[1])
    if not title_id:
        title_id=insert_book(
            conn, server_id, author_id, '', title[1])

    return


def save_series(string):
    section = string.split('|')
    server=section[0].split(':')
    server_id=select_server(conn, server[1])
    if not server_id:
        server_id=insert_server(conn, server[1])

    author=section[1].split(':')
    author_id=select_author(conn, author[1])
    if not author_id:
        author_id=insert_author(conn, author[1])

    series=section[2].split(':')
    series_id=select_server(conn, series[1])
    if not series_id:
        series_id=insert_server(conn, series[1])

    title=section[2].split(':')
    title_id=select_book(conn, title[1])
    if not title_id:
        title_id=insert_book(conn, server_id, author_id, series_id, title[1])

    return


def ook_book(line):
    a=line.split(' - ')
    b=a[0].split(' ')
    b=list(filter(None, b))
    string='server:' + str(b[0]) + '|' + 'author:' + str(b[1])
    for i in range(2, len(b)):
        string += ' ' + str(b[i])
    string += '|' + 'name:'
    c=a[1].split('::')
    string += str(c[0]).strip()

    print(string)
    save_book(string)
    return


def ook_series(line):
    a=line.split(' - ')
    b=a[0].split(' ')
    b=list(filter(None, b))
    string='server:' + str(b[0]) + '|' + 'author:' + str(b[1])
    for i in range(2, len(b)):
        string += ' ' + str(b[i])
    string += '|' + 'series:' + str(a[1]).strip() + '|' + 'name: '
    c=a[2].split('::')
    string += str(c[0]).strip()

    print(string)
    save_series(string)
    return


def new_book(line):
    a=line.split(' - ')
    b=a[0].split(' ')
    b=list(filter(None, b))
    string='server:' + str(b[0]) + '|' + 'author:' + str(b[1])
    for i in range(2, len(b)):
        string += ' ' + str(b[i])
    string += '|' + 'name:'
    c=a[1].split('::')
    string += str(c[0]).strip()

    print(string)
    save_book(string)
    return


def new_series(line):
    a=line.split(' - ')
    b=a[0].split(' ')
    b=list(filter(None, b))
    string='server:' + str(b[0]) + '|' + 'author:' + str(b[1])
    for i in range(2, len(b)):
        string += ' ' + str(b[i])
    string += '|' + 'series:' + str(a[1]).strip() + '|' + 'name: '
    c=a[2].split('::')
    string += str(c[0]).strip()

    print(string)
    save_series(string)
    return


def vadi_book(line):
    a=line.split(' - ')
    b=a[0].split(' ')
    b=list(filter(None, b))
    string='server:' + str(b[0]) + '|' + 'author:' + str(b[1])
    for i in range(2, len(b)):
        string += ' ' + str(b[i])
    string += '|' + 'name:'
    c=a[1].split('::')
    string += str(c[0]).strip()

    print(string)
    save_book(string)
    return


def vadi_series(line):
    a=line.split(' - ')
    b=a[0].split(' ')
    b=list(filter(None, b))
    string='server:' + str(b[0]) + '|' + 'author:' + str(b[1])
    for i in range(2, len(b)):
        string += ' ' + str(b[i])
    string += '|' + 'series:' + str(a[1]).strip() + '|' + 'name: '
    c=a[2].split('::')
    string += str(c[0]).strip()

    print(string)
    save_series(string)
    return


def detect_server_template(line):
    a = line.split(" ")
    b = line.split(" - ")
    servers = {
        '!Ook': lambda x: ook_book(line) if x == 2 else ook_series(line),
        '!new': lambda x: new_book(line) if x == 2 else new_series(line),
        '!vadi': lambda x: vadi_book(line) if x == 2 else vadi_series(line),
    }
    if len(b) == 2 or len(b) == 3:
        servers[a[0]](len(b))
    else: print("line doesn't make sense: " + str(line))
    return

conn = create_connection(database)
with conn:
    for file in os.listdir(dirs[0]):
        if file.endswith(tuple(exts)):
            file_name=os.path.abspath(dirs[0]+"/"+file)
            print("file: " + str(file_name))
            for line in open(file_name):
                if any(format in str(line) for format in formats) and any(server in str(line) for server in servers):
                    print("line: " + str(line))
                    detect_server_template(line)
