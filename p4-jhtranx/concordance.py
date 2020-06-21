from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance


    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        #create empty stop hash table
        self.stop_table = HashTable(191)
        #try to see if there is a file
        try:
            file = open(filename, 'r')
            for word in file:
                self.stop_table.insert(word.strip(), 0)
            file.close()
        #catch file not found error
        except FileNotFoundError:
            raise FileNotFoundError


    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        #create empty concordance table
        self.concordance_table = HashTable(191)

        try:
            file = open(filename, 'r')
            lineCount = 0
            fileContent = file.read()
            #removes apostrophes
            fileContent = fileContent.replace("'", "")
            #converts all punctuation to spaces
            fileContent = fileContent.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))) 
            #make content all lower case
            fileContent = fileContent.lower()
            #spilt into lines
            fileContent = fileContent.split('\n')

            for line in fileContent: #for every line in file
                lineCount += 1 #increase line count by 1
                line = line.split() # split line into a list of words
                line = list(dict.fromkeys(line)) # create a dict so that duplicate words are deleted
                # print(line) #PRINT DEBUG
                for word in line: #iterate through words in line
                    # print(word) #PRINT DEBUG
                    if word.isalpha(): #if the word is completely made up of chars
                        if not self.stop_table.in_table(word): #if the word is not in the stop table
                            self.concordance_table.insert(word, lineCount) #insert word to the concordance table
            file.close()
        #when file is not found
        except FileNotFoundError:
            raise FileNotFoundError



    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        #get all words(keys)
        wordList = self.concordance_table.get_all_keys()
        #sort the word list so that it is alphabetical
        wordList.sort()
        # print(wordList) #PRINT DEBUG

        #create a new file to write in
        file = open(filename, 'w')
        #get line list for each word
        for word in wordList:
            currentIndex = self.concordance_table.get_index(word)
            lineList = self.concordance_table.hash_table[currentIndex][1]
            # print(lineList) #PRINT DEBUG
            lineList = map(str, lineList) #convert the list of ints to str
            lineString = ' '.join(lineList) #create a string of the line numbers
            # print(word) #PRINT DEBUG
            # print(lineString) #PRINT DEBUG
            writeString = word + ': ' + lineString #create final string that is written into the file
            # print(writeString) #PRINT DEBUG
            file.write(writeString + '\n')
        file.close()




