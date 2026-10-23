# Báo cáo thực hành Selenium


## 1. Mục tiêu và công cụ

Tìm hiểu Selenium và xây dựng tối thiểu 5 test case tự động cho một website. Bài thực hành sử dụng [SauceDemo](https://www.saucedemo.com/) và triển khai 6 test case.

- **Selenium WebDriver:** điều khiển Chrome, tìm phần tử, nhập dữ liệu và nhấn nút.
- **pytest:** tổ chức test, khởi tạo trình duyệt riêng qua fixture và kiểm tra kết quả bằng `assert`.
- **pytest-html:** tạo báo cáo HTML kèm ảnh minh chứng.

Tài liệu tự học được liên kết trong [README](../README.md#tự-học).

## 2. Thiết kế và thực hiện

Điều kiện, dữ liệu, các bước và kết quả mong đợi của từng test được trình bày trong [TEST_CASES.md](TEST_CASES.md).

Mã nguồn nằm ở `tests/test_saucedemo.py`. Mỗi test dùng một phiên Chrome riêng và tự chuẩn bị trạng thái cần thiết. `WebDriverWait` chờ phần tử trước khi thao tác; `assert` kiểm tra URL, thông báo hoặc dữ liệu sản phẩm. `tests/conftest.py` khởi tạo, đóng trình duyệt và chụp ảnh kết quả.

Tài khoản demo: `standard_user` / `secret_sauce`. Trường hợp đăng nhập sai sử dụng `wrong_password`. Đặt hàng dùng dữ liệu giả lập `Sinh`, `Vien`, `700000`.

## 3. Kết quả

Lần chạy ngày **23/10/2026** trên Linux, Python 3.14.4, Chrome 156.0.8078.47, Selenium 4.51.0, pytest 9.1.1 và pytest-html 4.2.0, ở chế độ headless:

| Mã | Kịch bản | Kết quả |
| --- | --- | --- |
| TC01 | Đăng nhập đúng tài khoản | Pass |
| TC02 | Đăng nhập sai mật khẩu | Pass |
| TC03 | Thêm sản phẩm vào giỏ | Pass |
| TC04 | Xóa sản phẩm khỏi giỏ | Pass |
| TC05 | Hoàn tất đặt hàng | Pass |
| TC06 | Đăng xuất và kiểm tra chặn truy cập inventory | Pass |

Minh chứng: [báo cáo HTML](../reports/report.html) và [thư mục ảnh](../reports/screenshots/). Chạy lại bằng `python -m pytest` để cập nhật kết quả. Thư mục `reports` không được theo dõi bằng Git; cần đính kèm khi nộp bài.

## 4. Nhận xét

Bộ kiểm thử đáp ứng yêu cầu với 6 test độc lập, có kiểm tra kết quả và ảnh minh chứng. Phạm vi hiện tại là các chức năng cơ bản trên Chrome; kết quả còn phụ thuộc mạng và website demo. Có thể mở rộng bằng test thông tin đặt hàng bỏ trống hoặc chạy trên trình duyệt khác.
