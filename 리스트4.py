#list 관련한 문제
"""
1. flowers 변수에 다름 꽃들을 입력하세요
작약, 국화, 목련, 목단, 장미, 해바라기

2. 0, 2, 4 번 데이터 출력하기(인덱싱, 슬라이싱 둘다 사용하기)

3. 해바라기 => 백일홍 으로 수정하기

4. 사루비아, 맨드라미 두 종류 추가하기

5. 목련 삭제

6. 현재 데이터 개수 출력하기

7. 마지막 데이터 삭제하기

"""

flowers = ["작약", "국화", "목련", "목단", "장미", "해바라기"]

print( flowers[0], flowers[2], flowers[4]) #인덱싱

print( flowers[0:5:2]) #슬라이싱 0,2,4

#수정
flowers[5]="백일홍"
print( flowers )

#추가하기
flowers.append("사루비아")
flowers.append("맨드라미")
print( flowers )

#삭제
flowers.remove("목련") 
print( flowers )

print( "데이터 개수 : ", len(flowers))

#위치삭제
del flowers[len(flowers)-1 ]
print( flowers )