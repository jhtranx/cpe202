import unittest
import filecmp
import subprocess
from ordered_list import *
from huffman import *


class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

        freqlist	= cnt_freq("empty_file.txt")
        anslist = [0,0,0,0,0,0,0] 
        self.assertListEqual(freqlist[97:104], anslist)

        
    def test_lt_and_eq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        ascii = 97
        lst = OrderedList()
        for freq in anslist:
            node = HuffmanNode(chr(ascii), freq)
            lst.add(node)
            ascii += 1
        self.assertEqual(lst.index(HuffmanNode('e', 0)), 0)
        self.assertEqual(lst.index(HuffmanNode('d', 16)), 6)
        self.assertEqual(lst.index(HuffmanNode('a', 2)), 2)
        self.assertFalse(HuffmanNode('a', 2) == None)
                    
                    
    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.char, 32)

        
    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

        
    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        # print(freqlist)
        hufftree = create_huff_tree(freqlist)
        # print(hufftree)
        # print(hufftree.right)
        codes = create_code(hufftree)
        # print(codes)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_create_code2(self):
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord(' ')], '00')
        self.assertEqual(codes[ord('a')], '11')
        self.assertEqual(codes[ord('b')], '01')
        self.assertEqual(codes[ord('c')], '101')
        self.assertEqual(codes[ord('d')], '100')
        
    
    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file1_out_compressed.txt file1_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file2_out_compressed.txt file2_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb declaration_out_compressed.txt declaration_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb multiline_out_compressed.txt multiline_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

        # huffman_encode("file_WAP.txt", "file_WAP_out.txt")
        # # capture errors by running 'diff' on your encoded file with a *known* solution file
        # err = subprocess.call("diff -wb file_WAP_out.txt file_WAP_soln.txt", shell = True)
        # self.assertEqual(err, 0)
        # err = subprocess.call("diff -wb file_WAP_out_compressed.txt file_WAP_compressed_soln.txt", shell = True)
        # self.assertEqual(err, 0)

    def test_02_textfile_edge(self):
        #empty file
        huffman_encode("empty_file.txt", "empty_file_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb empty_file_out.txt empty_file.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb empty_file_out_compressed.txt empty_file.txt", shell = True)
        self.assertEqual(err, 0)

        #file not found
        with self.assertRaises(FileNotFoundError):
            huffman_encode("notreal.txt", "notreal_out.txt")

        #repeat one letter
        huffman_encode("repeat.txt", "repeat_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb repeat_out.txt repeat_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb repeat_out_compressed.txt repeat_out.txt", shell = True)
        self.assertEqual(err, 0)

    def test_02_textfile_isleofdogs(self):
        #empty file
        huffman_encode("isleofdogs.txt", "isleofdogs_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb isleofdogs_out.txt isleofdogs_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb isleofdogs_out_compressed.txt isleofdogs_out_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

    

    #PROJECT 3B - DECODE TESTS
    def test_01a_test_file1_parse_header(self):
        f = open('file1_compressed_soln.txt', 'rb')
        header = f.readline()        
        f.close()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.compare_freq_counts(parse_header(header), expected)
        
    def test_01_test_file1_decode(self):
        huffman_decode("file1_compressed_soln.txt", "file1_decoded.txt")
        err = subprocess.call("diff -wb file1.txt file1_decoded.txt", shell = True)
        self.assertEqual(err, 0)

    def test_02_test_file2_decode(self):
        huffman_decode("file2_compressed_soln.txt", "file2_decoded.txt")
        err = subprocess.call("diff -wb file2.txt file2_decoded.txt", shell = True)
        self.assertEqual(err, 0)

    def test_03_test_empty_decode(self):
        huffman_decode("empty_file_out_compressed.txt", "empty_file_decoded.txt")
        err = subprocess.call("diff -wb empty_file.txt empty_file_decoded.txt", shell = True)
        self.assertEqual(err, 0)

    def test_04_test_filenotfound_decode(self):
        with self.assertRaises(FileNotFoundError):
            huffman_decode("notreal.txt", "notreal_decoded.txt")

    def test_05_test_repeat_decode(self):
        huffman_decode("repeat_out_compressed.txt", "repeat_decoded.txt")
        err = subprocess.call("diff -wb repeat.txt repeat_decoded.txt", shell = True)
        self.assertEqual(err, 0)

    # def test_06_test_WAP_decode(self):
    #     huffman_decode("file_WAP_compressed_soln.txt", "file_WAP_decoded.txt")
    #     err = subprocess.call("diff -wb file_WAP.txt file_WAP_decoded.txt", shell = True)
    #     self.assertEqual(err, 0)

    def compare_freq_counts(self, freq, exp):
        for i in range(256):
            stu = 'Frequency for ASCII ' + str(i) + ': ' + str(freq[i])
            ins = 'Frequency for ASCII ' + str(i) + ': ' + str(exp[i])
            self.assertEqual(stu, ins)

if __name__ == '__main__': 
   unittest.main()
