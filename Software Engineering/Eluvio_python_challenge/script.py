import sys
import winsound

def get_file():
    n = 11
    total = []
    names = []
    for i in range(1, n):
        filex = []
        samplex = "sample." + str(i)
        names.append(samplex)
        file = open(samplex, "rb")
        byte = file.read(1)
        while byte:
            filex.append(byte)
            byte = file.read(1)
        total.append(filex)
        file.close()
    return total, names

def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    offset = x_longest - longest
    length = longest

    return offset, length

 
# Driver code
if __name__ == "__main__":
    duration = 1000  # milliseconds
    freq = 440  # Hz
    dict = {}
    total, names = get_file()
    result = []
    count_i = 1
    count_j = 0
    temp = total[0]
    my_dict = {}
    status = 0
    for i in total:
        for j in total[count_i:]:
            count_j += 1
            offset, length = longest_common_substring(i, j)
            if length not in dict:
                dict[length] = []
            filename = "sample." + names[count_i - 1] + " and sample." + names[count_j - 1]
            dict[length].append(names)
            dict[length].append(offset)
            nn += 1
            print("Comparison", status, "done")
        count_i += 1
        count_j = count_i

    res = max(k for k, v in dict.items())
    print("\nMax array size =", res)
    print("Found in files: ", dict[res][0])
    print("Offset:", dict[res][1])
    winsound.Beep(freq, duration)
