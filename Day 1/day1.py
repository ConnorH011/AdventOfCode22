f = open("input.txt", "r")
#print(f.read())
arr = []
count = 0
calCount = 0
msg = ""

for item in f:
    count = count + 1
    #print("line: " + str(count))
    if item == '\n':
        msg = ""
        msg = msg + str(calCount)
        arr.append(calCount)
        calCount = 0
        #print("reset: Final count = " + msg)

    else:
        calCount = calCount + int(item)
        #print(calCount)

firstElf = 0
secondElf = 0
thirdElf = 0

for i in range (0, len(arr)):

    if arr[i] > firstElf:
        secondElf = firstElf
        thirdElf = secondElf
        firstElf = arr[i]
    elif arr[i] > secondElf:
        thirdElf = secondElf
        secondElf = arr[i]
    elif arr[i] > thirdElf:
        thirdElf= arr[i]

max = firstElf + secondElf + thirdElf
print(thirdElf)
print(secondElf)
print(firstElf)
print("total of all 3 = " + str(max))