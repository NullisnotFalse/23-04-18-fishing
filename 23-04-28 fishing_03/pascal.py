# 재귀함수 사용
def pascal(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        last_line = pascal(n - 1)
        line = [1] * n
        for i in range(1, n - 1):
            line[i] = last_line[i - 1] + last_line[i]
        return line


print(pascal(10))


# 파스칼의 삼각형을 출력하는 함수
def pascal_01(n):
    base_list = [1]
    print_list = []
    print(1)
    count = 2
    while count <= n:
        count += 1
        base_list = print_list
        print_list = []
        print_list.append(1)
        if len(base_list) > 1:
            for i in range(1, len(base_list)):
                add_num = base_list[i] + base_list[i - 1]
                print_list.append(add_num)
        print_list.append(1)
        print(*print_list)


# pascal_01(11)


# n번째 줄의 리스트를 return하는 함수
def pascal_02(n):
    base_list = [1]
    print_list = []
    if n == 1:
        return base_list
    count = 2
    while count <= n:
        count += 1
        base_list = print_list
        print_list = []
        print_list.append(1)
        if len(base_list) > 1:
            for i in range(1, len(base_list)):
                add_num = base_list[i] + base_list[i - 1]
                print_list.append(add_num)
        print_list.append(1)
    return print_list


# print(pascal_02(12))
