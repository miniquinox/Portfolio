#! /usr/bin/env python

from __future__ import print_function, division
import sys
import json
import struct
import socket
import time
import threading
from optparse import OptionParser
import os.path

NUM_ARGS = 2
FIFTY_MS = 50/1000.0
ARINC429_RX_5 = 15
TASK_INTERVAL = FIFTY_MS * 10

Dict = None
Any = None
IPPort = int
Socket = socket.socket
SerializedIopToMapArinc = bytes

def words_from_json(path):
    with open(path) as f:
        json_string = f.read()
    try:
        parsed_json = json.loads(json_string)
        # formatted_json = json.dumps(parsed_json, indent=4, sort_keys=True)
        # with open("json_file.json","w") as f:
        #     f.write(formatted_json)
    except Exception as e:
        print(repr(e))
        raise

    return parsed_json


def arinc_normal_to_iop(int32):
    """arinc normal to iop conversion"""
    retval = ((int32 & 0x80000000) >> 23)
    retval |= ((int32 & 0x60000000) >> 20)
    retval |= ((int32 & 0x1FFFFF00) << 3)
    retval |= (int32 & 0x000000FF)
    return retval



def arinc_packet(word, label):
    pad = 0
    return struct.pack("!BBI", label, pad, arinc_normal_to_iop(word))


def socket_from_ip_port(ip_port):
    # type: (IPPort) -> Socket
    return None


def send_packets(sock, host, port, packets):
    """Sends list of packets over the sock to the (host, port)"""
    for packet in packets:
        sock.sendto(packet, (host, port))


def setup_command_line():
    """Setup and create the OptionParser."""
    usage = """usage: %prog host[:port] [testcondition]

    Sends ARINC packetes specified by json_file to host:port.
    """

    parser = OptionParser(usage=usage)
    return parser


def is_int(string):
    """Determines whether the input string is formated like an int or not"""
    try:
        int(string)
        return True
    except ValueError:
        return False


def check_inputs(options, args):

    if len(args) < NUM_ARGS:
        return "Invalid number of arguments; need {0}".format(NUM_ARGS)

    host = args[0]
    host_port = host.split(":")
    if len(host_port) > 1 and not is_int(host_port[1]):
        return "Port must be valid integer."

    return None


def decode_host(host, default_port):
    split_host = host.split(":")
    if len(split_host) > 1 and is_int(split_host[1]):
        return (split_host[0], int(split_host[1]))
    else:
        return (host, default_port)

def xmit_loop(output_words,sock,host,port,stop):
    while True:
        send_packets(sock, host, port, output_words)
        time.sleep(TASK_INTERVAL)
        if stop():
            break

def construct_data_words(words):
    # type: (List[str]) -> List[SerializedIopToMapArinc]
    """Takes a hex string formatted raw arinc word, moves around bits per the 
    IOP to MAP ICD, converts to big endian, packs into byte
    array per sim tool ICD with arinc port set to RX5"""
    return [arinc_packet(int(word, 16), ARINC429_RX_5) for word in words]

def main():
    testcondition = '1'
    parser = setup_command_line()
    options, args = parser.parse_args()
    err_msg = check_inputs(options, args)
    if err_msg:
        parser.error(err_msg)
    json_path = args[1] #'A429_AP_testconditions.json'
    with open(json_path) as f:
        json_string = f.read()

    parsed_testconditions = json.loads(json_string)
    #finally:
    host_port = args[0]
    host, port = decode_host(host_port, 12345)
    sock = socket.socket(type=socket.SOCK_DGRAM)
    if len(args) == 3:
       testcondition = args[2]


    while True:
        print("TestCondition  ",testcondition)
        words = parsed_testconditions[testcondition]
        for word in words:
            print("    ",word)
        output_words = construct_data_words(words)
        try:
            stop_xmit = False
            t = threading.Thread(target=xmit_loop, args=(output_words,sock,host,port,lambda: stop_xmit))
            t.start()
            testcondition = raw_input('testcondition? ')

            stop_xmit = True
            t.join()
            if testcondition == "":
                return
        except KeyboardInterrupt:
            print("Shutting down")
    sock.close()
    print("")
    print("Shutting down")



if __name__ == '__main__':
    main()
