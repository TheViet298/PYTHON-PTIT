# Hệ mật mã Caesar : dịch k ký tự , check phạm vi ký tự từ 0 -> 25
text = input() #Nhận đoạn văn bản rõ
k = int(input()) # Nhận khóa nhập vào từ bàn phím, ép kiểu về số nguyên

# duyệt qua toàn bộ chuỗi kí tự đầu vào 
# quy tắc mã hóa caesar : c = ( x + k)% 26
# hàm ord : xác định vị trí của ký tự trong unicode
# hàm chr : xác định ký tự dựa vào chỉ số mã ascii
res = ""
for i in range(len(text)): # duyệt chỉ số
  # tính vị trí / chỉ số của ký tự trong phạm vi 0 - 25
  if text[i] >= 'A' and text[i] <= 'Z': # chữ cái in hoa
    res = res + chr((ord(text[i]) - 65 + k) % 26 + 65) # tính phạm vi không vượt quá 25 ký tự
  elif text[i] >= 'a' and text[i] <= 'z': # chữ in thường 
    res = res + chr((ord(text[i]) - 97 + k) % 26 + 97) # tương tự trên
  else: # giữ nguyên\
    res = res + text[i]
print(res)