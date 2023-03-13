import requests
from bs4 import BeautifulSoup

# specify the URL of the website to scrape
url = "https://www.flaticon.com/free-icon/front-end_2721616"

# send an HTTP GET request to the website
response = requests.get(url)


# parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# find all the <img> tags and get their "src" attribute value
img_src_list = [img["src"] for img in soup.find_all("img")]

# find all the <video> tags and get their "src" attribute value
video_src_list = [video["src"] for video in soup.find_all("video")]

# create a list of all the source URLs
source_urls = img_src_list + video_src_list

# create a text file and write the source URLs to it
with open("source_urls.txt", "w") as f:
    for url in source_urls:
        f.write(url + "\n")

# print a message indicating the file has been saved
print("Source URLs saved to source_urls.txt.")

    
