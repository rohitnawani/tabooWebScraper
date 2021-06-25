from urllib.request import urlopen
import re

def ParseOutput(url):
    '''
    Examples Input/Output
    Input: https://playtaboo.com/ajax/v1/next?1624643694954
    Output: (GOVERNOR, ['STATE', 'REPRESENTATIVE', 'LEADER', 'EACH', 'ELECT'])
    '''
    string = str(urlopen(url).read())

    gameWordQuery = '<h2 class="game-word">(.*?)</h2>'
    gameWord = re.search(gameWordQuery, string).group(1)

    listItemsQuery = '<li>(.*?)</li>'
    listWords = re.findall(listItemsQuery, string)

    return (gameWord, listWords)

for num in range(100):
    url = "https://playtaboo.com/ajax/v1/next?" + str(num)
    data = ParseOutput(url)
    print(data)