"""
Created on Tue Jun  6 11:08:01 2017

@author: Raul
"""
s = 'azcbobobegghaklbeggi'

alphaStreak = ''      # Temp storage of string
tempList = []

for j in range(len(s) - 1):
    i = j
    temp = s[i]
    while s[i] <= s[i+1]:
        temp += s[i+1]
        i += 1
        if i == len(s) - 1:
            break
    tempList.append(temp)
    
print(tempList)

for lst in tempList:
    if len(lst) > len(alphaStreak):
        alphaStreak = lst
    
print('Longest substring in alphabetical order is:', alphaStreak)
