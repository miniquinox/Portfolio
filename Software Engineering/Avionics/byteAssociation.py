import unittest
import arincApSend
import testdata
import struct

BYTE1 = 00001111
BYTE2 = 00000000

def output_words()

    output_words = [arinc_packet(serialize_word(word), ARINC429_RX_5)
                    for word in words]

class ArincAPTest(unittest.unittest):
    def test_273_zeros(self):
        label_273 = testdata.label_273
        label_273["label"] = 273 #10111011
        label_273["sdi"] = 00        
        label_273["fields"]["spare11"] = 0
        label_273["fields"]["alt_armed"] = 0
        label_273["fields"]["nav_armed"] = 0
        label_273["fields"]["lnav_armed"] = 0
        label_273["fields"]["vnav_armed"] = 0
        label_273["fields"]["bc_armed"] = 0
        label_273["fields"]["loc_armed"] = 0
        label_273["fields"]["apr_armed"] = 0
        label_273["fields"]["vgp_armed"] = 0
        label_273["fields"]["spare20_21"] = 00
        label_273["fields"]["gs_armed"] = 0
        label_273["fields"]["vor_armed"] = 0
        label_273["fields"]["gp_armed"] = 0  
        label_273["fields"]["vpth_armed"] = 0
        label_273["fields"]["spare26_29"] = 0000        
        label_273["ssm"] = 00        
        label_273["parity"] = 0        
        input = [label_273]
        output = arincApSend.foo(input)
        word = [{10111011 00000000 00000000 00000000}]
        var = struct.pack('hh1', BYTE1, BYTE2, word)
        expected_output =  var
        print(var)
        self.assertEquals(expected_output, output)
      
    def test_273_ones(self):
        label_273 = testdata.label_273
        label_273["label"] = 273 #10111011
        label_273["sdi"] = 11        
        label_273["fields"]["spare11"] = 0
        label_273["fields"]["alt_armed"] = 1
        label_273["fields"]["nav_armed"] = 1
        label_273["fields"]["lnav_armed"] = 1
        label_273["fields"]["vnav_armed"] = 1
        label_273["fields"]["bc_armed"] = 1
        label_273["fields"]["loc_armed"] = 1
        label_273["fields"]["apr_armed"] = 1
        label_273["fields"]["vgp_armed"] = 1
        label_273["fields"]["spare20_21"] = 00
        label_273["fields"]["gs_armed"] = 1
        label_273["fields"]["vor_armed"] = 1
        label_273["fields"]["gp_armed"] = 1
        label_273["fields"]["vpth_armed"] = 1
        label_273["fields"]["spare26_29"] = 0000        
        label_273["ssm"] = 11
        label_273["parity"] = 1
        input = [label_273]
        output = arincApSend.foo(input)
        expected_output = [{000011110000000010111011110111111110011110000111}]
        self.assertEquals(expected_output, output)

    def test_273_mixed(self):
        label_273 = testdata.label_273
        label_273["label"] = 273 #10111011
        label_273["sdi"] = 01
        label_273["fields"]["spare11"] = 0
        label_273["fields"]["alt_armed"] = 1
        label_273["fields"]["nav_armed"] = 0
        label_273["fields"]["lnav_armed"] = 1
        label_273["fields"]["vnav_armed"] = 0
        label_273["fields"]["bc_armed"] = 1
        label_273["fields"]["loc_armed"] = 0
        label_273["fields"]["apr_armed"] = 1
        label_273["fields"]["vgp_armed"] = 0
        label_273["fields"]["spare20_21"] = 00
        label_273["fields"]["gs_armed"] = 1
        label_273["fields"]["vor_armed"] = 0
        label_273["fields"]["gp_armed"] = 1
        label_273["fields"]["vpth_armed"] = 0
        label_273["fields"]["spare26_29"] = 0000        
        label_273["ssm"] = 10
        label_273["parity"] = 1
        input = [label_273]
        output = arincApSend.foo(input)
        expected_output = [{000011110000000010111011010101010100010100000101}]
        self.assertEquals(expected_output, output)

    def test_273_mixed2(self):
        label_273 = testdata.label_273
        label_273["label"] = 273 #10111011
        label_273["sdi"] = 10
        label_273["fields"]["spare11"] = 0
        label_273["fields"]["alt_armed"] = 1
        label_273["fields"]["nav_armed"] = 0
        label_273["fields"]["lnav_armed"] = 1
        label_273["fields"]["vnav_armed"] = 0
        label_273["fields"]["bc_armed"] = 1
        label_273["fields"]["loc_armed"] = 0
        label_273["fields"]["apr_armed"] = 1
        label_273["fields"]["vgp_armed"] = 0
        label_273["fields"]["spare20_21"] = 00
        label_273["fields"]["gs_armed"] = 1
        label_273["fields"]["vor_armed"] = 0
        label_273["fields"]["gp_armed"] = 1
        label_273["fields"]["vpth_armed"] = 0
        label_273["fields"]["spare26_29"] = 0000        
        label_273["ssm"] = 01
        label_273["parity"] = 1
        input = [label_273]
        output = arincApSend.foo(input)
        expected_output = [{000011110000000010111011100101010100010100000011}]
        self.assertEquals(expected_output, output)










