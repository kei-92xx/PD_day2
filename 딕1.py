#dict타입은 키와 값 쌍으로 데이터를 저장하는 타입이다
# 키와 값 자체는 어떤 타입이든 상관없는데 보통 키의 경우에는 문자열을 많이 사용한다

colors = {'red':'빨간색', 'blue':'파란색', 'green':'초록색', 'black':'검정'}
print( colors['red']) #red, blue, green, black값등을 키라고 하고 키를 통해 데이터를 접근한다
print( colors['blue']) #인덱싱, 슬라이싱 적용 안됨
print( colors['green'])
print( colors['black'])

#dict 타입은 추가, 키값이 이미 존재했다면 수정, 값 바꿔치기, 없었으면 추가
colors['pink']='분홍색'
colors['black']='까만색' #수정

#삭제
del colors['red']
print( colors )

#키값 목록만 - 키 값순서는 내부적으로 알아서, 입력한 순서대로 나오지 않는다
for key in colors:
    print(key, colors[key])
    