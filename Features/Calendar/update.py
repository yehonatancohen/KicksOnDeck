# Import the required modules
import requests
import hashlib
import time

# Set the URL of the website to check
url = "https://www.example.com"

# Set the time interval for checking the website (in seconds)
interval = 60

# Set the initial content hash to an empty string
prev_content_hash = ""

# Loop indefinitely
while True:
    # Use the requests module to make an HTTP GET request to the URL
    response = requests.get(url)

    # Calculate the hash of the response content
    content_hash = hashlib.sha256(response.content).hexdigest()

    # Check if the content hash is different from the previous content hash
    if content_hash != prev_content_hash:
        # The website has been updated
        print(f"{time.ctime()}: The website has been updated!")

        # Set the previous content hash to the current content hash
        prev_content_hash = content_hash
    else:
        # The website has not been updated
        print(f"{time.ctime()}: The website has not been updated.")

    # Sleep for the specified time interval
    time.sleep(interval)
