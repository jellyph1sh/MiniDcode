#coding:utf-8
import sqlite3

def connection(file):
    return sqlite3.connect(file)

def leave(db):
    db.close()
    return True

def getsomething(file, something):
    try:
        db = connection(file)
        cursor = db.cursor()
        result = cursor.execute(f'SELECT * FROM {something}').fetchall()
        if result == []:
            result = '[WARN]', 'Aucun message n\'a encore été publié...'
    except Exception as error:
        result = '[ERROR]', error
        db.rollback()
    finally:
        try:
            leave(db)
        except:
            pass
        finally:
            return result

def putmessage(file, forum, *data):
    try:
        db = connection(file)
        for message in data:
            cursor = db.cursor()
            message = (cursor.lastrowid, message[0], message[1], message[2])
            cursor.execute(f'INSERT INTO t_{forum} VALUES(?,?,?,?)', message)
            db.commit()
            num = cursor.execute(f'SELECT * FROM t_forums WHERE forum_name = "{forum}" ').fetchone()[2]
            cursor.execute(f'UPDATE t_forums SET forum_mess = {num+1} WHERE forum_name = "{forum}" ')
            db.commit()
        result = 'Nouvelles données ajoutées !'
    except Exception as e:
        result = f'[ERROR] {e}'
        db.rollback()
    finally:
        try:
            leave(db)
        except:
            pass
        finally:
            return result

def startforum(file, forum):
    try:
        db = connection(file)
        cursor = db.cursor()
        cursor.execute(f"""CREATE TABLE "{'t_'+forum}" (
        	"id"	INTEGER,
        	"time"	TEXT,
        	"pseudo"	TEXT,
            "message"   TEXT,
        	PRIMARY KEY("id" AUTOINCREMENT)
        );""")
        db.commit()
        cursor = db.cursor()
        cursor.execute('INSERT INTO t_forums VALUES(?,?,?)', (cursor.lastrowid, forum, 0))
        db.commit()
        result = 'Forum créer avec succes'
    except Exception as e:
        result = f'[ERROR] {e}'
        db.rollback()
    finally:
        try:
            leave(db)
        except:
            pass
        finally:
            return result

def getforums(file):
    return getsomething(file, 't_forums')

def getmessages(file, forum):
    return getsomething(file, 't_'+forum)