# count : 문자열 내에서 특정 문자가 몇 개나 있는지 세는 메서드
n_text = "Hello, cherry!"
count = n_text.count("i")
print(count)


# find: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는
# 메서드 (없을 경우 -1 return)
n_text = "Hello, cherry!"
position = n_text.find("cherry")
print(position)


# index: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는
# 메서드 (없을 경우 ValueError)
n_text = "Hello, cherry!"
try:
    position = n_text.index("cherry")
    print(position)
except ValueError:
    print("찾는 문자열이 없습니다.")


# join: 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 메서드
cuties = ["cherry", "fairy", "flower"]
joined_cuties = ", ".join(cuties)
print(joined_cuties)


# upper: 문자열 내의 모든 소문자를 대문자로 바꾸는 메서드
# lower: 문자열 내의 모든 대문자를 소문자로 바꾸는 메서드
n_text = "Hello, cherry!"
uppercase_test = n_text.upper()
print(uppercase_test)

lowercase_text = n_text.lower()
print(lowercase_text)


# replace: 문자열 내에서 특정 문자열을 다른 문자열로 바꾸는 메서드
n_text = "Hello, cherry!"
replaced_text = n_text.replace("cherry", "Python")
print(replaced_text)


# split: 문자열을 특정 문자를 기준으로 나누는 메서드(결과는 리스트 형태로 반환)
n_text = "cherry,fairy,flower"
cuties = n_text.split(",")
print(cuties)


# len: 리스트의 길이를 반환하는 내장 함수
n_numbers = [1, 2, 3, 4, 5]
print(len(n_numbers))


# del: 리스트에서 특정 요소를 삭제하는 연산자
n_numbers = [1, 2, 3, 4, 5]
del n_numbers[1]
print(n_numbers)


# append: 리스트의 맨 뒤에 새로운 요소를 추가하는 메서드
n_numbers = [1, 2, 3, 4, 5]
n_numbers.append(6)
print(n_numbers)


# sort: 리스트를 오름차순으로 정렬하는 메서드
n_numbers = [3, 1, 4, 2, 5]
n_numbers.sort()
print(n_numbers)


# reverse: 리스트의 요소 순서를 반대로 뒤집는 메서드
n_numbers = [1, 2, 3, 4, 5]
n_numbers.reverse()
print(n_numbers)


# index: 리스트에서 특정 요소의 인덱스를 반환하는 메서드
cuties = ["fairy", "cherry", "flower"]
print(cuties.index("cherry"))


# insert: 리스트의 특정 위치에 요소를 삽입하는 메서드
n_numbers = [1, 2, 3, 4, 5]
n_numbers.insert(2, 6)
print(n_numbers)


# remove: 리스트에서 특정 요소를 제거하는 메서드
n_numbers = [1, 2, 3, 4, 5]
n_numbers.remove(3)
print(n_numbers)


# pop: 리스트에서 마지막 요소를 빼낸 뒤, 그 요소를 삭제하는 메서드
n_numbers = [1, 2, 3, 4, 5]
n_numbers.pop(3)
print(n_numbers)


# count: 리스트에서 특정 요소의 개수를 세는 메서드
n_numbers = [1, 2, 3, 4, 5]
print(n_numbers.count(3))


# extend: 리스트를 확장하여 새로운 요소들을 추가하는 메서드
n_numbers = [1, 2, 3]
n_numbers.extend([4, 5, 6])
print(n_numbers)


# += 연산자를 사용해서도 구현할 수도
n_numbers = [1, 2, 3]
n_numbers += [4, 5, 6]
print(n_numbers)


# 딕셔너리 초기화
empty_dict = {}
my_dict = {"cherry": 1, "banana": 2, "orange": 3}
print(my_dict)


# 딕셔너리 쌍 추가
my_dict = {"cherry": 1, "banana": 2, "orange": 3}
my_dict["grape"] = 4
print(my_dict)


# del: 딕셔너리에서 특정 요소를 삭제
my_dict = {"cherry": 1, "banana": 2, "orange": 3}
del my_dict["banana"]
print(my_dict)


# 딕셔너리에서 특정 Key에 해당하는 Value를 얻는 방법 (딕셔너리에 Key가 없는 경우, KeyError)
my_dict = {"cherry": 1, "banana": 2, "orange": 3}
print(my_dict["cherry"])


# keys: 딕셔너리에서 모든 Key를 리스트로 만들기
my_dict = {"cherry": 1, "banana": 2, "orange": 3}
key_list = list(my_dict.keys())
print(key_list)


# values: 딕셔너리에서 모든 Value를 리스트로 만들기
my_dict = {"cherry": 1, "banana": 2, "orange": 3}
value_list = list(my_dict.values())
print(value_list)


# items: 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
fairy = {"name": "cherry", "age": 27, "gender": "fairy"}
items = fairy.items()
print(items)


# clear: 딕셔너리의 모든 요소를 삭제
fairy = {"name": "cherry", "age": 27, "gender": "fairy"}
fairy.clear()
print(fairy)


# get: 딕셔너리에서 지정한 키에 대응하는 값을 반환 (딕셔너리에 Key가 없는 경우, None 반환)
fairy = {"name": "cherry", "age": 27, "gender": "fairy"}
name = fairy.get("name")
print(name)

email = fairy.get("email")
print(email)

email = fairy.get("email", "unknown")
print(email)

# request.POST['key']의 경우 값이 없으면 ValueError가 나옴
# request.POST.get('key')의 경우 값이 없으면 None을 반환함


# in: 해당 키가 딕셔너리 안에 있는지 확인
fairy = {"name": "cherry", "age": 27, "gender": "fairy"}
print("name" in fairy)
print("email" in fairy)
