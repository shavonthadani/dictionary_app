import mysql.connector
from difflib import get_close_matches
def translate(w):
    #create connection
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
        definition = ""
        for result in results:
            definition += result[0] + "\n"
        return definition

    #Gets words to look for similarities might have error
    word_search = cursor.execute("SELECT Expression FROM Dictionary")
    words = cursor.fetchall()
    wordsf = []
    for word in words:
        wordsf.append(word[0])
    if len(get_close_matches(w,wordsf)) > 0:
        word = get_close_matches(w, wordsf)[0]
        yn = input("Did you mean {} instead? Enter Y if yes or N or no. ".format(word))
        if yn == "Y":
            sec_search = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
            sec_def = cursor.fetchall()
            definition = ""
            for result in sec_def:
                definition += result[0] + "\n"
            return definition

        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "we did not understand your entry"
    else:
        return("No word found!")

word = input("enter word: ")

output = translate(word)
print(output)
