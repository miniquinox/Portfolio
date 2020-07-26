import unittest
from arincAPsend import foo
import struct
# import testdata
from struct import *

BYTE1 = 0b00001111
BYTE2 = 0b00000000

class ArincAPTest(unittest.TestCase):
    def test_zeros(self):
        label_273 = {
        "label": 273, #10111011
        "ssm": "normal", 
        "fields": { 
            "spare11": 0,
            "alt_armed": 0,
            "nav_armed": 0,
            "lnav_armed": 0,
            "vnav_armed": 0,
            "bc_armed": 0,
            "loc_armed": 0,
            "apr_armed": 0,
            "vgp_armed": 0, 
            "spare20_21": 0, 
            "gs_armed": 0,
            "vor_armed": 0,
            "spare24_29": 0 
        },
        "sdi": 0,
        "parity": 0 
        }       
        input = [label_273]
        #input = ["0xBB", "0xcd", "0xab23"]
        output = foo(input)
        word = 0b00000000000000000000000010111011
        var = [struct.pack("!BBI", BYTE1, BYTE2, word)]
        expected_output = var
        print(str(expected_output))
        print(output)
        self.assertEqual(expected_output, output)

if __name__ == '__main__':
    unittest.main()
