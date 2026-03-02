import re
import os

def check_password_strength(file_path):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?\":{}|<> ]).{8,}$"

    if not os.path.exists(file_path):
        print(f"Lỗi: Không tìm thấy file '{file_path}'.")
        return

    if os.path.getsize(file_path) == 0:
        print(f"Thông báo: File '{file_path}' hoàn toàn trống.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
           
            passwords = [line.rstrip('\n').rstrip('\r') for line in file]

        if not passwords:
            print("Thông báo: File không chứa nội dung mật khẩu hợp lệ.")
            return

        valid_count = 0
        weak_count = 0

        print(f"{'Mật khẩu':<25} | {'Độ dài':<6} | {'Trạng thái':<10}")
        print("-" * 40)

        for pwd in passwords:
            if re.match(pattern, pwd):
                print(f"{pwd:<25} | {len(pwd):<6} | Mạnh")
                valid_count += 1
            else:
                print(f"{pwd:<25} | {len(pwd):<6} | Yếu")
                weak_count += 1

        print("-" * 40)
        print(f"Tổng kết: {valid_count} Mạnh, {weak_count} Yếu.")

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

check_password_strength('passwords.txt')