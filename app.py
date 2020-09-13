import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)


@app.route("/<name>")
def instagramProfile(name):
    url = "https://www.instagram.com/"+name
    x = requests.get(url)
    soup = BeautifulSoup(x.text, "lxml")

    r = soup.body.script.contents[0]
    start = r.index("profile_pic_url_hd")
    rawText = r[start + 21:]
    end = rawText.index('"')
    instUrl = rawText[:end]
    newUrl = instUrl.replace("\\u0026", "&")
    return newUrl

if __name__ == "__main__":
    app.run()