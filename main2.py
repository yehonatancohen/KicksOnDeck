from bs4 import BeautifulSoup
from puppeteer import launch

# Read the list of proxies from the "proxies.txt" file
with open("proxies.txt") as f:
  proxies = f.read().splitlines()

# Loop through the list of proxies
for proxy in proxies:
  # Launch Puppeteer with the specified proxy
  browser = launch(args=["--proxy-server=" + proxy])
  page = browser.newPage()

  # Open the Nike website and navigate to the shoe page
  page.goto("https://www.nike.com/il/launch/")
  shoe_link = page.find_by_text("Nike Air Zoom Pegasus 37")
  shoe_link.click()

  # Select the shoe size and add it to the cart
  size_dropdown = page.find_by_id("size")
  size_dropdown.click()
  size_option = page.find_by_xpath("//option[@value='9.5']")
  size_option.click()
  add_to_cart_button = page.find_by_id("add-to-cart")
  add_to_cart_button.click()

  # Fill in the checkout form with random information
  page.goto("https://www.nike.com/il/checkout")
  first_name_input = page.find_by_id("firstName")
  first_name_input.fill("John")
  last_name_input = page.find_by_id("lastName")
  last_name_input.fill("Doe")
  email_input = page.find_by_id("email")
  email_input.fill("johndoe@example.com")
  phone_input = page.find_by_id("phoneNumber")
  phone_input.fill("1234567890")
  address_input = page.find_by_id("address")
  address_input.fill("123 Main Street")
  city_input = page.find_by_id("city")
  city_input.fill("City")
  state_input = page.find_by_id("state")
  state_input.fill("State")
  zip_input = page.find_by_id("zip")
  zip_input.fill("12345")

  # Submit the checkout form
  submit_button = page.find_by_id("submit")
  submit_button.click()

  # Close the browser
  browser.close()
