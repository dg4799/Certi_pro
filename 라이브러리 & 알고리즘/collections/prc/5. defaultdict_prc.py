from collections import defaultdict

fruit = {'apple':100, 'grape':200, 'orange':300, 'banana':400}  # 괴일이 딕셔너리로 종류별 갯수가 있을때


d = defaultdict(list)                                           # 일정 갯수 이상의 과일명을
for i in fruit:                                                 # defaultdict를 사용해서 딕셔너리로 append해서 생성 가능.
    if fruit[i] <= 200: d["~200"].append(i)                     # 본래 딕셔너리는 value없이 생성 못함!!
    elif 200 < fruit[i] <= 400: d["~400"].append(i)

print(d)
print(d["~200"])
print(d["~400"])

d = {}                                                          # 딕셔너리는 value 없이 생성할 수 없음
for i in fruit:
    if fruit[i] <= 200: d["~200"].append(i)
    elif 200 < fruit[i] <= 400: d["~400"].append(i)
