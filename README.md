# TTS - 01 - Open Vibe Coding Challenge

## Đề bài: Một script tự động kiểm tra xem độ mạnh của các mật khẩu trong một file text nhập vào có đạt chuẩn hay không.
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

---

## TÀI LIỆU KIẾN TRÚC DỰ ÁN

**1. Vấn đề giải quyết**
    
Trong môi trường an ninh mạng hiện nay, mật khẩu yếu là kẽ hở lớn nhất dẫn đến các cuộc tấn công Brute-force hoặc Dictionary Attack.

* Thách thức: Người dùng có xu hướng đặt mật khẩu dễ nhớ nhưng không an toàn. Việc kiểm tra thủ công hàng trăm, hàng ngàn mật khẩu trong hệ thống quản trị là bất khả thi và tốn thời gian.

* Mục tiêu: Xây dựng một công cụ tự động hóa việc rà soát và phân loại mật khẩu theo các tiêu chuẩn bảo mật hiện đại (độ dài, ký tự đặc biệt, số, chữ hoa/thường). Phục vụ cho việc mã hóa mật khẩu một cách an toàn, khó bị hacker tấn công.


**2. Tech Stack & Công cụ sử dụng**

* Ngôn ngữ Python 3.10+: Lựa chọn vì sự phổ biến, thư viện xử lý chuỗi mạnh mẽ và không cần cài đặt phức tạp (Zero-dependency).

* Thư viện chuẩn re (Regex): Sử dụng biểu thức chính quy để đối soát mẫu nhanh chóng và chính xác. Đây là công cụ tối ưu nhất để xử lý các quy tắc logic phức tạp trong mật khẩu.

* Thư viện chuẩn os: Dùng để kiểm tra sự tồn tại và trạng thái của file vật lý trước khi xử lý, đảm bảo tính bền vững (robustness) của script.

* AI (Gemini): Đóng vai trò "Pair Programmer" để tối ưu hóa các chuỗi Regex khó và thiết kế giao diện bảng (table) trên terminal.

* Note: Sử dụng thư viện re để hiểu cách thức hoạt động của Regex và tận dụng cho các quá trình phân tích log,... trong hoạt động bảo mật sau này.

**3.Luồng hoạt động chính (Workflow)**

Chương trình hoạt động theo một luồng tuyến tính (Linear Flow) để đảm bảo hiệu suất cao nhất:

**Mô tả chi tiết flow:**

* Input: Người dùng cung cấp đường dẫn file mật khẩu (mặc định là passwords.txt).

* Validation: Script kiểm tra file có tồn tại không? Có rỗng (0 byte) không? Nếu lỗi, thông báo ngay cho người dùng.

* Preprocessing: Đọc từng dòng, sử dụng phương thức .strip() để loại bỏ khoảng trắng dư thừa và loại bỏ các dòng trống.

* Core Logic (Regex): Áp dụng pattern: 

                                    ^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<> ]).{8,}$

                                    (?=.*[a-z]): Ít nhất một chữ thường.

                                    (?=.*[A-Z]): Ít nhất một chữ in hoa.

                                    (?=.*[0-9]): Ít nhất một chữ số.

                                    (?=.*[!@...]): Ít nhất một ký tự đặc biệt.

                                    .{8,}: Độ dài tối thiểu 8 ký tự.

* Output: Hiển thị kết quả dưới dạng bảng ngay trên Console và in tổng kết số lượng mật khẩu Mạnh/Yếu.

---

## Nhật ký "Vibe Coding"

Link AI: 

        https://gemini.google.com/share/6b87545e6752

---
## Video Demo
Link video:

        https://drive.google.com/file/d/1PR11xeiPzVxuSBePmrz62g_aVn8iYwrr/view?usp=sharing