import os
from ordered_list import *
from huffman_bit_writer import *
from huffman_bit_reader import *

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right
        
    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        return (type(other) == HuffmanNode and 
        self.char == other.char and
        self.freq == other.freq)
        
    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if self.freq == other.freq:
            return type(other) and (self.char < other.char)
        return type(other) and (self.freq < other.freq)
    

def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file'''
    #open the txt file
    file = open(filename, 'r')
    #create a frequency list with 256 zeros
    freqList = [0 for i in range(256)]
    while True:
        c = file.read(1)
        #reaches end of file
        if not c:
            break
        #iterate through the file and add 1 to every count
        if ord(c) < 256:
            freqList[ord(c)] += 1
    file.close()
    return freqList


def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''
    #creating ordered list of Huffman nodes from char_freq
    orderedList = OrderedList()
    #iterate through all values of char_freq
    for i in range(256):
        #if it is not a 0 count
        if char_freq[i] != 0:
            #create a Huffman Node and append to the list
            orderedList.add(HuffmanNode(i, char_freq[i]))
    
    while orderedList.size() != 1:
        #make combined node
        node1 = orderedList.pop(0)
        node2 = orderedList.pop(0)

        #comparing which node has the lower ASCII value
        if node1.char > node2.char:
            newChar = node2.char
        elif node1.char < node2.char:
            newChar = node1.char
        #set new frequency to the sum of children freqs
        newFreq = node1.freq + node2.freq

        newNode = HuffmanNode(newChar, newFreq)
        #set left and right children
        newNode.left = node1
        newNode.right = node2

        #append the combined node to the list
        orderedList.add(newNode)
    return orderedList.pop(0)


def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    #create a string that will store Huffman code
    codeString = ''
    #create an array of empty strings that will be filled with Huffman codes
    codeList = ['' for i in range(256)]
    return create_code_helper(node, codeList, codeString)

def create_code_helper(node, codelist, code):
    '''a helper function for create_code, basically takes in a root node, empty list, and empty code and returns
    a list with code'''
    #base case - when there are no children and it is a leaf
    if (node.left == None) and (node.right == None):
        codelist[node.char] = code
        return codelist

    #iteration - checking each side of the node
    #if the left child is not None
    if node.left != None:
        create_code_helper(node.left, codelist, code + '0')
    #if the right child is not None
    if node.right != None:
        create_code_helper(node.right, codelist, code + '1')
    return codelist
        

def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    #create header empty string
    header = []
    for i in range(256):
        #if it is not a 0 count
        if freqs[i] != 0:
            #add the index and freq to the header
            header.append(str(i))
            header.append(str(freqs[i]))
    return (" ".join(header))


def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''
    #empty file catch
    try:
        if os.stat(in_file).st_size == 0:
            file = open(out_file, 'w')
            file.close()
            newfilename = out_file[:(len(out_file) - 4)] + "_compressed.txt"
            file = HuffmanBitWriter(newfilename)
            file.close()
            return
    except FileNotFoundError:
        raise FileNotFoundError()

    #prep work
    freqList = cnt_freq(in_file)
    rootNode = create_huff_tree(freqList)
    codeList = create_code(rootNode)
    header = create_header(freqList)

    #reading the in_file and making output str
    outputList = []
    file = open(in_file, 'r')
    while True:
        c = file.read(1)
        #reaches end of file
        if not c:
            break
        #iterate through the file and add huffman code to output string
        if ord(c) < 256:
            outputList.append(codeList[ord(c)])
    file.close()

    #join outputlist to make string for uncompressed
    outputString_uncompressed = header + '\n' + ''.join(outputList)

    #editing over out_file
    file = open(out_file, 'w')
    file.write(outputString_uncompressed)
    file.close()

    newfilename = out_file[:(len(out_file) - 4)] + "_compressed.txt"

    #join outputlist to make string for compressed
    outputString_compressed = ''.join(outputList)

    #writing new compressed file
    file = HuffmanBitWriter(newfilename)
    file.write_str(header)
    file.write_str("\n")
    file.write_code(outputString_compressed)
    file.close()


def huffman_decode(encoded_file, decode_file):
    '''encoded_file (.txt) -> decode_file (.txt)
    Reads an encoded text file, encoded_file, and writes the decoded text into an output text file, 
    decode_file, using the Huffman Tree produced by using the header information.  
    If the encoded_file does not exist, your program should raise the FileNotFoundError exception. 
    If the specified output file already exists, its old contents will be overwritten.  
    '''
    #empty file catch
    try:
        if os.stat(encoded_file).st_size == 0:
            file = open(decode_file, 'w')
            file.close()
            return
    except FileNotFoundError:
        raise FileNotFoundError() 

    #reading the encoded_file
    file = open(encoded_file, 'rb')
    header = file.readline()
    file.close()

    #creating the freqList from bit header
    freqList = parse_header(header)
    charsNum = sum(freqList)

    #creating a HuffTree, returning a rootNode
    rootNode = create_huff_tree(freqList)

    try:
        decodedString = tree_reader(encoded_file, charsNum, rootNode)
    except:
        for i in range(len(freqList)):
            if freqList[i] != 0:
                freq = freqList[i]
                decodedString = chr(i) * freq
                break

    file = open(decode_file, 'w')
    file.write(decodedString)
    file.close()


def parse_header(header_string):
    '''header_string (bytes) -> freqList (list)
    takes a string input parameter (the first line of the input file)
    and returns a list of frequencies
    '''
    #decoding and making a string without newline
    tempString = header_string.decode("utf-8")
    simpleString = tempString.replace("\n", "")

    #making headerList and removing all empty spaces
    headerList = list(simpleString.split(" "))
    indexList = []
    indexfreqList = []

    #seperate header list into two lists: index and index freqs
    for i in range(len(headerList)):
        if (i % 2) == 0:
            indexList.append(int(headerList[i]))
        else:
            indexfreqList.append(int(headerList[i]))

    #create a frequency list with 256 zeros
    freqList = [0 for i in range(256)]

    for i in range(len(indexList)):
        freqList[indexList[i]] = indexfreqList[i]

    return freqList


def tree_reader(encoded_file, num_of_chars, rootNode):
    '''rootNode (node) -> finalString (str)
    takes in a huffman tree root node, encoded_file, and number of characters
    and creates a string with its contents
    '''
    stringList = []
    charsCount = 0
    currentNode = rootNode
    file = HuffmanBitReader(encoded_file)
    file.read_str()

    #while character count is less than number of chars
    while charsCount < num_of_chars:
        res = file.read_bit()
        #if digit is 0 (False) go left, if 1 (True) go right
        if res == False:
            currentNode = currentNode.left
        elif res == True:
            currentNode = currentNode.right

        #reaches a leaf node
        if currentNode.left == None and currentNode.right == None:
            stringList.append(chr(currentNode.char))
            #set current node back to root
            currentNode = rootNode
            #add one to character count
            charsCount += 1

    finalString = ''.join(stringList)
    file.close()
    return finalString

print(create_header([97, 16, 98, 7, 99, 51, 100, 19, 101, 8]))