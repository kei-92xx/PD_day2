#1~10까지의 합계 구하기
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 

"""
    f(n) = 1~n까지의 합계
         = f(n-1) + n
         = f(n-2) + n-1 + n
         
    sum    i    sum
    0      1     1
    1      2     3
    3      3     6
    6      4     10
    sum = 0 #값이 누적되어야 하기대문에 처음에 0으로 시작한다
    sum = sum + i #누적하기 , i=1, 10
"""
sum = 0
i = 1
print(sum, i)

sum = sum + i
i = i + 1
print(sum, i)

sum = sum + i
i = i + 1
print(sum, i)

sum = sum + i
i = i + 1
print(sum, i)


sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)