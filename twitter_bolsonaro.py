import requests 
from bs4 import BeautifulSoup as bs

username = "jairbolsonaro"
n_tweets = 10

def scrape_tweets(username, n_tweets, url='https://twitter.com/'):
    # request data
    get_html = requests.get(url + username)
    content_type = get_html.headers['content-type'].split('/')[1].split(';')[0]
    html = get_html.content
    soup = bs(html, content_type)

    tweets = soup.find_all("div", {"class":"tweet"})
    for t in tweets[0:n_tweets]:
        post = t.find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
        print(post.text)
        
scrape_tweets(username, n_tweets)
