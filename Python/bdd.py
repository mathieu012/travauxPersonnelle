import mysql.connector
import random
from mysql.connector import errorcode

conn = mysql.connector.connect(host="db4free.net", user='rootmat81',password="x-8@WDgRs4iN4AN" ,
                            database='english81')
cursor = conn.cursor()

#Sélectionne un mot et sa traduction de manière aléatoire
def selectRandom():
    
    cursor.execute("""SELECT id FROM vocabulaire""")
    idx = cursor.fetchall()
    N = random.randint(0,(len(idx)-1))
    idN = str(idx[N][0])
    

    cursor.execute("""SELECT word, mot FROM vocabulaire where id =""" + idN)
    data = cursor.fetchone()
    print("word = "+data[0])
    print("mot = "+data[1])
    return data

def insertVocabulaire(english, traduction):
    try:
        requete = ("INSERT INTO vocabulaire (word, mot) VALUES('" + english + "', '"+ traduction + "')" )
        cursor.execute(requete)
        conn.commit()
        return "SUCCESS"

    except :
        conn.rollback()
        return "ERROR"

def verif(english, traduction):
    cursor.execute("""SELECT word, mot FROM vocabulaire""")
    data = cursor.fetchall()

    for row in data :
        
        if row[0] == english : 
            print("This vocabulary is already entered")
            print("Please choose an other option")
            return "1"
            
            

    
def close():
    conn.close()