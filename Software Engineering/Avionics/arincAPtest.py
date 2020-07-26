#! /usr/bin/env python
import unittest
from arincAPsend import construct_data_words
# [] -> []
# [""] -> [""]
# ["", "", ""] -> ["", "", ""]
class ArincAPTest(unittest.TestCase):
    def test_0(self):
        input = ["0x0"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x00\x00"]
        self.assertEquals(expected_output, output)    

    def test_1(self):
        input = ["0xFFFFFFFF"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\xff\xff\xff\xff"]       
        self.assertEquals(expected_output, output)
        
    def test_case1(self):
        input = ["0x1"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x00\x01"]       
        self.assertEquals(expected_output, output)
        
    def test_case2(self):
        input = ["0x00000002"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x00\x02"]       
        self.assertEquals(expected_output, output)
        
    def test_case3(self):
        input = ["0x4"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x00\x04"]       
        self.assertEquals(expected_output, output)
        
    def test_case4(self):
        input = ["0x00000008"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x00\x08"]       
        self.assertEquals(expected_output, output)
        
    def test_case5(self):
        input = ["0x10"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x00\x10"]       
        self.assertEquals(expected_output, output)
        
    def test_case6(self):
        input = ["0x00000020"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x00\x20"]       
        self.assertEquals(expected_output, output)
        
    def test_case7(self):
        input = ["0x40"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x00\x40"]       
        self.assertEquals(expected_output, output)
        
    def test_case8(self):
        input = ["0x00000080"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x00\x80"]       
        self.assertEquals(expected_output, output)
        
    def test_case9(self):
        input = ["0x100"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x08\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case10(self):
        input = ["0x00000200"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x10\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case11(self):
        input = ["0x400"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x20\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case12(self):
        input = ["0x00000800"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x40\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case13(self):
        input = ["0x1000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x80\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case14(self):
        input = ["0x00002000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x01\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case15(self):
        input = ["0x4000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x02\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case16(self):
        input = ["0x00008000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x04\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case17(self):
        input = ["0x10000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x08\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case18(self):
        input = ["0x00020000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x10\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case19(self):
        input = ["0x40000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x20\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case20(self):
        input = ["0x00080000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x40\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case21(self):
        input = ["0x100000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x80\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case22(self):
        input = ["0x00200000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x01\x00\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case23(self):
        input = ["0x400000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x02\x00\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case24(self):
        input = ["0x00800000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x04\x00\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case25(self):
        input = ["0x1000000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x08\x00\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case26(self):
        input = ["0x2000000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x10\x00\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case27(self):
        input = ["0x04000000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x20\x00\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case28(self):
        input = ["0x8000000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x40\x00\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case29(self):
        input = ["0x10000000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x80\x00\x00\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case30(self):
        input = ["0x20000000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x02\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case31(self):
        input = ["0x40000000"]
        output = construct_data_words(input)        
        expected_output = ["\x0f\x00\x00\x00\x04\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_case32(self):
        input = ["0x80000000"]
        output = construct_data_words(input)       
        expected_output = ["\x0f\x00\x00\x00\x01\x00"]       
        self.assertEquals(expected_output, output)
        
    def test_empty(self):
        input = []
        output = construct_data_words(input)       
        expected_output = []       
        self.assertEquals(expected_output, output)
        
    def test_multiple(self):
        input = ["0x80000000",
                 "0x40000000",
                 "0x20000000",
                 "0x80000000",
                 "0x40000000",
                 "0x20000000",
                 "0x80000000",
                 "0x40000000",
                 "0x20000000",
                 "0x80000000",
                 "0x40000000",
                 "0x20000000"]
        output = construct_data_words(input)       
        expected_output = ["\x0f\x00\x00\x00\x01\x00", 
                           "\x0f\x00\x00\x00\x04\x00",
                           "\x0f\x00\x00\x00\x02\x00",
                           "\x0f\x00\x00\x00\x01\x00", 
                           "\x0f\x00\x00\x00\x04\x00",
                           "\x0f\x00\x00\x00\x02\x00",
                           "\x0f\x00\x00\x00\x01\x00", 
                           "\x0f\x00\x00\x00\x04\x00",
                           "\x0f\x00\x00\x00\x02\x00",
                           "\x0f\x00\x00\x00\x01\x00", 
                           "\x0f\x00\x00\x00\x04\x00",
                           "\x0f\x00\x00\x00\x02\x00"]       
        self.assertEquals(expected_output, output)

if __name__ == "__main__":
    unittest.main()
