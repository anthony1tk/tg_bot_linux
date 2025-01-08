import pymysql
import datetime

def DbContext_saveuser(message):
    try:
        connection = pymysql.connect(host="localhost", user="admin", password="589674", database="quickmedia_bot")
        print(f"Connection successful!      [{datetime.datetime.now()}]")
        save_user(connection, message)
    except Exception as e:
        print("Error:", e)

    finally:
        if 'connection' in locals() and connection:
            connection.commit()
            connection.close()
            print(f"Connection closed.      [{datetime.datetime.now()}]")

def DbContext_setlanguage(language, message):
    try:
        connection = pymysql.connect(host="localhost", user="admin", password="589674", database="quickmedia_bot")

        print(f"Connection successful!      [{datetime.datetime.now()}]")
        set_language(connection, language, message)
    except Exception as e:
        print("Error:", e)

    finally:
        if 'connection' in locals() and connection:
            connection.commit()
            connection.close()
            print(f"Connection closed.      [{datetime.datetime.now()}]")

def DbContext_language(message):
    try:
        connection = pymysql.connect(host="localhost", user="admin", password="589674", database="quickmedia_bot")

        print(f"Connection successful!      [{datetime.datetime.now()}]")
        language = userlanguage(connection, message)
        return language
    except Exception as e:
        print("Error:", e)

    finally:
        if 'connection' in locals() and connection:
            connection.commit()
            connection.close()
            print(f"Connection closed.          [{datetime.datetime.now()}]")
        



def save_user(connection, message):
    cursor = connection.cursor()
    cursor.execute(f"SELECT CASE WHEN EXISTS (SELECT 1 FROM users WHERE userchat = %s) THEN 'TRUE' ELSE 'FALSE' end as query;", (message,))
    row = cursor.fetchone()
    if ('FALSE' in row):
        cursor.execute(f"INSERT INTO users (userchat) VALUES (%s);", (message,))
        print(f"{message} added.      [{datetime.datetime.now()}]")
    else:
        print(f"{message} already exists.      [{datetime.datetime.now()}]")
    cursor.close()

def set_language(connection, language, message):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE users SET userlanguage = %s WHERE userchat = %s;", (language, message,))
    print(f"Language updated successfully!    [{datetime.datetime.now()}]")
    cursor.close() 


def userlanguage(connection, message):
    cursor = connection.cursor()
    cursor.execute(f"SELECT userlanguage from users where userchat= %s;", (message,))
    row = cursor.fetchone()
    if("russian" in  row):
        language = 'russian'
    elif("english" in row):
        language = 'english'
    else:
        language = None
    return language

