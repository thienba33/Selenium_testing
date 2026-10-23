# Kiểm thử tự động bằng Selenium

Thực hành 6 test case trên [SauceDemo](https://www.saucedemo.com/) bằng Python, Selenium WebDriver và pytest:

- Đăng nhập thành công.
- Đăng nhập sai mật khẩu.
- Thêm sản phẩm vào giỏ hàng.
- Xóa sản phẩm khỏi giỏ hàng.
- Hoàn tất đặt hàng.
- Đăng xuất và kiểm tra truy cập lại trang sản phẩm.

## Cài đặt

Yêu cầu: Python 3.10+, Google Chrome và Internet. Selenium tự tải driver phù hợp khi chạy lần đầu.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Trên Windows, tạo môi trường bằng `py -m venv .venv`, kích hoạt bằng `.\.venv\Scripts\Activate.ps1`, rồi cài thư viện như trên.

## Chạy

```bash
python -m pytest            # Chạy không mở cửa sổ Chrome
python -m pytest --headed   # Mở Chrome để quan sát
```

Mỗi test dùng một phiên Chrome riêng. Kết quả được lưu ở `reports/report.html`, ảnh minh chứng ở `reports/screenshots/`. Báo cáo được cập nhật mỗi lần chạy; đính kèm thư mục `reports` khi nộp bài.

## Tài liệu bài tập

- [Đặc tả 6 test case](docs/TEST_CASES.md).
- [Báo cáo thực hành](docs/BAO_CAO.md)
- Mã kiểm thử: `tests/test_saucedemo.py`; cấu hình trình duyệt và chụp ảnh: `tests/conftest.py`.

