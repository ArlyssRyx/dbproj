#Table Commit, USER - Use initially, not in Final:
#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE USERNAMES
         (USERNAME TEXT(15) PRIMARY KEY UNIQUE);''')
print ("Table created successfully");



#Table Commit, Decks
conn.execute('''CREATE TABLE DECKS
         (USERNAME CHAR(15) REFERENCES USERNAMES(USERNAME),
         DECK_NAME CHAR(80) NOT NULL,
         NUM_CARDS INT,
         GAME_ID INT NOT NULL);''')
print ("Table created successfully");



#Table Commit, Has Stats
conn.execute('''CREATE TABLE PLAYER_HAS_STATS
         (USERNAME CHAR(15) REFERENCES USERNAMES(USERNAME),
         NAME CHAR(80) REFERENCES STATS(NAME));''')
print ("Table created successfully");



#Table Commit, Stats
conn.execute('''CREATE TABLE STATS
         (NAME TEXT PRIMARY KEY,
         VALUE INT DEFAULT 0);''')
print ("Table created successfully");



#Table Commit, Deck Cards
conn.execute('''CREATE TABLE DECK_CONTAINS_CARD
         (USERNAME CHAR(15) REFERENCES USERNAMES(USERNAME),
         DECK_NAME CHAR(80) REFERENCES DECKS(DECK_NAME),
         GAME_ID INT REFERENCES CARDS(GAME_ID),
         CARD_ID INT REFERENCES CARDS(CARD_ID));''')
print ("Table created successfully");



#Table Commit, Cards
conn.execute('''CREATE TABLE CARDS
         (GAME_ID INT,
         CARD_ID INT PRIMARY KEY,
	    CARD_NAME CHAR(80) NOT NULL,
         GAME_NAME CHAR(80) NOT NULL,
         RARITY TEXT);''')
print ("Table created successfully");



#Table Commit, Tags
conn.execute('''CREATE TABLE TAGS
         (GAME_ID INT REFERENCES CARDS(GAME_ID),
         CARD_ID INT REFERENCES CARDS(CARD_ID),
         TAG TEXT);''')
print ("Table created successfully");



#Table Commit, Pack get cards
conn.execute('''CREATE TABLE PACK_GETS_CARD
         (GAME_ID_C INT REFERENCES CARDS(GAME_ID),
         CARD_ID INT REFERENCES CARDS(CARD_ID),
         GAME_ID_P INT REFERENCES PACKS(GAME_ID),
         PACK_NAME CHAR(80) REFERENCES PACKS(PACK_NAME));''')
print ("Table created successfully");



#Table Commit, Packs
conn.execute('''CREATE TABLE PACKS
         (GAME_ID INT NOT NULL,
         PACK_NAME CHAR(80) PRIMARY KEY,
         GAME_NAME CHAR(80),
         NUM_CARDS INT NOT NULL);''')
print ("Table created successfully");



#Table Commit, Rarities
conn.execute('''CREATE TABLE RARITIES
         (GAME_ID INT REFERENCES PACKS(GAME_ID),
         PACK_NAME CHAR(50) REFERENCES PACKS(PACK_NAME),
         RARITY TEXT);''')
print ("Table created successfully");

conn.close()