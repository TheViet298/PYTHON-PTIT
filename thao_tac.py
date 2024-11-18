# Định dạng đầu vào
# 9
# append 1
# append 2
# append 3
# insert 3 1
# print
# insert 4 3
# pop
# sort
# print

n = int(input())  # Đọc số lượng thao tác từ đầu vào

my_list = []  # Khởi tạo một danh sách rỗng
# duyệt for , nhập và tách từ 
# đọc đến đâu check thao tác đến đó
for _ in range(n):
    command = input().split()  # Đọc lệnh và các tham số từ đầu vào
    action = command[0]

    if action == 'append':
        element = int(command[1])
        my_list.append(element)
    elif action == 'insert':
        index = int(command[1])
        element = int(command[2])
        my_list.insert(index, element)
    elif action == 'remove':
        i = int(command[1])
        my_list.remove(index)
    elif action == 'print':
        print(my_list)
    elif action == 'pop':
        my_list.pop()
    elif action == 'sort':
        my_list.sort()
    elif action == 'reverse':
        my_list.reverse()

# Kết thúc chương trình
