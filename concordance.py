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
        try:
            i = open(filename, "r")
            i.close()
        except:
            raise FileNotFoundError
        
        i = open(filename, "r")

        self.stop_table = HashTable(191)
        stopWords = i.readlines()
        #rint(stopWords)
        '''this gets all the words in stop table and puts it into the stop table hash'''
        count = 1
        for j in stopWords:
            self.stop_table.insert(j.rstrip(), count)
            count += 1
        i.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        (The stop words hash table could possibly be None.)
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            i = open(filename, "r")
            i.close()
        except:
            raise FileNotFoundError
        
        myFile = open(filename, "r")
        self.concordance_table = HashTable(191)
        #duplicates = HashTable(191)

        #need to filter out punctuation, numbers and words in stop words hash table
        content = myFile.read() #process input one line at a time
        contentList = content.split("\n")
        myFile.close()
        for i in range(len(contentList)): #for each line
            for j in contentList[i]: #for each char in each line
                if j == "'":
                    contentList[i] = contentList[i].replace(j, "")
                elif j in string.punctuation:
                    contentList[i] = contentList[i].replace(j, " ")

            token = contentList[i].split()
            for item in token:
                if item.isalpha() and not self.stop_table.in_table(item.lower()): # means its a word
                    #add it to duplicate and concordance if it's not in duplicataes
                    if not self.concordance_table.in_table(item.lower()):
                        #duplicates.insert(item.lower(), [i + 1])
                        self.concordance_table.insert(item.lower(), [i + 1])
                    else: #its in duplicates if it goes here
                        #need to replace the value with a list of the new value and the old value
                        #print(self.concordance_table.get_all_keys())
                        #print(self.concordance_table.hash)
                        index = self.concordance_table.get_index(item.lower())
                        #value = self.concordance_table.hash[index]
                        if (i + 1) not in self.concordance_table.hash[index][1]:
                            self.concordance_table.hash[index][1].append(i + 1)
        #myFile.close()


    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        myKeys = self.concordance_table.get_all_keys()
        myKeys.sort()
        f = open(filename, "w")
        for key in myKeys:
            index = self.concordance_table.get_index(key)
            f.write(key + ": ")
            for line in self.concordance_table.hash[index][1]:
                f.write(str(line) + " ")
            f.write("\n")
        
        f.close()

