from urllib.request import urlopen
import re

TABOO_URL = "https://playtaboo.com/ajax/v1/next/?"
SAVED_CARDS = "taboo.txt"

def parse_output(url):
    '''
    Examples Input/Output
    Input: https://playtaboo.com/ajax/v1/next/?1624643694954
    Output: (GOVERNOR, ['STATE', 'REPRESENTATIVE', 'LEADER', 'EACH', 'ELECT'])

    Note: game_word_query is based on the string format of the current ajax query.
    '''
    string = ''
    with urlopen(url) as response:
        string = str(response.read())

    # searches for word (any chars) between 2 raw strings
    game_word_query = r'game-word\\\\">' + '(.*?)' + r'<\\\\/h2>'
    game_word = re.search(game_word_query, string).group(1) # matches first ()-group finding

    list_items_query = r'<li>'+'(.*?)'+r'<\\\\/li>'
    list_words = re.findall(list_items_query, string)

    return (game_word, list_words)

def prompt_user():
    '''
    Prompt user for number of taboo cards to print.
    '''
    try:
        num_cards = int(input("How many taboo cards do you need? Enter number: "))
    except:
        print("That wasn't a number, try again?")
        num_cards = prompt_user()
    return num_cards


num_cards = prompt_user()
print("Printing",num_cards,"cards:")

# Print each taboo card and save output to file.
with open(SAVED_CARDS, "a+") as file:
    for num in range(num_cards):
        URL = TABOO_URL + str(num)
        data = parse_output(URL)
        file.write(str(data) + "\n")
        print(data)
