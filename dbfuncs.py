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

def add_card_to_pack(GameIDC, CardID, GameIDP, PackName):
    # Puts cards into a pack
    # Uses the inputs from Cards, then Packs
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    conn.execute("INSERT INTO PACK_GETS_CARD (GAME_ID_C,CARD_ID,GAME_ID_P, PACK_NAME) \
          VALUES (?,?,?,?)", (GameIDC, CardID, GameIDP, PackName));
    conn.commit()
    conn.close()

def get_pack_gameid(packname):
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    cursor= conn.execute("SELECT GAME_ID, PACK_NAME from PACKS")
    for row in cursor:
        if row[1] == packname:
            packinfo = row[0]
            return packinfo
    return "TEST GAME"

def create_card(GameID, CardID, CardName, GameName, CardRarity):
    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO CARDS (GAME_ID,CARD_ID,CARD_NAME,GAME_NAME, RARITY) \
          VALUES (?,?,?,?,?)", (GameID, CardID, CardName, GameName, CardRarity));

    conn.commit()
    conn.close()

def get_cards_from_pack(packname):
    # Selects all Cards in a pack based on user choice of the name
    conn = sqlite3.connect('database.db')
    SelectPack = packname
    CardNamer = conn.execute("SELECT CARD_NAME, CARD_ID from CARDS")
    PackNum = conn.execute("SELECT CARD_ID, PACK_NAME from PACK_GETS_CARD")
    PackIDs = []
    output = []
    for packRow in PackNum:
        if (packRow[1] == SelectPack):
            PackIDs.append(packRow[0])
    for cardRow in CardNamer:
        for packRow in PackIDs:
            if (cardRow[1] == packRow):
                output.append(cardRow[0])

    conn.close()
    return output