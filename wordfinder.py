# Ryan Hutchings
# Unit 21.4 Python OOP Exercises

"""Word Finder: finds random words from a dictionary.
"""
from random import choice #for randomly choosing a word from the word list

class WordFinder:
    """
    Retrieves a random word using a word list from a text file

    Attributes:
    -------------------------
    filepath: str
        saves the filepath for reading a text file of words
    words_read: function (returns list)((runs automatically))
        runs a function to read a text file of words and returns a list of them
    file: function 
        runs a functions to open, read or write, and close a file

    My Tests
    -------------------------
    >>> wf = WordFinder("short_list_of_words.txt")
    11 words read

    >>> wf.filepath
    'short_list_of_words.txt'

    #The list in these tests is in the 'short_list_of_words.txt' file (easier for testing)
    >>> wf.random() in ['biscuitts', 'gravy', 'cat', 'dog', 'ferret', 'people', 'love', 'peace', 'world', 'sleep', 'repeat']
    True

    >>> wf.random() in ['biscuitts', 'gravy', 'cat', 'dog', 'ferret', 'people', 'love', 'peace', 'world', 'sleep', 'repeat']
    True

    >>> wf.random() in ['biscuitts', 'gravy', 'cat', 'dog', 'ferret', 'people', 'love', 'peace', 'world', 'sleep', 'repeat']
    True

    >>> wf.random() in ['biscuitts', 'gravy', 'cat', 'dog', 'ferret', 'people', 'love', 'peace', 'world', 'sleep', 'repeat']
    True

    """
    def __init__(self, filepath):
        self.filepath = filepath
        file = open(self.filepath, 'r')
        self.words_read = self.addWordsToListAndPrintResults(file)
        print(f'{len(self.words_read)} words read')
        file.close()

    def addWordsToListAndPrintResults(self, file):
        """Reads through the text file, adds all the new words to the read list, and returns the list of read words"""
        list_of_words = []
        new_line = '\n'
        for word in file:
            if (word == new_line): 
                break

            if (word not in list_of_words):
                if word.endswith(new_line):
                    list_of_words.append(word[:-1])
                else:
                    list_of_words.append(word)
        return list_of_words
    
    def random(self):
        """Returns a randomly picked word from the words_read list"""
        random_word = choice(self.words_read)
        return random_word


    
    

# Test
# short_list_of_words = WordFinder('short_list_of_words.txt')
# print(short_list_of_words.random() in short_list_of_words.words_read)

