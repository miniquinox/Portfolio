dict = {1: {
        "label": 0o102, 
        "ssm": "normal", 
        "fields": {
            "altitude_select_knob": 1,
            "spare12": 0,
            "data": 7501
        },
        "sdi": 0,
        "parity": 0
        },
        
        2: {
        "label": 0o103, 
        "ssm": "normal", 
        "fields": {
            "airspeed_select_knob": 1,
            "spare12_17": 0,  
            "data": 73
        },
        "sdi": 0,
        "parity": 0 
        },
        
        3: {
        "label": 0o104, 
        "ssm": "normal", 
        "fields": {
            "vertspeed_select_knob": 1,
            "spare12_14": 0,  
            "data": 1000
        },
        "sdi": 0,
        "parity": 0 
        },

        4: {
        "label": 0o140, 
        "ssm": "normal", 
        "fields": {
            "spare11_14": 0, 
            "data": 5 
        },
        "sdi": 0,
        "parity": 0
        },
        
        5: {
        "label": 0o141, 
        "ssm": "normal", 
        "fields": {
            "spare11_16": 0, 
            "data": 4
        },        
        "sdi": 0,
        "parity": 0 
        },
        
        6: {
        "label": 0o273, 
        "ssm": "normal", 
        "fields": { 
            "spare11": 0,
            "alt_armed": 0,
            "nav_armed": 1,
            "lnav_armed": 0,
            "vnav_armed": 0,
            "bc_armed": 1,
            "loc_armed": 0,
            "apr_armed": 1,
            "vgp_armed": 0, 
            "spare20_21": 2, 
            "gs_armed": 0,
            "vor_armed": 1,
            "spare24_29": 4 
        },
        "sdi": 0,
        "parity": 0 
        },
        
        7: {
        "label": 0o274, 
        "ssm": "normal", 
        "fields": { 
            "ias_mode": 0,
            "vnav_mode": 1,
            "alt_hold_mode": 0,
            "vs_mode": 1,
            "toga_around_mode": 0,
            "ga_mode": 1,
            "vgp_active": 0,
            "envelope_protect": 0,
            "gs_mode": 0,
            "gp_mode": 0,
            "vpth_mode": 0,
            "level_mode": 0,
            "spare23": 0, 
            "cws_engaged": 0,
            "spare26": 1, 
            "flash_vert_mode": 0,
            "pitch_mode": 0,
            "capture_sub_mode": 0
        },
        "sdi": 0,
        "parity": 0 
        },
        
        8: {
        "label": 0o275, 
        "ssm": "normal", 
        "fields": { 
            "lnav_sub_mode": 0,
            "hdg_mode": 0,
            "half_bank_active": 0,
            "bc_sub_mode": 0,
            "loc_sub_mode": 0,
            "spare16": 0,
            "ga_mode": 0,
            "straight_and_level": 0,
            "spare19": 0,
            "roll_mode": 0,
            "capture_sub_mode": 0,
            "vor_sub_mode": 0,
            "track_sub_mode": 0,
            "level_mode": 0,
            "intercept_sub_mode": 0,
            "nav_mode": 0,
            "apr_mode": 0,
            "flash_ap_lateral_mode": 0,
            "tcs_mode": 0
        },
        "sdi": 0,
        "parity": 0 
        },
        
        9: {
        "label": 0o300, 
        "ssm": "normal", 
        "fields": { 
            "yaw_trim_status": 0, 
            "roll_trim_status": 0, 
            "ap_engaged": 0,
            "fd_engaged": 0,
            "yd_selected": 0,
            "ap_status": 3, 
            "lateral_arm_status": 0,
            "lateral_mode_status": 0,
            "vertical_arm_status": 0,
            "gs_arm_status": 0,
            "vert_mode_status": 0,
            "pitch_trim_status": 3 
            },
        "sdi": 0,
        "parity": 0 
        },
        
        10: {
        "label": 0o301, 
        "ssm": "normal", 
        "fields": { 
            "underspeed": 0,
            "overspeed": 0,
            "speed_protect": 0,
            "bank_limit": 0,
            "servo_limit": 0,
            "servo_fail": 0,
            "trimming": 0,
            "no_pfd_comm": 0,
            "spare19_27": 0, 
            "ap_inop": 0,
            "ap_disconnect": 0
        },
        "sdi": 0,
        "parity": 0 
        },
        
        11: {
        "label": "Label not registered", 
        "ssm": "normal", 
        "fields": { 
            "general_data": 0,
        },
        "sdi": 0,
        "parity": 0 
        }}
        
