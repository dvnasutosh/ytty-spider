import os
import platform
import requests
import zipfile

# Determine the platform (Windows, Mac, Linux)
platform_name = platform.system()

# URL to download the ChromeDriver executable
chrome_driver_url = "https://chromedriver.storage.googleapis.com/109.0.5414.74/chromedriver{}.zip".format(platform_name.lower())


# Download the ChromeDriver executable
response = requests.get(chrome_driver_url)
open("chromedriver.zip", "wb").write(response.content)

# Extract the ChromeDriver executable from the ZIP file
with zipfile.ZipFile("chromedriver.zip", "r") as zip_ref:
    zip_ref.extractall(".")

# Delete the ZIP file
os.remove("chromedriver.zip")

# Make the ChromeDriver executable file executable
os.chmod("chromedriver", 0o755)

print("ChromeDriver has been successfully downloaded and extracted.")
