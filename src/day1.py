from pathlib import Path

print(Path(__file__).parent.parent)
data = (Path(__file__).parent.parent / 'data/day1.txt').read_text()

# What is the total distance between your lists?

leftList = []
rightList = []

for line in data.splitlines():
  left, right = map(int, line.split())
  leftList.append(left)
  rightList.append(right)

leftList.sort()
rightList.sort()

resultList = [abs(left - right) for left, right in zip(leftList, rightList)]

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
