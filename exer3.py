#  Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

'''word = 'banana'
count = 0
for letter in word:
    if word == 'a':
        count = count + 1
print(count)'''


def letterCounter(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count = count + 1
    return count


word = input('Please type a word: ')
try:
    inputWord = str(word)
except:
    print('This is not a word')
    exit()
letter = input('Please type a letter: ')
print(letterCounter)
