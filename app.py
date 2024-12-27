from flask import Flask, render_template, request  
import twitter_scraper  
import pymongo  
  
app = Flask(__name__)  
  
# Route to display scraped data  
@app.route("/")
def index():
    try:
        mongodb_uri = "mongodb://localhost:27017/"
        mongodb_db = "twitter_trends"
        mongodb_collection = "trends"

        client = pymongo.MongoClient(mongodb_uri)
        db = client[mongodb_db]
        collection = db[mongodb_collection]

        scraped_data = collection.find()
        return render_template("index.html", scraped_data=scraped_data)
    except Exception as e:
        return f"Error occurred: {e}"

# Route to run the Selenium script  
@app.route("/scrape", methods=["POST"])  
def scrape():  
   twitter_scraper.scrape_twitter_trends()  
   return "Scraping complete!"  
  
if __name__ == "__main__":  
   app.run(debug=True)