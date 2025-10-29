# Overview

The Twitter Scraper is a Python + Streamlit web application that allows users to scrape live tweets from Twitter without using the official API. It provides a simple and interactive interface to extract real-time tweets, hashtags, and trends directly from Twitter using Selenium automation and ProxyMesh for smooth and reliable access.

This project eliminates the limitations of API rate limits and token restrictions, enabling dynamic tweet analysis without storing data in a database — ideal for real-time data visualization or research.

🚀 Features

✅ Real-Time Scraping: Fetches live tweets dynamically using Selenium.
✅ API-Free Access: Bypasses the need for Twitter API keys and rate limits.
✅ Proxy Integration: Uses ProxyMesh to handle requests anonymously and avoid IP blocks.
✅ Secure Credential Handling: Environment variables managed through .env and python-dotenv.
✅ Live Display on Streamlit: Shows scraped tweets instantly on button click — no database needed.
✅ Optional MongoDB Support: Connection setup for storing tweets or trends if persistence is required.

🧠 Problem It Solves

Traditional Twitter APIs impose strict limits on data access, requiring authentication keys and offering limited request counts.
This project solves that problem by:

Allowing developers and analysts to instantly extract tweets without waiting for API approvals.

Helping marketers, researchers, or journalists analyze live trends directly from Twitter in real-time.

Providing a lightweight, front-end-driven solution that displays scraped data instantly — no complex backend setup required.

# Tech Stack

Language: Python

Frontend: Streamlit

Automation: Selenium WebDriver, ChromeDriverManager

Proxy Handling: ProxyMesh

Environment Management: Python-dotenv

Database (optional): MongoDB (via PyMongo)

# How It Works

Loads credentials (Twitter username, password, proxy keys) from .env file.

Configures a Selenium WebDriver with ProxyMesh for anonymous access.

Automates login and scraping from Twitter.

Displays the scraped tweets live in the Streamlit interface (on button click).

Optionally connects to MongoDB for data storage.

📂 Project Structure
twitter-scraper/
│
├── main.py                 # Core scraper logic (Selenium + Proxy)
├── app.py                  # Streamlit interface for live display
├── .env                    # Environment variables (Twitter & proxy creds)
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

# Installation & Setup
# Clone this repository
git clone https://github.com/your-username/twitter-scraper.git
cd twitter-scraper

# Install dependencies
pip install -r requirements.txt

 Create a .env file
 Add your credentials like:
 TWITTER_USERNAME=your_username
 TWITTER_PASSWORD=your_password
 PROXY_MESH_API_KEY=your_key
 MONGODB_URI=your_mongo_uri (optional)

# Run the Streamlit app
streamlit run app.py

🧩 Future Improvements

Add keyword-based tweet filtering.

Integrate sentiment analysis for live tweets.

Enhance UI with charts for tweet frequency & engagement metrics.

Deploy on Streamlit Cloud or Render for public access.

✨ Author

Sai Upadhyay
