from math import floor

ma = [1, 2, 3, 4, 5, 6, 7, 8]

intput = int(raw_input("Enter an integer to search for: "))

print "Array:", ma

print "Iterative search:"

count = 0
found = False
for i in range(0, len(ma)):
    count += 1
    if ma[i] == intput:
        print "Found %s in %s iterations." % (intput, count)
        found = True
        break

if not found:
    print "%s not found." % (intput)

print "\nBinary search:"

count = 0
while len(ma) > 1:
    count += 1
    middle = int(floor(len(ma) / 2))
    if ma[middle] == intput:
        iteration = middle * count
        print "Found %s in %s iterations." % (intput, count)
        break
    elif ma[middle] < intput:
        ma = ma[middle:]
    else:
        ma = ma[:middle]

if len(ma) == 1:
    if ma[0] == intput:
        print "Found %s in %s iterations." % (intput, count+1)
    else:
        print "%s not found." % (intput)