# def test_140(self)
    # data = calculation(test["fields"]["data"], 180/4096, 13)   
    # test["label"] = 1
    # test["ssm"] = 1
    # test["fields"]["spare11_14"] = 1
    # test["fields"]["data"] = 1
    # test["sdi"] = 1
    # test["parity"] = 1
    # int32 = arinc_140(test)

# def test_141(self)
    # data = calculation(test["fields"]["data"], 180/4096, 13)    
    # test["label"] = 1
    # test["ssm"] = 1
    # test["fields"]["spare11_16"] = 1
    # test["fields"]["data"] = 1
    # test["sdi"] = 1
    # test["parity"] = 1
    # int32 = arinc_141(test)

# def test_273(self)
    # test["label"] = 1
    # test["ssm"] = 1
    # test["fields"]["spare11"] = 1
    # test["fields"]["alt_armed"] = 1
    # test["fields"]["nav_armed"] = 1
    # test["fields"]["lnav_armed"] = 1
    # test["fields"]["vnav_armed"] = 1
    # test["fields"]["bc_armed"] = 1
    # test["fields"]["loc_armed"] = 1
    # test["fields"]["apr_armed"] = 1
    # test["fields"]["vgp_armed"] = 1
    # test["fields"]["spare20_21"] = 1
    # test["fields"]["gs_armed"] = 1
    # test["fields"]["vor_armed"] = 1
    # test["fields"]["spare24_29"] = 1    
    # test["sdi"] = 1
    # test["parity"] = 1
    # int32 = arinc_273(test)

# def test_274(self)
    # test["label"] = 1
    # test["ssm"] = 1
    # test["fields"]["ias_mode"] = 1
    # test["fields"]["vnav_mode"] = 1
    # test["fields"]["alt_hold_mode"] = 1
    # test["fields"]["vs_mode"] = 1
    # test["fields"]["toga_around_mode"] = 1
    # test["fields"]["ga_mode"] = 1
    # test["fields"]["vgp_active"] = 1
    # test["fields"]["envelope_protect"] = 1
    # test["fields"]["gs_mode"] = 1
    # test["fields"]["gp_mode"] = 1
    # test["fields"]["vpth_mode"] = 1
    # test["fields"]["level_mode"] = 1
    # test["fields"]["spare23"] = 1 
    # test["fields"]["cws_engaged"] = 1
    # test["fields"]["spare26"] = 1
    # test["fields"]["flash_vert_mode"] = 1
    # test["fields"]["pitch_mode"] = 1
    # test["fields"]["capture_sub_mode"] = 1     
    # test["sdi"] = 1
    # test["parity"] = 1
    # int32 = arinc_274(test)

# def test_275(self)
    # test["label"] = 1
    # test["ssm"] = 1
    # test["fields"]["capture_sub_mode"] = 1
    # test["fields"]["hdg_mode"] = 1
    # test["fields"]["half_bank_active"] = 1
    # test["fields"]["bc_sub_mode"] = 1
    # test["fields"]["loc_sub_mode"] = 1
    # test["fields"]["spare16"] = 1
    # test["fields"]["ga_mode"] = 1
    # test["fields"]["straight_and_level"] = 1
    # test["fields"]["spare19"] = 1
    # test["fields"]["roll_mode"] = 1
    # test["fields"]["capture_sub_mode"] = 1
    # test["fields"]["vor_sub_mode"] = 1
    # test["fields"]["track_sub_mode"] = 1    
    # test["fields"]["level_mode"] = 1
    # test["fields"]["intercept_sub_mode"] = 1
    # test["fields"]["nav_mode"] = 1
    # test["fields"]["apr_mode"] = 1
    # test["fields"]["flash_ap_lateral_mode"] = 1   
    # test["fields"]["tcs_mode"] = 1   
    # test["sdi"] = 1
    # test["parity"] = 1
    # int32 = arinc_275(test)

