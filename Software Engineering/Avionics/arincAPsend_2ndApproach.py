#! /usr/bin/env python

from __future__ import print_function, division
import json
import struct
import socket
import time
from optparse import OptionParser
import os.path
import logging


NUM_ARGS = 2
FIFTY_MS = 50/1000.0
ARINC429_RX_5 = 15
TASK_INTERVAL = FIFTY_MS * 10
DEFAULT_LISTEN_PORT = 8020
NETCTRL_OP_REQUEST_COMMAND = 10
PACKET_REPETITIONS = 5

DEFAULT_SIM_PORT = 12345
DEFAULT_EFD_PORT = 8550

Dict = None
Any = None
IPPort = int
Socket = socket.socket
COMMAND = "netiop"


def arinc_label_ssm(label, sdi, ssm, parity):
    """Setup ARINC label"""
    # type: (int, int, int, int) -> int
    if parity:
        parity_bit = 0x80000000
    else:
        parity_bit = 0

    return (label & 0xFF | ((sdi & 0b11) << 8) |
            parity_bit | ((ssm & 0x3) << 29))


def discrete_ssm_string_to_bits(ssm):
    # type: (str) -> int
    ssm_lower = ssm.lower()
    # In python, 0b denotes binary, 0o denotes octal, 0x denotes hexadecimal
    mapping = {
        "failure": 0b11,
        "ncd": 0b01,
        "test": 0b10,
        "normal": 0b00
    }
    assert ssm_lower in mapping
    return mapping[ssm_lower]


def binary_ssm_string_to_bits(ssm):
    # type: (str) -> int
    ssm_lower = ssm.lower()
    # In python, 0b denotes binary, 0o denotes octal, 0x denotes hexadecimal
    mapping = {
        "failure": 0b00,
        "ncd": 0b01,
        "test": 0b10,
        "normal": 0b11
    }
    assert ssm_lower in mapping
    return mapping[ssm_lower]


def arinc_102(word):
    # type: (Dict[Any]) -> int
    assert word["label"] == 0o102
    # This function assumes all the subfields are ints and do not exceed the
    # number of bits the field allows
    base_word = arinc_label_ssm(word["label"], word["sdi"],
                                binary_ssm_string_to_bits(word["ssm"]),
                                word["parity"])

    arinc_word = (base_word |
                  word["fields"]["altitude_select_knob"] << 10 |
                  word["fields"]["spare12"] << 11 |
                  word["fields"]["data"])
    return arinc_word


def arinc_103(word):
    # type: (Dict[Any]) -> int
    assert word["label"] == 0o103
    # This function assumes all the subfields are ints and do not exceed the
    # number of bits the field allows
    base_word = arinc_label_ssm(word["label"], word["sdi"],
                                binary_ssm_string_to_bits(word["ssm"]),
                                word["parity"])

    arinc_word = (base_word |
                  word["fields"]["airspeed_select_knob"] << 10 |
                  word["fields"]["spare12_17"] << 11 |
                  word["fields"]["data"])
    return arinc_word


def arinc_104(word):
    # type: (Dict[Any]) -> int
    assert word["label"] == 0o104
    # This function assumes all the subfields are ints and do not exceed the
    # number of bits the field allows
    base_word = arinc_label_ssm(word["label"], word["sdi"],
                                binary_ssm_string_to_bits(word["ssm"]),
                                word["parity"])
    arinc_word = (base_word |
                  word["fields"]["vertspeed_select_knob"] << 10 |
                  word["fields"]["spare12_14"] << 11 |
                  word["fields"]["data"])
    return arinc_word


def arinc_140(word):
    # type: (Dict[Any]) -> int
    assert word["label"] == 0o140
    # This function assumes all the subfields are ints and do not exceed the
    # number of bits the field allows
    base_word = arinc_label_ssm(word["label"], word["sdi"],
                                binary_ssm_string_to_bits(word["ssm"]),
                                word["parity"])

    arinc_word = (base_word |
                  word["fields"]["spare11_14"] << 10 |
                  word["fields"]["data"])
    return arinc_word


