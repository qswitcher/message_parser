import re
import json
import sys
import urllib2
from BeautifulSoup import BeautifulSoup

def parse(raw):
    message = {}
    mentions = re.findall('@(\w+)', raw)
    if len(mentions) > 0:
        message['mentions'] = mentions

    emoticons = re.findall('\(([a-zA-Z0-9]{1,15})\)', raw)
    if len(emoticons) > 0:
        message['emoticons'] = emoticons

    urls = re.findall('https?:\/\/\S+', raw)

    if len(urls) > 0:
        links = []
        message['links'] = links

        for url in urls:
            title = ''
            try:
                source = urllib2.urlopen(url)
                BS = BeautifulSoup(source)
                title = BS.find('title').text
            except urllib2.HTTPError:
                pass
            links.append({'url': url, 'title': title})

    return json.dumps(message, sort_keys=True, indent=4, separators=(',', ':'))   

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print parse(sys.argv[2])
    else:
        print "Example 1 ===================="
        print parse("@chris you around?")
        print "Example 2 ===================="
        print parse("Good morning! (megusta) (coffee)")
        print "Example 3 ===================="
        print parse("Olympics are starting soon; http://www.nbcolympics.com")
        print "Example 4 ===================="
        print parse("@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016")