# def test_300(self)
    # test["label"] = 1
    # test["ssm"] = 1
    # test["fields"]["yaw_trim_status"] = 1
    # test["fields"]["roll_trim_status"] = 1
    # test["fields"]["ap_engaged"] = 1
    # test["fields"]["fd_engaged"] = 1
    # test["fields"]["yd_selected"] = 1
    # test["fields"]["ap_status"] = 1
    # test["fields"]["lateral_arm_status"] = 1
    # test["fields"]["lateral_mode_status"] = 1
    # test["fields"]["vertical_arm_status"] = 1
    # test["fields"]["gs_arm_status"] = 1
    # test["fields"]["vert_mode_status"] = 1
    # test["fields"]["pitch_trim_status"] = 1
    # test["sdi"] = 1
    # test["parity"] = 1
    # int32 = arinc_300(test)

# def test_301(self)
    # test["label"] = 1
    # test["ssm"] = 1
    # test["fields"]g["underspeed"] = 1
    # test["fields"]["overspeed"] = 1
    # test["fields"]["speed_protect"] = 1
    # test["fields"]["bank_limit"] = 1
    # test["fields"]["servo_limit"] = 1
    # test["fields"]["servo_fail"] = 1
    # test["fields"]["trimming"] = 1
    # test["fields"]["no_pfd_comm"] = 1
    # test["fields"]["spare19_27"] = 1
    # test["fields"]["ap_inop"] = 1
    # test["fields"]["ap_disconnect"] = 1
    # test["sdi"] = 1
    # test["parity"] = 1
    # int32 = arinc_301(test)

# def test_102(self)
    # data = calculation(test["fields"]["data"], 1, 15)
    # test["label"] = 1
    # test["ssm"] = 1
    # test["fields"]["altitude_select_knob"] = 1
    # test["fields"]["spare12"] = 1
    # test["fields"]["data"] = 1
    # test["sdi"] = 1
    # test["parity"] = 1
    # int32 = arinc_102(test)

# def test_103(self)
    # data = calculation(test["fields"]["data"], 0.25, 12)
    # test["label"] = 1
    # test["ssm"] = 1
    # test["fields"]["airspeed_select_knob"] = 1
    # test["fields"]["spare12_17"] = 1
    # test["fields"]["data"] = 1
    # test["sdi"] = 1
    # test["parity"] = 1
    # int32 = arinc_103(test)

# def test_104(self)
    # data = calculation(test["fields"]["data"], 1, 17)
    # test["label"] = 1
    # test["ssm"] = 1
    # test["fields"]["vertspeed_select_knob"] = 1
    # test["fields"]["spare12_14"] = 1
    # test["fields"]["data"] = 1
    # test["sdi"] = 1
    # test["parity"] = 1
    # int32 = arinc_104(test)

# def test_none(self)
    # int32 = word["word"] & 0xffffffff

# def main(word)
    # label_oct = None
    # if "label" in word:
        # label = word["label"]
        # label_oct = int(str(label), 8)
        # word["label"] = label_oct
        # test = word
    # elif label_oct == 0o102:
        # test_140(self)
    # elif label_oct == 0o102:
        # test_141(self)
    # elif label_oct == 0o102:
        # test_273(self)
    # elif label_oct == 0o102:
        # test_274(self)
    # elif label_oct == 0o102:
        # test_275(self)
    # elif label_oct == 0o102:
        # test_300(self)
    # elif label_oct == 0o102:
        # test_301(self)
    # elif label_oct == 0o102:
        # test_102(self)
    # elif label_oct == 0o102:
        # test_103(self)
    # elif label_oct == 0o102:
        # test_104(self)
    # elif "word" in word and label_oct is None:
        # test_none(self)    
    # else:
        # assert False
    # return int32
    
    
    
    # def test1(self):
        # input = [{"label": 102,}] # Make this
        # output = output_words(input)
        # expected_output = None # make this
        # self.assertEquals(expected_output, output)