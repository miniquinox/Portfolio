import re

# rlabel = re.compile('.*label\s*:\s*(.*)')
# rssm = re.compile('.*sdi\s*:\s*(.*)')
# rsdi = re.compile('.*ssm\s*:\s*(.*)')
# rparity = re.compile('.*parity\s*:\s*(.*)')

rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
            else:
                m = rsdi.match(line)
                if m is not None:
                    sdi = m.group(1)
                else:
                    m = rparity.match(line)
                    if m is not None:
                        parity = m.group(1)
                    
if labelnum is not None:
    word(outFile, labelnum, ssm, sdi, parity)
    labelnum = None

inFile.close()
outFile.close()



# dictionary = {}

# with open("json_dict.txt") as file:
    # for lines 3 to 9 in file:
        # (key, val) = line.split()
        # label_102[char(key)] = val
    # for line 12 to 18 in file:
        # (key, val) = line.split()
        # label_103[char(key)] = val
    # for line 21 to 27 in file:
        # (key, val) = line.split()
        # label_104[char(key)] = val
    # for line 30 to 35 in file:
        # (key, val) = line.split()
        # label_140[char(key)] = val
    # for line 33 to 43 in file:
        # (key, val) = line.split()
        # label_141[char(key)] = val
    # for line 46 to 62 in file:
        # (key, val) = line.split()
        # label_273[char(key)] = val
    # for line 65 to 86 in file:
        # (key, val) = line.split()
        # label_274[char(key)] = val
    # for line 89 to 111 in file:
        # (key, val) = line.split()
        # label_275[char(key)] = val
    # for line 114 to 129 in file:
        # (key, val) = line.split()
        # label_300[char(key)] = val
    # for line 132 to 146 in file:
        # (key, val) = line.split()
        # label_301[char(key)] = val    
# print (label_102)



rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')

def word(out, label, ssm, sdi, parity):
    print(label, ssm, sdi, parity)
    out.write('label: %s... ssm = "%s", sdi = "%s",parity = "%s"\n' % (label, ssm, sdi, parity))

inFile = open("json_dict.txt")
outFile = open("result.txt", "w")
firstOfBlock = False
labelnum = None
for line in inFile:
    if line.startswith("-----------------"):
        firstOfBlock = True
        if labelnum is not None:
            word(outFile, labelnum, ssm, sdi, parity)
            labelnum = None
    else:
        if firstOfBlock:
            m = rlabel.match(line)
            if m is not None:
                labelnum = m.group(1)
                firstOfBlock = False
        else:
            line = line.strip()
            m = rssm.match(line)
            if m is not None:
                ssm = m.group(1)
rlabel = re.compile('.*"label"\s*:\s*(.*)')
rssm = re.compile('.*"sdi"\s*:\s*(.*)')
rsdi = re.compile('.*"ssm"\s*:\s*(.*)')
rparity = re.compile('.*"parity"\s*:\s*(.*)')