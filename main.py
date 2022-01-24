from urllib.request import urlopen
import re

TABOO_URL = "https://playtaboo.com/ajax/v1/next/?"
SAVED_CARDS = "taboo.txt"

def parseOutput(url):
    '''
    Examples Input/Output
    Input: https://playtaboo.com/ajax/v1/next/?1624643694954
    Output: (GOVERNOR, ['STATE', 'REPRESENTATIVE', 'LEADER', 'EACH', 'ELECT'])
    
    Note: gameWordQuery is based on the string format of the current ajax query.
    '''
    string = str(urlopen(url).read())

    gameWordQuery = r'game-word\\\\">' + '(.*?)' + r'<\\\\/h2>' # searches for word (any chars) between 2 raw strings
    gameWord = re.search(gameWordQuery, string).group(1) # matches first ()-group finding

    listItemsQuery = r'<li>'+'(.*?)'+r'<\\\\/li>'
    listWords = re.findall(listItemsQuery, string)

    return (gameWord, listWords)

def promptUser():
    '''
    Prompt user for number of taboo cards to print.
    '''
    try:
        numCards = int(input("How many taboo cards do you need? Enter number: "))
    except:
        print("That wasn't a number, try again?")
        numCards = promptUser()
    return numCards


numCards = promptUser()
print("Printing",numCards,"cards:")

# Print each taboo card and save output to file.
with open(SAVED_CARDS, "a+") as file:
    for num in range(numCards):
        url = TABOO_URL + str(num)
        data = parseOutput(url)
        file.write(str(data) + "\n")
        print(data)