def arinc_141(word):
    # type: (Dict[Any]) -> int
    assert word["label"] == 0o141
    # This function assumes all the subfields are ints and do not exceed the
    # number of bits the field allows
    base_word = arinc_label_ssm(word["label"], word["sdi"],
                                binary_ssm_string_to_bits(word["ssm"]),
                                word["parity"])

    arinc_word = (base_word |
                  word["fields"]["spare11_16"] << 10 |
                  word["fields"]["data"])
    return arinc_word


def arinc_273(word):
    # type: (Dict[Any]) -> int
    assert word["label"] == 0o273
    # This function assumes all the subfields are ints and do not exceed the
    # number of bits the field allows
    base_word = arinc_label_ssm(word["label"], word["sdi"],
                                discrete_ssm_string_to_bits(word["ssm"]),
                                word["parity"])

    arinc_word = (base_word |
                  word["fields"]["spare11"] << 10 |
                  word["fields"]["alt_armed"] << 11 |
                  word["fields"]["nav_armed"] << 12 |
                  word["fields"]["lnav_armed"] << 13 |
                  word["fields"]["vnav_armed"] << 14 |
                  word["fields"]["bc_armed"] << 15 |
                  word["fields"]["loc_armed"] << 16 |
                  word["fields"]["apr_armed"] << 17 |
                  word["fields"]["vgp_armed"] << 18 |
                  word["fields"]["spare20_21"] << 19 |
                  word["fields"]["gs_armed"] << 21 |
                  word["fields"]["vor_armed"] << 22 |
                  word["fields"]["spare24_29"] << 23)
    return arinc_word


def arinc_274(word):
    # type: (Dict[Any]) -> int
    assert word["label"] == 0o274
    # This function assumes all the subfields are ints and do not exceed the
    # number of bits the field allows
    base_word = arinc_label_ssm(word["label"], word["sdi"],
                                discrete_ssm_string_to_bits(word["ssm"]),
                                word["parity"])

    arinc_word = (base_word |
                  word["fields"]["ias_mode"] << 10 |
                  word["fields"]["vnav_mode"] << 11 |
                  word["fields"]["alt_hold_mode"] << 12 |
                  word["fields"]["vs_mode"] << 13 |
                  word["fields"]["toga_around_mode"] << 14 |
                  word["fields"]["ga_mode"] << 15 |
                  word["fields"]["vgp_active"] << 16 |
                  word["fields"]["envelope_protect"] << 17 |
                  word["fields"]["gs_mode"] << 18 |
                  word["fields"]["gp_mode"] << 19 |
                  word["fields"]["vpth_mode"] << 20 |
                  word["fields"]["level_mode"] << 21 |
                  word["fields"]["spare23"] << 22 |
                  word["fields"]["cws_engaged"] << 24 |
                  word["fields"]["spare26"] << 25 |
                  word["fields"]["flash_vert_mode"] << 26 |
                  word["fields"]["pitch_mode"] << 27 |
                  word["fields"]["capture_sub_mode"] << 28)
    return arinc_word


def arinc_275(word):
    # type: (Dict[Any]) -> int
    assert word["label"] == 0o275
    # This function assumes all the subfields are ints and do not exceed the
    # number of bits the field allows
    base_word = arinc_label_ssm(word["label"], word["sdi"],
                                discrete_ssm_string_to_bits(word["ssm"]),
                                word["parity"])

    arinc_word = (base_word |
                  word["fields"]["lnav_sub_mode"] << 10 |
                  word["fields"]["hdg_mode"] << 11 |
                  word["fields"]["half_bank_active"] << 12 |
                  word["fields"]["bc_sub_mode"] << 13 |
                  word["fields"]["loc_sub_mode"] << 14 |
                  word["fields"]["spare16"] << 15 |
                  word["fields"]["ga_mode"] << 16 |
                  word["fields"]["straight_and_level"] << 17 |
                  word["fields"]["spare19"] << 18 |
                  word["fields"]["roll_mode"] << 19 |
                  word["fields"]["capture_sub_mode"] << 20 |
                  word["fields"]["vor_sub_mode"] << 21 |
                  word["fields"]["track_sub_mode"] << 22 |
                  word["fields"]["level_mode"] << 23 |
                  word["fields"]["intercept_sub_mode"] << 24 |
                  word["fields"]["nav_mode"] << 25 |
                  word["fields"]["apr_mode"] << 26 |
                  word["fields"]["flash_ap_lateral_mode"] << 27 |
                  word["fields"]["tcs_mode"] << 28)
    return arinc_word


