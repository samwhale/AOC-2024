from parse_data import parseData

# Day 1
# could make this more efficient on import, but this is enough
parsedData = parseData('data/day1.txt')
leftList = []
rightList = []

# What is the total distance between your lists?
for row in parsedData:
  leftList.append(row[0])
  rightList.append(row[1])

leftList.sort()
rightList.sort()

resultList = []

for i in (range(len(leftList))):
  resultList.append(abs(leftList[i] - rightList[i]))

print("Solution 1", sum(resultList))


# Calculate a total similarity score by adding up each number in the left list
# after multiplying it by the number of times that number appears in the right list.

# Find number of times each number appears in the right list
rightMap = {}

for i in range(len(rightList)):
  rightNumber = rightList[i]
  if rightNumber in rightMap:
    rightMap[rightNumber] += 1
  else:
    rightMap[rightNumber] = 1

leftListMultiplied = []

for entry in leftList:
  if entry in rightMap:
    leftListMultiplied.append(entry * rightMap[entry])

print("Solution 2", sum(leftListMultiplied))
