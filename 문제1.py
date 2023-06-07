#문제1. 3의 배수를 10개만 한줄로 출력하기
for i in range(3,31,3):
    print(i, end=' ')
print()

#문제2. 100, 90, 80, 70,,,, 10 까지 한줄로 출력하기
for i in range(100, 0, -10):
    print(i, end=' ')
print()

#문제3. 다음 리스트에서 홀수번째 방 데이터만 출력하기 1,3,5,7,9,,,,
colors=['red', 'green', 'blue', 'cyan', 'magenta', 'black', 'brown', 'yellow', 'green']
for i in range(1, len(colors), 2):
    print(colors[i], end=' ')
print()

#문제4. 구구단 4단 출력하기
dan = 4   #단수를 변경할 수 있도록 변수 입력
for i in range(1, 10):
    print(f"{dan} X {i} = {dan*i}")


#문제5. 정수를 1 ~100까지 출력하는데, 10개마다 줄바꿈을 할것 힌트) if문도 사용

for i in range(1, 101): 
    print(i, end = ' ')
    if i %10 == 0:  #10개마다 줄바꿈을 하는 방법
        print()
print()

