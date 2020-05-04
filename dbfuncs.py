import sqlite3

def register_user(User):
    conn = sqlite3.connect('database.db')
    print ("Opened database successfully")

    UserGood = 1

    cursor = conn.execute("SELECT USERNAME from USERNAMES")
    for row in cursor:
        if(row[0] == User):
            print ("User already exists");
            UserGood = 0
            break;

    if(UserGood == 1):
        conn.execute("INSERT INTO USERNAMES(USERNAME) \
                        VALUES (?)", (User,));
        print ("User created successfully");

    conn.commit()
    conn.close()
    return UserGood

def check_user(User):
    conn = sqlite3.connect('database.db')
    print ("Opened database successfully")

    UserGood = 1

    cursor = conn.execute("SELECT USERNAME from USERNAMES")
    for row in cursor:
        if(row[0] == User):
            print ("User already exists");
            UserGood = 0
            break;

    conn.commit()
    conn.close()
    return UserGood