def arinc_300(word):
    # type: (Dict[Any]) -> int
    assert word["label"] == 0o300
    # This function assumes all the subfields are ints and do not exceed the
    # number of bits the field allows
    base_word = arinc_label_ssm(word["label"], word["sdi"],
                                discrete_ssm_string_to_bits(word["ssm"]),
                                word["parity"])

    arinc_word = (base_word |
                  word["fields"]["yaw_trim_status"] << 10 |
                  word["fields"]["roll_trim_status"] << 13 |
                  word["fields"]["ap_engaged"] << 16 |
                  word["fields"]["fd_engaged"] << 17 |
                  word["fields"]["yd_selected"] << 18 |
                  word["fields"]["ap_status"] << 19 |
                  word["fields"]["lateral_arm_status"] << 21 |
                  word["fields"]["lateral_mode_status"] << 22 |
                  word["fields"]["vertical_arm_status"] << 23 |
                  word["fields"]["gs_arm_status"] << 24 |
                  word["fields"]["vert_mode_status"] << 25 |
                  word["fields"]["pitch_trim_status"] << 26)
    return arinc_word


def arinc_301(word):
    # type: (Dict[Any]) -> int
    assert word["label"] == 0o301
    # This function assumes all the subfields are ints and do not exceed the
    # number of bits the field allows
    base_word = arinc_label_ssm(word["label"], word["sdi"],
                                discrete_ssm_string_to_bits(word["ssm"]),
                                word["parity"])

    arinc_word = (base_word |
                  word["fields"]["underspeed"] << 10 |
                  word["fields"]["overspeed"] << 11 |
                  word["fields"]["speed_protect"] << 12 |
                  word["fields"]["bank_limit"] << 13 |
                  word["fields"]["servo_limit"] << 14 |
                  word["fields"]["servo_fail"] << 15 |
                  word["fields"]["trimming"] << 16 |
                  word["fields"]["no_pfd_comm"] << 17 |
                  word["fields"]["spare19_27"] << 18 |
                  word["fields"]["ap_inop"] << 27 |
                  word["fields"]["ap_disconnect"] << 28)
    return arinc_word


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


def calculation(data, resolution, bit_length):
    # type: (Dict[data]) -> int
    # calculation of data field by resolution
    y = int(round(data*(1/resolution)))

    arinc_output_word = (y << (32 - (bit_length + 3))) & 0x1FFFFFFF

    return arinc_output_word


def serialize_word(word):
    label_oct = None
    if "label" in word:
        label = word["label"]
        label_oct = int(str(label), 8)
        word["label"] = label_oct
        test = word

    if label_oct == 0o140:
        data = calculation(test["fields"]["data"], 180/4096, 13)
        test["fields"]["data"] = data
        int32 = arinc_140(test)
    elif label_oct == 0o141:
        data = calculation(test["fields"]["data"], 180/4096, 13)
        test["fields"]["data"] = data
        int32 = arinc_141(test)
    elif label_oct == 0o273:
        int32 = arinc_273(test)
    elif label_oct == 0o274:
        int32 = arinc_274(test)
    elif label_oct == 0o275:
        int32 = arinc_275(test)
    elif label_oct == 0o300:
        int32 = arinc_300(test)
    elif label_oct == 0o301:
        int32 = arinc_301(test)
    elif label_oct == 0o104:
        data = calculation(test["fields"]["data"], 1, 15)
        test["fields"]["data"] = data
        int32 = arinc_104(test)
    elif label_oct == 0o103:
        data = calculation(test["fields"]["data"], 0.25, 12)
        test["fields"]["data"] = data
        int32 = arinc_103(test)
    elif label_oct == 0o102:
        data = calculation(test["fields"]["data"], 1, 17)
        test["fields"]["data"] = data
        int32 = arinc_102(test)
    elif "word" in word and label_oct is None:
        int32 = word["word"] & 0xffffffff
    else:
        assert False

    return int32


