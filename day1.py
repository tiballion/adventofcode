# Opens the file and reads the data
with open('day1.txt') as f:
    data = f.readlines()

# Removes the newline character from the end of each line
# and convert each "set" of calories in a single list of integers
# and puts all the lists in a single list
full = []
tmp = []
for line in data:
    if line == '\n':
        full.append(tmp)
        tmp = []
    else:
        tmp.append(int(line[:-1]))


# Gets the max of the lists and prints the max value
# PART 1 :
# maxi = 0
# for i in full:
    # if sum(i) > maxi:
        # maxi = sum(i)
# print(maxi)

# Gets the sum of the top 3 values of the sum
# PART 2 :
s = []
for i in full:
    t = sum(i)
    s.append(t)
sort = sorted(s)
print(sum(sort[-3:]))
