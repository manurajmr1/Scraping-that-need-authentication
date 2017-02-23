import sys
import requests
import os
from lxml import html

USERNAME = ""
PASSWORD = ""

LOGIN_URL = "https://google.com/login"
URL = "https://google.com/users/SwedenAcademy/videos?page="

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]

    # Create payload
    payload = {
        "user[username]": USERNAME, 
        "user[password]": PASSWORD, 
        "authenticity_token": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    	
    f=open("videos.txt", "a+") 
    count = 1
    for i in range(8):
        # Each page
        result = session_requests.get(URL+str(i+1), headers = dict(referer = URL+str(i+1)))
        tree = html.fromstring(result.content)
        bucket_elems = tree.xpath("//a[@class='vButton vGrey vMicro']/@href")

        for elem in bucket_elems:        # Each video
            page = session_requests.get('https://google.com'+elem, headers = dict(referer = 'https://google.com'+elem))
            tree = html.fromstring(page.content)
            vid_links = tree.xpath("//a[contains(@href, 'http://download.google.com')]/@href")
            os.system('wget -O '+str(count)+'.mp4 "'+vid_links[0]+'"')
 	    count += 1
            #f.write(vid_links[0]+"\n")
            #print(vid_links)
     

    f.close()

if __name__ == '__main__':
    main()
