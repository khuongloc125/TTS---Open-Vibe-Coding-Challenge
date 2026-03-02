# TTS - 01 - Open Vibe Coding Challenge

## Đề bài: Một script tự động kiểm tra xem độ mạnh của các mật khẩu trong một file text nhập vào có đạt chuẩn hay không.
---

## Vấn đề giải quyết
    
Người dùng thường có xu hướng đặt mật khẩu đơn giản, dễ nhớ nhưng lại dễ bị tấn công. Việc kiểm tra thủ công hàng trăm tài khoản là bất khả thi. Script này tự động hóa quy trình đó bằng các bộ lọc Regex chính xác qua đó tiếp cận và làm quen với Regex cho việc phân tích sau này.

---
## Hướng dẫn cài đặt và sử dụng

**1. Chuẩn bị môi trường**

* Đảm bảo máy đã cài đặt Python 3.x.

* Clone repository này về máy.

* Mở Terminal (hoặc CMD/PowerShell)

        git clone https://github.com/khuongloc125/TTS---Open-Vibe-Coding-Challenge.git

**2. Dữ liệu đầu vào**

* Có thể sửa nội dung file passwords.txt hoặc để nguyên và chạy luôn.

**3. Cách chạy dự án**

* Mở Terminal (hoặc CMD/PowerShell) tại thư mục dự án và chạy lệnh:

    python checkpw.py

**4. Kết quả kỳ vọng**

* Chương trình sẽ hiển thị bảng thống kê trực quan ngay trên màn hình:

        Mật khẩu                  | Độ dài | Trạng thái

        ------------------------------------------------

        xxxxxxxxxxxxx             | x      | Mạnh

        xxxxxxxxxxxxx             | x      | yếu

        ------------------------------------------------
         Tổng kết: 1 Mạnh, 1 Yếu.