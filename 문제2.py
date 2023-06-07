#문제1. 1~100까지 중에 홀수의 합계만 구하기
sum = 0
for i in range(1, 100, 2):
    sum = sum + i
print(sum)

#문제2. 1~100까지 중에 7의 배수의 개수 세기
cnt=0
for i in range(1,100):
    if i%7==0:
        cnt=cnt+1
print(cnt)