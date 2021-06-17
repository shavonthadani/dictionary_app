#model.py
#Shavon Thadani
#Script is the backend for dictionary.py
#06/17/2021
import mysql.connector
from difflib import get_close_matches

class Model:
    #returns a tuple of the word and the definition
    def translate(self, w):
        #create connection to database
        global con
        global cursor
        con = mysql.connector.connect(
        user = "ardit700_student",
        password = "ardit700_student",
        host = "108.167.140.122",
        database = "ardit700_pm1database"
        )
        #make a cursor to go through the table
        cursor = con.cursor()
        #find the results
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % w)
        results = cursor.fetchall()

        w = w.lower()

        #format the results and return
        if results:
            number = 0
            definition = ""
            for result in results:
                number = number + 1
                definition += str(number) + ". " + result[0] + "\n"
            return (w, definition)

        #If not exact match
        #get all words from database, compare how similar they are, find definition for most similar word
        word_search = cursor.execute("SELECT Expression FROM Dictionary")
        words = cursor.fetchall()
        wordsf = []
        for word in words:
            wordsf.append(word[0])
        #found a similar result
        if len(get_close_matches(w,wordsf)) > 0:
            word = get_close_matches(w, wordsf)[0]
            sec_search = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
            sec_def = cursor.fetchall()
            definition = ""
            num =0
            #format output and return
            for result in sec_def:
                num = num + 1
                definition += str(num) + ". "+ result[0] + "\n"
            return (word, definition)
        #no similar word found
        else:
            return(w,"No word found!")
