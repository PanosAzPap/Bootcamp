from random import choice

pickedWord = []
wordList = ['football', 'code', 'paper', 'bootcamp', 'employability', 'algorithm', 'function', 'island', 'communications', 'letter', 'skydive']
w = choice(wordList)
life = 7
lastLetter =[]
prevWord = 0

#  CREATES WORD OF DASHES
def emptyWord(lengthOfWord):
    word = []
    for i in range(lengthOfWord):
        word.insert(i, '_')
    return word

#  TRANSFORMS STRING TO LIST
def listWord(word):
    wordToList = []
    for i in range(len(word)):
        wordToList.append(word[i])
    return wordToList

#TRANSFORMS LIST TO STRING
def stringWord(List):
    listToWord = ''
    for i in range(len(List)):
        listToWord = listToWord + ' ' + List[i]
    return listToWord

#  DO THE TRANSFORMATIONS
pickedWord = listWord(w)
gWord = emptyWord(len(pickedWord))

#  PRINTS THE WORD TO GUESS
print(stringWord(gWord))

#  GAME PROCEDURE
while (pickedWord != gWord) and (life > 0):
    print('Used letters:', lastLetter)
    letter = input('Select a letter: ')

    for i in range(len(pickedWord)):
        if (pickedWord[i] == letter):
            gWord[i] = letter
            prevWord = prevWord + 1

#  IF WRONG REMOVE LIFE
    if (prevWord == 0):
        life = life - 1

    prevWord = 0
    lastLetter.append(letter)
    print(stringWord(gWord))
    print('Remain lives:',life)

#  CHECK WIN OR LOSE CONDITIONS
if (life == 0):
    print('You Lost! The word is', stringWord(pickedWord))
else:
    print('Congratulations! You WON!')
            

