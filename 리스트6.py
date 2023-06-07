#정수 5개 입력받기
numList = []
for i in range(1, 6): #range - 숫자를 연속적으로 생성해 낸다. 1,2,3,4,5 까지만 생성
    num = int(input("숫자 : "))
    numList.append( num )
    
print( numList )