def arinc_packet(word, label):
    pad = 0
    return struct.pack("!BBI", label, pad, arinc_normal_to_iop(word))


def send_packets(sock, host, port, packets):
    """Sends list of packets over the sock to the (host, port)"""
    for packet in packets:
        sock.sendto(packet, (host, port))


def setup_command_line():
    """Setup and create the OptionParser."""
    usage = """usage: %prog host[:port] json_file [options]

    Sends ARINC packetes specified by json_file to host:port.
    Run with --help option for more info.
    """

    parser = OptionParser(usage=usage)

    help_msg = "Sends ARINC packet using netiop build, [default:%default]"
    parser.add_option("--netiop", action="store_true", dest="netiop",
                      help=help_msg)

    help_msg = "EFD listen port. Only relevant with netiop [default:%default]"
    parser.add_option("--lport", action="store", dest="listen_port", type=int,
                      help=help_msg, default=DEFAULT_LISTEN_PORT)
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

    json_path = args[1]
    if not os.path.isfile(json_path):
        "{0} is not a valid file".format(json_path)

    return None


def decode_host(host, default_port):
    split_host = host.split(":")
    if len(split_host) > 1 and is_int(split_host[1]):
        return (split_host[0], int(split_host[1]))
    else:
        return (host, default_port)


def netiop_command(lport):
    """Create netiop command for for 32-bit lport"""
    str_lport = str(lport)
    # this is good network byte ordered
    payload_format = "!H{0}sx{1}sx".format(len(COMMAND),
                                           len(str_lport))
    logging.debug("lport: %d", lport)
    return struct.pack(payload_format, NETCTRL_OP_REQUEST_COMMAND,
                       (COMMAND), str_lport)


def shutdown_command():
    """Create netiop command w/o port to shutdown"""
    return struct.pack("!H{0}sx".format(len(COMMAND)),
                       NETCTRL_OP_REQUEST_COMMAND,
                       (COMMAND))


def send_netiop_start(sock, listen_port, host, port):
    """Send netiop start command socket"""
    init_cmd = netiop_command(listen_port)
    logging.debug("init_cmd: %s", repr(init_cmd))
    logging.debug("sending netiop")
    for _ in xrange(0, PACKET_REPETITIONS):
        sock.sendto(init_cmd, (host, port))
        time.sleep(FIFTY_MS)

def foo(words):
    # words = words_from_json(json_path)    
    return [arinc_packet(serialize_word(word), ARINC429_RX_5)
                    for word in words]

def main():
    parser = setup_command_line()
    options, args = parser.parse_args()
    err_msg = check_inputs(options, args)

    if err_msg:
        parser.error(err_msg)

    host_port = args[0]
    json_path = args[1]

    default_port = DEFAULT_SIM_PORT if not options.netiop else DEFAULT_EFD_PORT

    host, port = decode_host(host_port, default_port)

    send_port = port if not options.netiop else options.listen_port

    words = words_from_json(json_path)
    output_words = foo(words)  

    sock = socket.socket(type=socket.SOCK_DGRAM)

    try:
        if options.netiop:
            send_netiop_start(sock, options.listen_port, host, port)
        while True:
            send_packets(sock, host, send_port, output_words)
            time.sleep(TASK_INTERVAL)
    except KeyboardInterrupt:
        print("")
        print("Shutting down")
        if options.netiop:
            close_cmd = shutdown_command()
            for _ in xrange(0, PACKET_REPETITIONS):
                sock.sendto(close_cmd, (host, port))
                time.sleep(FIFTY_MS)
    finally:
        sock.close()
        print("Done")


if __name__ == '__main__':
    main()
