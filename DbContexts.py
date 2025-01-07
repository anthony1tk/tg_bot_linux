import pyodbc
import datetime

def DbContext_saveuser(message):
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=localhost;'
            'DATABASE=QuickMedia_bot;'
            'USERNAME=root;'
            'PASSWORD=AnthonyY05Y!;'
            'TrustServerCertificate=True;'
        )
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
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=localhost;'
            'DATABASE=QuickMedia_bot;'
            'USERNAME=root;'
            'PASSWORD=AnthonyY05Y!;'
            'TrustServerCertificate=True;'
        )
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
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=localhost;'
            'DATABASE=QuickMedia_bot;'
            'USERNAME=root;'
            'PASSWORD=AnthonyY05Y!;'
            'TrustServerCertificate=True;'
        )

        print(f"Connection successful!      [{datetime.datetime.now()}]")
        language = user_language(connection, message)
        return language
    except Exception as e:
        print("Error:", e)

    finally:
        if 'connection' in locals() and connection:
            connection.commit()
            connection.close()
            print(f"Connection closed.      [{datetime.datetime.now()}]")
        



def save_user(connection, message):
    cursor = connection.cursor()
    cursor.execute("SELECT CASE WHEN EXISTS (SELECT 1 FROM users WHERE user_chat = (?)) THEN 'TRUE' ELSE 'FALSE' end as query;", (message))
    row = cursor.fetchone()
    if ('FALSE' in row):
        cursor.execute("INSERT INTO users (user_chat) VALUES (?);", (message))
        print(f"{message} added.      [{datetime.datetime.now()}]")
    else:
        print(f"{message} already exists.      [{datetime.datetime.now()}]")
    cursor.close()

def set_language(connection, language, message):
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET user_language = (?) WHERE user_chat = (?);", (language, message))
    print(f"Language updated successfully!      [{datetime.datetime.now()}]")
    cursor.close() 


def user_language(connection, message):
    cursor = connection.cursor()
    cursor.execute(f"SELECT user_language from users where user_chat=(?);", (message))
    row = cursor.fetchone()
    if("russian" in  row):
        language = 'russian'
    elif("english" in row):
        language = 'english'
    else:
        language = None
    return language

