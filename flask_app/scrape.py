from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Specify the URL of the Seeking Alpha page you want to scrape
url = 'https://seekingalpha.com/market-news/top-news'

# Initialize the Selenium webdriver (make sure to have the appropriate driver executable in your PATH)
driver = webdriver.Chrome()

# Navigate to the desired page
driver.get(url)

# Wait for the page to load (adjust the sleep duration as needed)
time.sleep(5)

# Find the elements containing the company information
company_elements = driver.find_elements(By.CSS_SELECTOR, '.mc-list-item')

# Create a list to store the company names
company_names = []

# Extract the company names from the elements
for element in company_elements:
    company_names.append(element.text)

# Get only the top 10 company names
top_10_companies = company_names[:10]

# Print the top 10 company names
for company in top_10_companies:
    print(company)

# Close the browser
driver.quit()
