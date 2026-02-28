import re
import os

def check_password_strength(file_path):
    pattern = r"^(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?\":{}|<>]).{8,}$"

    # 1. Kiểm tra sự tồn tại của file
    if not os.path.exists(file_path):
        print(f"ỗi: Không tìm thấy file '{file_path}'.")
        return

    # 2. Kiểm tra file rỗng (0 byte)
    if os.path.getsize(file_path) == 0:
        print(f"Thông báo: File '{file_path}' hoàn toàn trống rỗng.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
           
            passwords = [line.strip() for line in file if line.strip()]

        if not passwords:
            print("Thông báo: File không chứa nội dung mật khẩu hợp lệ.")
            return

        valid_count = 0
        weak_count = 0

        print(f"{'Mật khẩu':<25} | {'Trạng thái':<10}")
        print("-" * 40)

        for pwd in passwords:
            if re.match(pattern, pwd):
                print(f"{pwd:<25} | Mạnh")
                valid_count += 1
            else:
                print(f"{pwd:<25} | Yếu")
                weak_count += 1

        # Thống kê cuối cùng
        print("-" * 40)
        print(f"Tổng kết: {valid_count} Mạnh, {weak_count} Yếu.")

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Thực thi
check_password_strength('passwords.txt')