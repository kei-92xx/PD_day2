words = ['school', "asembly", "chair", "hospital", "desk", "rain", "rainbow"]
print( words )
print( "데이터 개수 : ", len(words))

#인덱싱
print( words[0])
print( words[1])
print( words[2])

words[3] = "house"
print( words )

#for문을 이용해 전부 출력하기
for w in words:
 print(w)

#슬라이싱 - 파이썬 이후로 등장하는 문법  리스트변수[시작:종료:증감치]

print( words[0:3]) #0,1,2 마지막꺼는 제외하고 출력한다
#[0:3:1] 마지막 생략하면 1로 알아 듣는다
print( words[0:5:2]) # 0,2,4 번 방만 출력된다

#뒤에서부터 출력가능
print( words[6:4:-1]) # 6,5

#완전히 역순으로 전체출력
print( words[::-1]) # 6,5,4,3,2,1,0
print( words[6:-1:-1]) # 파이썬 버전에 따라 다르게 동작한다. 예전엔 에러가 발생, 지금은 출력안함

print( words[6:0:-1]) # 마지막 0번째는 출력되지 않는데 전체를 역순으로 출력하려면 [::-1]을 사용하자