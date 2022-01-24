from urllib.request import urlopen
import re

def parseOutput(url):
    '''
    Examples Input/Output
    Input: https://playtaboo.com/ajax/v1/next/?1624643694954
    Output: (GOVERNOR, ['STATE', 'REPRESENTATIVE', 'LEADER', 'EACH', 'ELECT'])
    '''
    string = str(urlopen(url).read())

    gameWordQuery = r'game-word\\\\">'+'(.*?)'+r'<\\\\/h2>'
    gameWord = re.search(gameWordQuery, string).group(1) # matches first () group finding

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
with open("taboo.txt", "a+") as file:
    for num in range(numCards):
        url = "https://playtaboo.com/ajax/v1/next/?" + str(num)
        data = parseOutput(url)
        file.write(str(data) + "\n")
        print(data)
