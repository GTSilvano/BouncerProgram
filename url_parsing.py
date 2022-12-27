from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse


parser = argparse.ArgumentParser(description='extract headers')
parser.add_argument('url_link')
args = parser.parse_args()

link = args.url_link

html = urlopen(link)
bs = BeautifulSoup(html, "html.parser")
heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
for tags in bs.find_all(heading_tags):
    if tags.text.strip() =="Best VPN for Search Engines" or tags.text.strip() == "Best VPN Deal! Get HideIPVPN for $2.7/mo!":
        continue
    print(tags.name + ' -> ' + tags.text.strip())
