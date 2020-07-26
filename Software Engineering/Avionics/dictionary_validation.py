#! /usr/bin/env python

from __future__ import print_function, division
import sys


def default_handler(word):
    label = word & 0xff
    sdi = (word & 0xc00000) >> 22
    general_data = (word & 0x3FFFFC)  >> 3
    ssm = (word & 0x6) >> 1
    parity = (word & 0x1) >> 0        
    dict = {
        "label" : "0o{0:03o}".format(label),
        "sdi": bin(sdi),
        "ssm": bin(ssm),
        "parity": bin(parity),
        "fields": {
            "general_data": hex(general_data)
            }
        }

    return dict

def label_102_to_readable(word):
    sdi = (word & 0xc00000) >> 22
    altitude_select_knob = (word & 0x200000)  >> 21
    spare12 = word & (0x100000) >> 20
    data13_28 = (word & 0xffff0) >> 4
    sign_bit = (word & 0x8) >> 3
    ssm = (word & 0x6) >> 1
    parity = (word & 0x1) >> 0        

    dict = {"fields": {}}
    dict["label"] = "0o{0:03o}".format(0o102)
    dict["sdi"] = bin(sdi)
    dict["fields"]["altitude_select_knob"] = bin(altitude_select_knob)
    dict["fields"]["spare12"] = bin(spare12)
    dict["fields"]["data13_28"] = bin(data13_28)
    dict["fields"]["sign_bit"] = bin(sign_bit)
    dict["ssm"] = bin(ssm)
    dict["parity"] = bin(parity)
    
    return dict

def arinc_to_readable(word):
    
    label_to_handler = {
        0o102: label_102_to_readable,
    }

    label = word & 0xff
    handler = label_to_handler.get(label, default_handler)
    return handler(word)


def main():
    args = sys.argv[1:]
    for arg in args:
        print(arg, arinc_to_readable(int(arg, 0)))
    return 0

if __name__ == "__main__":
    sys.exit(main())