WORD = 0x5D156A42 # Label 102
# WORD = 0x12345643 # Label 103
# WORD = 0x789ABC44 # Label 104
# WORD = 0xDEF50560 # Label 140
# WORD = 0x477A0F61 # Label 141
# WORD = 0x28AD3FBB # Label 273
# WORD = 0x930E42BC # Label 274
# WORD = 0x2250FFBD # Label 275
# WORD = 0x5055ADC0 # Label 300
# WORD = 0x5A6D9FC1 # Label 301
# WORD = 0x159FAC36 # General case (Label 66)
VALUE = WORD & 0xff # Label
print "\n Here is your label ", oct(VALUE), "\n"
            
for key in dict[1]: # Label 102
    if dict[1][key] == (VALUE):
        
        sdi = (WORD & 0xc00000) >> 22
        altitude_select_knob = (WORD & 0x200000)  >> 21
        spare12 = WORD & (0x100000) >> 20
        data13_28 = (WORD & 0xffff0) >> 4
        sign_bit = (WORD & 0x8) >> 3
        ssm = (WORD & 0x6) >> 1
        parity = (WORD & 0x1) >> 0        

        dict[1]["sdi"] = bin(sdi)
        dict[1]["fields"]["altitude_select_knob"] = bin(altitude_select_knob)
        dict[1]["fields"]["spare12"] = bin(spare12)
        dict[1]["fields"]["data13_28"] = bin(data13_28)
        dict[1]["fields"]["sign_bit"] = bin(sign_bit)
        dict[1]["ssm"] = bin(ssm)
        dict[1]["parity"] = bin(parity)

        print(dict[1])
        
    elif dict[2][key] == (VALUE): # Label 103
        
        sdi = (WORD & 0xc00000) >> 22
        airspeed_select_knob = (WORD & 0x200000)  >> 21
        spare12_17 = WORD & (0x1f8000) >> 15
        data18_28 = (WORD & 0x7ff0) >> 4
        sign_bit = (WORD & 0x8) >> 3
        ssm = (WORD & 0x6) >> 1
        parity = (WORD & 0x1) >> 0        

        dict[2]["sdi"] = bin(sdi)
        dict[2]["fields"]["airspeed_select_knob"] = bin(airspeed_select_knob)
        dict[2]["fields"]["spare12_17"] = bin(spare12_17)
        dict[2]["fields"]["data18_28"] = bin(data18_28)
        dict[2]["fields"]["sign_bit"] = bin(sign_bit)
        dict[2]["ssm"] = bin(ssm)
        dict[2]["parity"] = bin(parity)

        print(dict[2])    
        
    elif dict[3][key] == (VALUE): # Label 104
        
        sdi = (WORD & 0xc00000) >> 22
        vertspeed_select_knob = (WORD & 0x200000)  >> 21
        spare12_14 = WORD & (0x1c0000) >> 18
        data15_28 = (WORD & 0x3fff0) >> 4
        sign_bit = (WORD & 0x8) >> 3
        ssm = (WORD & 0x6) >> 1
        parity = (WORD & 0x1) >> 0        

        dict[3]["sdi"] = bin(sdi)
        dict[3]["fields"]["vertspeed_select_knob"] = bin(vertspeed_select_knob)
        dict[3]["fields"]["spare12_14"] = bin(spare12_14)
        dict[3]["fields"]["data15_28"] = bin(data15_28)
        dict[3]["fields"]["sign_bit"] = bin(sign_bit)
        dict[3]["ssm"] = bin(ssm)
        dict[3]["parity"] = bin(parity)

        print(dict[3])
    
    elif dict[4][key] == (VALUE): # Label 140
        
        sdi = (WORD & 0xc00000) >> 22
        spare11_16 = WORD & (0x3f0000) >> 16
        data17_28 = (WORD & 0xfff0) >> 4
        sign_bit = (WORD & 0x8) >> 3
        ssm = (WORD & 0x6) >> 1
        parity = (WORD & 0x1) >> 0        

        dict[4]["sdi"] = bin(sdi)
        dict[4]["fields"]["vertspeed_select_knob"] = bin(airspeed_select_knob)
        dict[4]["fields"]["spare11_16"] = bin(spare11_16)
        dict[4]["fields"]["data17_28"] = bin(data17_28)
        dict[4]["fields"]["sign_bit"] = bin(sign_bit)
        dict[4]["ssm"] = bin(ssm)
        dict[4]["parity"] = bin(parity)

        print(dict[4])

    elif dict[5][key] == (VALUE): # Label 141
        
        sdi = (WORD & 0xc00000) >> 22
        spare11_16 = WORD & (0x3f0000) >> 16
        data17_28 = (WORD & 0xfff0) >> 4
        sign_bit = (WORD & 0x8) >> 3
        ssm = (WORD & 0x6) >> 1
        parity = (WORD & 0x1) >> 0        

        dict[5]["sdi"] = bin(sdi)
        dict[5]["fields"]["spare11_16"] = bin(spare11_16)
        dict[5]["fields"]["data17_28"] = bin(data17_28)
        dict[5]["fields"]["sign_bit"] = bin(sign_bit)
        dict[5]["ssm"] = bin(ssm)
        dict[5]["parity"] = bin(parity)        

        print(dict[5])

    elif dict[6][key] == (VALUE): # Label 273
        
        sdi = (WORD & 0xc00000) >> 22
        spare11 = WORD & (0x200000) >> 21
        alt_armed = (WORD & 0x100000) >> 20
        nav_armed = (WORD & 0x80000) >> 19
        lnav_armed = (WORD & 0x40000) >> 18
        vnav_armed = (WORD & 0x20000) >> 17
        bc_armed = (WORD & 0x10000) >> 16
        loc_armed = (WORD & 0x8000) >> 15
        apr_armed = (WORD & 0x4000) >> 14
        vgp_armed = (WORD & 0x2000) >> 13
        spare20_21 = (WORD & 0x18) >> 11
        gs_armed = (WORD & 0x400) >> 10
        vor_armed = (WORD & 0x200) >> 9
        gp_armed = (WORD & 0x100) >> 8
        vpth_armed = (WORD & 0x80) >> 7
        spare26_29 = (WORD & 0x3c) >> 3
        ssm = (WORD & 0x6) >> 1
        parity = (WORD & 0x1) >> 0

        dict[6]["sdi"] = bin(sdi)
        dict[6]["fields"]["spare11"] = bin(spare11)
        dict[6]["fields"]["alt_armed"] = bin(alt_armed)
        dict[6]["fields"]["nav_armed"] = bin(nav_armed)
        dict[6]["fields"]["lnav_armed"] = bin(lnav_armed)
        dict[6]["fields"]["vnav_armed"] = bin(vnav_armed)
        dict[6]["fields"]["bc_armed"] = bin(bc_armed)
        dict[6]["fields"]["loc_armed"] = bin(loc_armed)
        dict[6]["fields"]["apr_armed"] = bin(apr_armed)
        dict[6]["fields"]["vgp_armed"] = bin(vgp_armed)
        dict[6]["fields"]["spare20_21"] = bin(spare20_21)
        dict[6]["fields"]["gs_armed"] = bin(gs_armed)
        dict[6]["fields"]["vor_armed"] = bin(vor_armed)
        dict[6]["fields"]["gp_armed"] = bin(gp_armed)
        dict[6]["fields"]["vpth_armed"] = bin(vpth_armed)
        dict[6]["fields"]["spare26_29"] = bin(spare26_29)
        dict[6]["ssm"] = bin(ssm)
        dict[6]["parity"] = bin(parity)

        print(dict[6])

    elif dict[7][key] == (VALUE): # Label 274
        
        sdi = (WORD & 0xc00000) >> 22
        ias_mode = WORD & (0x200000) >> 21
        vnav_mode = (WORD & 0x100000) >> 20
        alt_hold_mode = WORD & (0x80000) >> 19
        vs_mode = WORD & (0x40000) >> 18
        toga_around_mode = (WORD & 0x20000) >> 17
        ga_mode = (WORD & 0x10000) >> 16
        vgp_active = (WORD & 0x8000) >> 15
        envelope_protect = (WORD & 0x4000) >> 14
        gs_mode = (WORD & 0x2000) >> 13
        gp_mode = (WORD & 0x1000) >> 12
        vpth_mode = (WORD & 0x800) >> 11
        level_mode = (WORD & 0x400) >> 10
        spare23_24 = (WORD & 0x300) >> 8
        cws_engaged = (WORD & 0x80) >> 7
        spare26 = (WORD & 0x40) >> 6
        flash_vert_mode = (WORD & 0x20) >> 5
        pitch_mode = (WORD & 0x10) >> 4
        capture_sub_mode = (WORD & 0x8) >> 3
        ssm = (WORD & 0x6) >> 1
        parity = (WORD & 0x1) >> 0

        dict[7]["sdi"] = bin(sdi)
        dict[7]["fields"]["ias_mode"] = bin(ias_mode)
        dict[7]["fields"]["vnav_mode"] = bin(vnav_mode)
        dict[7]["fields"]["alt_hold_mode"] = bin(alt_hold_mode)
        dict[7]["fields"]["vs_mode"] = bin(vs_mode)
        dict[7]["fields"]["toga_around_mode"] = bin(toga_around_mode)
        dict[7]["fields"]["ga_mode"] = bin(ga_mode)
        dict[7]["fields"]["vgp_active"] = bin(vgp_active)
        dict[7]["fields"]["envelope_protect"] = bin(envelope_protect)
        dict[7]["fields"]["gs_mode"] = bin(gs_mode)
        dict[7]["fields"]["gp_mode"] = bin(gp_mode)
        dict[7]["fields"]["vpth_mode"] = bin(vpth_mode)
        dict[7]["fields"]["level_mode"] = bin(level_mode)
        dict[7]["fields"]["spare23_24"] = bin(spare23_24)
        dict[7]["fields"]["cws_engaged"] = bin(cws_engaged)
        dict[7]["fields"]["spare26"] = bin(spare26)
        dict[7]["fields"]["flash_vert_mode"] = bin(flash_vert_mode)
        dict[7]["fields"]["pitch_mode"] = bin(pitch_mode)
        dict[7]["fields"]["capture_sub_mode"] = bin(capture_sub_mode)
        dict[7]["ssm"] = bin(ssm)
        dict[7]["parity"] = bin(parity)

        print(dict[7])

    elif dict[8][key] == (VALUE): # Label 275
        
        sdi = (WORD & 0xc00000) >> 22
        lnav_sub_mode = WORD & (0x200000) >> 21
        hdg_mode = WORD & (0x100000) >> 20
        half_bank_active = (WORD & 0x80000) >> 19
        bc_sub_mode = WORD & (0x40000) >> 18
        loc_sub_mode = WORD & (0x20000) >> 17
        spare16 = (WORD & 0x10000) >> 16
        ga_mode = (WORD & 0x8000) >> 15
        straight_and_level = (WORD & 0x4000) >> 14
        spare19 = (WORD & 0x2000) >> 13
        roll_mode = (WORD & 0x1000) >> 12
        capture_sub_mode = (WORD & 0x800) >> 11
        vor_sub_mode = (WORD & 0x400) >> 10
        track_sub_mode = (WORD & 0x200) >> 9
        level_mode = (WORD & 0x100) >> 8
        intercept_sub_mode = (WORD & 0x80) >> 7
        nav_mode = (WORD & 0x40) >> 6
        apr_mode = (WORD & 0x20) >> 5
        flash_ap_lateral_mode = (WORD & 0x10) >> 4
        tcs_mode = (WORD & 0x8) >> 3
        ssm = (WORD & 0x6) >> 1
        parity = (WORD & 0x1) >> 0

        dict[8]["sdi"] = bin(sdi)
        dict[8]["fields"]["lnav_sub_mode"] = bin(lnav_sub_mode)
        dict[8]["fields"]["hdg_mode"] = bin(hdg_mode)
        dict[8]["fields"]["half_bank_active"] = bin(half_bank_active)
        dict[8]["fields"]["bc_sub_mode"] = bin(bc_sub_mode)
        dict[8]["fields"]["loc_sub_mode"] = bin(loc_sub_mode)
        dict[8]["fields"]["spare16"] = bin(spare16)
        dict[8]["fields"]["ga_mode"] = bin(ga_mode)
        dict[8]["fields"]["straight_and_level"] = bin(straight_and_level)
        dict[8]["fields"]["spare19"] = bin(spare19)
        dict[8]["fields"]["roll_mode"] = bin(roll_mode)
        dict[8]["fields"]["capture_sub_mode"] = bin(capture_sub_mode)
        dict[8]["fields"]["vor_sub_mode"] = bin(vor_sub_mode)
        dict[8]["fields"]["track_sub_mode"] = bin(track_sub_mode)
        dict[8]["fields"]["level_mode"] = bin(level_mode)
        dict[8]["fields"]["intercept_sub_mode"] = bin(intercept_sub_mode)
        dict[8]["fields"]["nav_mode"] = bin(nav_mode)
        dict[8]["fields"]["apr_mode"] = bin(apr_mode)
        dict[8]["fields"]["flash_ap_lateral_mode"] = bin(flash_ap_lateral_mode)
        dict[8]["fields"]["tcs_mode"] = bin(tcs_mode)
        dict[8]["ssm"] = bin(ssm)
        dict[8]["parity"] = bin(parity)

        print(dict[8])
        
    elif dict[9][key] == (VALUE): # Label 300
        
        sdi = (WORD & 0xc00000) >> 22
        yaw_trim_status = (WORD & 0x380000) >> 21
        roll_trim_status = (WORD & 0x70000) >> 16
        ap_engaged = (WORD & 0x8000) >> 15
        fd_engaged = (WORD & 0x4000) >> 14
        yd_selected = (WORD & 0x2000) >> 13
        ap_status = (WORD & 0x1800) >> 11
        lateral_arm_status = (WORD & 0x400) >> 10
        lateral_mode_status = (WORD & 0x200) >> 9
        vertical_arm_status = (WORD & 0x100) >> 8
        gs_arm_status = (WORD & 0x80) >> 7
        vert_mode_status = (WORD & 0x40) >> 6
        pitch_trim_status = (WORD & 0x38) >> 3
        ssm = (WORD & 0x6) >> 1
        parity = (WORD & 0x1) >> 0

        dict[9]["sdi"] = bin(sdi)
        dict[9]["fields"]["yaw_trim_status"] = bin(yaw_trim_status)
        dict[9]["fields"]["roll_trim_status"] = bin(roll_trim_status)
        dict[9]["fields"]["ap_engaged"] = bin(ap_engaged)
        dict[9]["fields"]["fd_engaged"] = bin(fd_engaged)
        dict[9]["fields"]["yd_selected"] = bin(yd_selected)
        dict[9]["fields"]["ap_status"] = bin(ap_status)
        dict[9]["fields"]["lateral_arm_status"] = bin(lateral_arm_status)
        dict[9]["fields"]["lateral_mode_status"] = bin(lateral_mode_status)  
        dict[9]["fields"]["vertical_arm_status"] = bin(vertical_arm_status)
        dict[9]["fields"]["gs_arm_status"] = bin(gs_arm_status)
        dict[9]["fields"]["vert_mode_status"] = bin(vert_mode_status)
        dict[9]["fields"]["pitch_trim_status"] = bin(pitch_trim_status)
        dict[9]["ssm"] = bin(ssm)
        dict[9]["parity"] = bin(parity)

        print(dict[9])
        
    elif dict[10][key] == (VALUE): # Label 301
        
        sdi = (WORD & 0xc00000) >> 22
        underspeed = (WORD & 0x200000) >> 21
        overspeed = (WORD & 0x100000) >> 20
        speed_protect = (WORD & 0x80000) >> 19
        bank_limit = (WORD & 0x40000) >> 18
        servo_limit = (WORD & 0x20000) >> 17
        servo_fail = (WORD & 0x10000) >> 16
        trimming = (WORD & 0x8000) >> 15
        no_pfd_comm = (WORD & 0x4000) >> 14
        spare19_27 = (WORD & 0x3FE0) >> 5
        failure = (WORD & 0x10) >> 4
        ap_disconnect = (WORD & 0x8) >> 3
        ssm = (WORD & 0x6) >> 1
        parity = (WORD & 0x1) >> 0

        dict[10]["sdi"] = bin(sdi)
        dict[10]["fields"]["underspeed"] = bin(underspeed)
        dict[10]["fields"]["overspeed"] = bin(overspeed)
        dict[10]["fields"]["speed_protect"] = bin(speed_protect)
        dict[10]["fields"]["bank_limit"] = bin(bank_limit)
        dict[10]["fields"]["servo_limit"] = bin(servo_limit)
        dict[10]["fields"]["servo_fail"] = bin(servo_fail)
        dict[10]["fields"]["trimming"] = bin(trimming)
        dict[10]["fields"]["no_pfd_comm"] = bin(no_pfd_comm)
        dict[10]["fields"]["spare19_27"] = bin(spare19_27)
        dict[10]["fields"]["failure"] = bin(failure)
        dict[10]["fields"]["ap_disconnect"] = bin(ap_disconnect)
        dict[10]["ssm"] = bin(ssm)
        dict[10]["parity"] = bin(parity)

        print(dict[10])

    else:
        
        sdi = (WORD & 0xc00000) >> 22
        general_data = (WORD & 0x3FFFFC)  >> 3
        ssm = (WORD & 0x6) >> 1
        parity = (WORD & 0x1) >> 0        

        dict[11]["sdi"] = bin(sdi)
        dict[11]["fields"]["general_data"] = hex(general_data)
        dict[11]["ssm"] = bin(ssm)
        dict[11]["parity"] = bin(parity)

        print(dict[11])