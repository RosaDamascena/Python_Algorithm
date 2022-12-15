import sys
input = sys.stdin.readline

numOfNumbers, numOfQuestions = map(int, input().split())    # 수의 개수 numOfNumbers와 합을 구해야 하는 횟수 numOfQuestions 입력 받기
numbers = list(map(int, input().split()))   # numOfNumbers만큼 숫자 입력 받기

prefixSum = [0] # 합배열 변수 선언
temp = 0

for i in numbers :
    temp = temp + i
    prefixSum.append(temp) # 합 배열 만들기
 
for i in range(numOfQuestions) :
    start, end = map(int, input().split())
    print(prefixSum[end] - prefixSum[start])