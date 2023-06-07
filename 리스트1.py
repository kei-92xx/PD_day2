"""
name='홍길동'
work_time = 30
per_pay = 20000

name2='임꺽정'
work_time2 = 40
per_pay2 = 15000

pay = work_time * per_pay
pay2 = work_time2 * per_pay2

print( name, work_time, per_pay, pay)
print( name2, work_time2, per_pay2, pay2)
여러 데이터를 하나하나 형식으로 사용하면 많은 시간이걸림 (list) < 를 사용하지 않을경우
"""

#리스트 - 배열, 하나의 메모리에 여러개의 데이터를 저장할 수 있다.
nums = [1,2,3,4,5,6,7,8,9,10] #리스트안에 10개의 데이터를 저장한다
#데이터 공간을 10개 만들고 0번부터 번호를 부여한다, 0,1,2,3,4,5,6,7,8,9 까지 만들어진다
print( nums )
print( nums[0] ) #0번 방의 데이터만, 이걸 인덱싱 이라고 부른다
print( nums[1] )
print( nums[2] )
print( nums[3] )
print( nums[4] )

nums[0] = 10 #인덱싱을 이용해 값을 변경한다
nums[1] = 20
nums[2] = 30
print( nums )

#nums의 배열 자체가 사라지고 새로 만든다
nums = [10,20,30] #새로 메모리를 만들어서 10,20,30을 저장하는거라 위의 리스트는 사라진다
print( nums )

#반복처리
for  n in nums: # for 변수명 in 리스트 타입:  -- 데이터를 하나씩 차례대로  변수로 옮겨준다
    print(n)
    
