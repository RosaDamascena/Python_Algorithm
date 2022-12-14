n = input()
myScoreList = list(map(int, input().split( )))
myMax = max(myScoreList)

sum = sum(myScoreList)

print(sum * 100 / myMax / int(n))