import random



a=[]
for experimentNumber in range(10000):
    a.append(random.randint(0, 1))


pattern1 = [1, 1, 1, 1, 1, 1]
search_list = a
cursor1 = 0
found1 = []
for i in search_list:
    if i == pattern1[cursor1]:
        cursor1 += 1
        if cursor1 == len(pattern1):
            found1.append(pattern1)
            cursor1 = 0
    else:
        cursor1 = 0


pattern2 = [0, 0, 0, 0, 0, 0]
cursor2 = 0
found2 = []
for i in search_list:
    if i == pattern2[cursor2]:
        cursor2 += 1
        if cursor2 == len(pattern2):
            found2.append(pattern2)
            cursor2 = 0
    else:
        cursor2 = 0


numberOfStreaks=(len(found1)+len(found2))
print("The Number of Streaks in 10,000 coin flips is:" + str(numberOfStreaks) )






