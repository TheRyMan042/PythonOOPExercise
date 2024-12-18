# Ryan Hutchings
# Unit 21.4 Python OOP Exercises

"""Subclass Word Finder: finds random words, including subclasses of words, from a dictionary.
"""
from wordfinder import WordFinder #import the class from another file
from random import choice #for randomly choosing a word from the word list

class SubclassWordFinder(WordFinder):
    """
    Retrieves a random word using some subclasses of word lists from a text file

    Attributes:
    -------------------------
    filepath: str
        saves the filepath for reading a text file of words
    words_read_subclasses: function (returns list)((runs automatically))
        runs a function to read a text file of words with subclasses and returns a list of words with subclasses in their own list
    file: function 
        runs a functions to open, read or write, and close a file
    
    My Tests
    -------------------------
    >>> subclass_words = SubclassWordFinder('word_list_with_subclasses.txt')
    3 subclasses read

    >>> subclass_words.filepath
    'word_list_with_subclasses.txt'

    #The list in these tests is in the 'word_list_with_subclasses.txt' file (easier for testing)
    >>> subclass_words.subclass_random() in ['cat', 'dog', 'ferret', 'biscuitts', 'gravy', 'banana', 'sleep', 'climb', 'run', 'dance'] 
    True

    >>> subclass_words.subclass_random() in ['cat', 'dog', 'ferret', 'biscuitts', 'gravy', 'banana', 'sleep', 'climb', 'run', 'dance']
    True

    >>> subclass_words.subclass_random() in ['cat', 'dog', 'ferret', 'biscuitts', 'gravy', 'banana', 'sleep', 'climb', 'run', 'dance']
    True

    >>> subclass_words.subclass_random() in ['cat', 'dog', 'ferret', 'biscuitts', 'gravy', 'banana', 'sleep', 'climb', 'run', 'dance']
    True

    """

    def __init__(self, filepath):
        self.filepath = filepath
        file = open(self.filepath, 'r')
        self.words_read_subclasses = self.read_subclass_words(file)
        print(f'{len(self.words_read_subclasses)} subclasses read')
        file.close()

    def read_subclass_words(self, file):
        """Reads through the file, filters out the subclass lists and adds the words into separate lists, and returns all the lists into the main list"""
        subclasses_of_words = []
        for word in file:
            if '#' in word:
                subclass = super().addWordsToListAndPrintResults(file)
                subclasses_of_words.append(subclass)
        return subclasses_of_words
    
    def subclass_random(self):
        """Returns a randomly picked word from a randomly picked subclass using the words_read_subclasses list"""
        random_subclass = choice(self.words_read_subclasses)
        # print(random_subclass)
        return choice(random_subclass)
            


# Test
# subclass_words = SubclassWordFinder('word_list_with_subclasses.txt')
# subclass_words.subclass_random()