from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


PRODUCT = "Sauce Labs Backpack"


def visible(driver, selector):
    return WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
    )


def click(driver, selector):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    ).click()


def login(driver, base_url, password="secret_sauce"):
    driver.get(base_url + "/")
    visible(driver, "[data-test='username']").send_keys("standard_user")
    visible(driver, "[data-test='password']").send_keys(password)
    click(driver, "[data-test='login-button']")


def open_cart_with_product(driver, base_url):
    login(driver, base_url)
    click(driver, "[data-test='add-to-cart-sauce-labs-backpack']")
    click(driver, ".shopping_cart_link")
    visible(driver, ".cart_item")


def test_tc01_login_success(driver, base_url):
    login(driver, base_url)
    assert visible(driver, ".title").text == "Products"
    assert driver.current_url == base_url + "/inventory.html"
    assert driver.find_elements(By.CSS_SELECTOR, ".inventory_item")


def test_tc02_login_wrong_password(driver, base_url):
    login(driver, base_url, password="wrong_password")
    error = visible(driver, "[data-test='error']")
    assert "Username and password do not match any user in this service" in error.text
    assert driver.current_url == base_url + "/"
    assert visible(driver, "[data-test='login-button']").is_displayed()


def test_tc03_add_product_to_cart(driver, base_url):
    login(driver, base_url)
    item = visible(driver, ".inventory_item")
    assert item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == PRODUCT
    expected_price = item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
    click(driver, "[data-test='add-to-cart-sauce-labs-backpack']")
    assert visible(driver, ".shopping_cart_badge").text == "1"
    click(driver, ".shopping_cart_link")
    cart_item = visible(driver, ".cart_item")
    assert len(driver.find_elements(By.CSS_SELECTOR, ".cart_item")) == 1
    assert cart_item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == PRODUCT
    assert cart_item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text == expected_price
    assert cart_item.find_element(By.CSS_SELECTOR, ".cart_quantity").text == "1"


def test_tc04_remove_product_from_cart(driver, base_url):
    open_cart_with_product(driver, base_url)
    assert visible(driver, ".inventory_item_name").text == PRODUCT
    click(driver, "[data-test='remove-sauce-labs-backpack']")
    WebDriverWait(driver, 15).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".cart_item")))
    assert driver.find_elements(By.CSS_SELECTOR, ".cart_item") == []
    assert driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge") == []


def test_tc05_checkout_success(driver, base_url):
    open_cart_with_product(driver, base_url)
    click(driver, "[data-test='checkout']")
    visible(driver, "[data-test='firstName']").send_keys("Sinh")
    visible(driver, "[data-test='lastName']").send_keys("Vien")
    visible(driver, "[data-test='postalCode']").send_keys("700000")
    click(driver, "[data-test='continue']")
    assert visible(driver, ".title").text == "Checkout: Overview"
    assert visible(driver, ".inventory_item_name").text == PRODUCT
    assert visible(driver, ".cart_quantity").text == "1"
    click(driver, "[data-test='finish']")
    assert visible(driver, "[data-test='complete-header']").text == "Thank you for your order!"
    assert driver.current_url == base_url + "/checkout-complete.html"
    assert driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge") == []


def test_tc06_logout(driver, base_url):
    login(driver, base_url)
    visible(driver, ".inventory_list")
    click(driver, "#react-burger-menu-btn")
    click(driver, "[data-test='logout-sidebar-link']")
    assert visible(driver, "[data-test='login-button']").is_displayed()
    assert driver.current_url == base_url + "/"
    driver.get(base_url + "/inventory.html")
    assert "You can only access '/inventory.html' when you are logged in." in visible(driver, "[data-test='error']").text
    assert driver.current_url == base_url + "/"
