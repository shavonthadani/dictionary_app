import mysql.connector
from difflib import get_close_matches

def closeConn():
    cursor.close()
    con.close()
def translate(w):
    #create connection
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

    #print results
    if results:
        number = 0
        definition = ""
        for result in results:
            number = number + 1
            definition += str(number) + ". " + result[0] + "\n"
        return (w, definition)

    #Gets words to look for similarities might have error
    word_search = cursor.execute("SELECT Expression FROM Dictionary")
    words = cursor.fetchall()
    wordsf = []
    for word in words:
        wordsf.append(word[0])
    if len(get_close_matches(w,wordsf)) > 0:
        word = get_close_matches(w, wordsf)[0]

        sec_search = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
        sec_def = cursor.fetchall()
        definition = ""
        num =0
        for result in sec_def:
            num = num + 1
            definition += str(num) + ". "+ result[0] + "\n"
        return (word, definition)
    else:
        return(w,"No word found!")

#word = input("enter word: ")

#output = translate(word)
#print(output)
