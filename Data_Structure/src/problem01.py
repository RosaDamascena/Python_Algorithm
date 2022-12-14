n = input()
numbers = list(input()) # 리스트 형태로 저장
sum = 0

for i in numbers :
    sum = sum + int(i) # 각 자리 수 더하기

print(sum)