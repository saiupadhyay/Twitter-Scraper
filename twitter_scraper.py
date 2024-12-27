import os
import time
import pymongo
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv 

# Load environment variables from .env file
load_dotenv()
print(os.getenv("TWITTER_USERNAME"))

# Set up credentials and sensitive data using environment variables
proxy_mesh_api_key = os.getenv("PROXY_MESH_API_KEY")
twitter_username = os.getenv("TWITTER_USERNAME")
twitter_password = os.getenv("TWITTER_PASSWORD")
mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")  # Default fallback
mongodb_db = os.getenv("MONGODB_DB", "twitter_trends")
mongodb_collection = os.getenv("MONGODB_COLLECTION", "trends")

# Set up ProxyMesh
proxy_mesh_url = f"http://{proxy_mesh_api_key}@us.proxymesh.com:31280"

# Configure Chrome WebDriver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(f"--proxy-server={proxy_mesh_url}")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def scrape_twitter_trends():
    try:
        # Log in to Twitter
        driver.get("https://twitter.com/login")
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username_input.send_keys(twitter_username)
        username_input.send_keys(Keys.RETURN)

        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(twitter_password)
        password_input.send_keys(Keys.RETURN)

        # Navigate to home page
        WebDriverWait(driver, 10).until(EC.url_contains("https://twitter.com/home"))
        trending_topics = []

        # Scrape trending topics
        trending_topics_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@data-testid='trend']"))
        )
        for element in trending_topics_elements:
            topic_name = element.find_element(By.XPATH, ".//div[@dir='auto']").text
            trending_topics.append(topic_name)

        # Get the current IP address
        ip_address = requests.get("https://api.ipify.org").text

        # Insert data into MongoDB
        client = pymongo.MongoClient(mongodb_uri)
        db = client[mongodb_db]
        collection = db[mongodb_collection]
        collection.insert_one({
            "unique_id": time.time(),
            "trending_topics": trending_topics,
            "date_time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "ip_address": ip_address
        })
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error during scraping: {e}")
    finally:
        driver.quit()  # Ensure WebDriver is closed even if an error occurs

if __name__ == "__main__":
    scrape_twitter_trends()
