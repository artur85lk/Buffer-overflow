#  BED CHAR

def check(line, a, b):
        x = line[a]
        y = line[b]
        if (x == "F" and y == "0") or (x == "0" and y == "1") or (x == "1" and y == "2") \
                or (x == "2" and y == "3") or (x == "3" and y == "4") or (x == "4" and y == "5") \
                or (x == "5" and y == "6") or (x == "6" and y == "7") or (x == "7" and y == "8") \
                or (x == "8" and y == "9") or (x == "9" and y == "A") or (x == "A" and y == "B") \
                or (x == "B" and y == "C") or (x == "C" and y == "D") or (x == "D" and y == "E") \
                or (x == "E" and y == "F"):
            return line
        else:
            print("Error")


def check2(line, a, b):
    x = b[1]
    y = line[a]
    if (x == "F" and y == "0") or (x == "0" and y == "1") or (x == "1" and y == "2") \
            or (x == "2" and y == "3") or (x == "3" and y == "4") or (x == "4" and y == "5") \
            or (x == "5" and y == "6") or (x == "6" and y == "7") or (x == "7" and y == "8") \
            or (x == "8" and y == "9") or (x == "9" and y == "A") or (x == "A" and y == "B") \
            or (x == "B" and y == "C") or (x == "C" and y == "D") or (x == "D" and y == "E") \
            or (x == "E" and y == "F"):
        return line
    else:
        print("Error")

f = open("calc.txt","r")
lines = f.readlines()
s = "00000000"
for line in lines:
    try:
        line = line.replace("\n","")
        check2(line, 7, s)
        s = line
        print(line[6], line[7])
        check(line,7,5)
        if line[7] == "F":
            print()
        print(line[4], line[5])
        check(line, 5, 3)
        if line[5] == "F":
            print()
        print(line[2], line[3])
        check(line, 3, 1)
        if line[3] == "F":
            print()
        print(line[0], line[1])
        if line[1] == "F":
            print()
    except IndexError:
        print("")
f.close()
