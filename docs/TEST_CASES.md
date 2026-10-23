# Đặc tả test case

Website: https://www.saucedemo.com/. Trình duyệt: Chrome. Mỗi test dùng phiên trình duyệt mới; không chia sẻ cookie hay giỏ hàng. Kết quả thực tế được ghi trong báo cáo pytest, không điền sẵn Pass vào bảng thiết kế.

## TC01 — Đăng nhập thành công

- **Điều kiện:** ở trang đăng nhập, chưa đăng nhập.
- **Dữ liệu:** `standard_user` / `secret_sauce`.
- **Các bước:** nhập username → nhập password → nhấn Login.
- **Mong đợi:** URL `/inventory.html`, tiêu đề `Products`, có danh sách sản phẩm.
- **Mã nguồn:** `test_tc01_login_success`.

## TC02 — Đăng nhập sai mật khẩu

- **Điều kiện:** ở trang đăng nhập, chưa đăng nhập.
- **Dữ liệu:** `standard_user` / `wrong_password`.
- **Các bước:** nhập tài khoản → nhập mật khẩu sai → nhấn Login.
- **Mong đợi:** thông báo chứa `Username and password do not match any user in this service`; URL vẫn là trang gốc; nút Login vẫn hiển thị.
- **Mã nguồn:** `test_tc02_login_wrong_password`.

## TC03 — Thêm sản phẩm vào giỏ hàng

- **Điều kiện:** đăng nhập hợp lệ, giỏ trống.
- **Dữ liệu:** `Sauce Labs Backpack`; giá hiển thị ở danh sách sản phẩm làm giá đối chiếu.
- **Các bước:** ghi nhận tên và giá → nhấn Add to cart của Backpack → kiểm tra huy hiệu giỏ → mở giỏ.
- **Mong đợi:** huy hiệu `1`; giỏ chỉ có một dòng, đúng tên và giá đã ghi nhận, số lượng `1`.
- **Mã nguồn:** `test_tc03_add_product_to_cart`.

## TC04 — Xóa sản phẩm khỏi giỏ

- **Điều kiện:** đăng nhập hợp lệ; tự thêm một Backpack và mở giỏ trong chính test này.
- **Dữ liệu:** `Sauce Labs Backpack`.
- **Các bước:** xác nhận sản phẩm có trong giỏ → nhấn Remove.
- **Mong đợi:** không còn dòng sản phẩm; huy hiệu số lượng biến mất.
- **Mã nguồn:** `test_tc04_remove_product_from_cart`.

## TC05 — Hoàn tất đặt hàng

- **Điều kiện:** đăng nhập hợp lệ; tự thêm một Backpack và mở giỏ trong chính test này.
- **Dữ liệu:** First Name `Sinh`, Last Name `Vien`, Zip/Postal Code `700000`.
- **Các bước:** Checkout → nhập thông tin → Continue → kiểm tra Overview, sản phẩm và số lượng → Finish.
- **Mong đợi:** Overview chứa Backpack với số lượng `1`; sau Finish, URL `/checkout-complete.html`, thông báo `Thank you for your order!`, không còn huy hiệu giỏ.
- **Mã nguồn:** `test_tc05_checkout_success`.

## TC06 — Đăng xuất

- **Điều kiện:** đăng nhập thành công bằng tài khoản hợp lệ.
- **Dữ liệu:** URL trang bảo vệ `/inventory.html`.
- **Các bước:** mở menu → Logout → kiểm tra trang đăng nhập → truy cập trực tiếp inventory.
- **Mong đợi:** sau Logout về trang gốc có nút Login; truy cập trực tiếp bị chuyển về trang đăng nhập và có lỗi chứa `You can only access '/inventory.html' when you are logged in.`.
- **Mã nguồn:** `test_tc06_logout`.
