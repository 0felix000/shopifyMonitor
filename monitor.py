import requests
import json
from dhooks import Webhook, Embed
from time import sleep
import random
import threading

f = open('settings.json')
data = json.load(f)
ping_on_startup = data['pingOnStartup']
url = data['webhook']
delay= int(data['delayMS'])/1000
def webhook(title,c,img):
    link = ""
    if url == "file":
        with open(str("webhooks.txt")) as f:
            lines = f.readlines()
            link = random.choice(lines).strip()
    else:
        link = url 
    hook = Webhook(link)
    embed = Embed(
    description=c,
    color=16763978,
    timestamp='now' 
    )
    embed.set_author(name=title)
    embed.set_thumbnail(img)
    embed.set_footer(text='0felix000 monitoring')
    r = hook.send(embed=embed)


def monitor(site,d):
    def output(x):
        x = site + " " + x
        return x

    proxies = {

    }
    old = {

    }
    def changeProxy():
        with open(str("proxies.txt")) as f:
            lines = f.readlines()
            proxie = random.choice(lines)
            print(output("using proxy " + proxie))
            ip = proxie.split(":")[0]
            port = proxie.split(":")[1].split(":")[0]
            username = proxie.split(":")[2].split(":")[0]
            password = proxie.split(":")[3].split(":")[0]
            proxies = {
            "http": f"http://{username}:{password}@{ip}:{port}/",
            "https": f"http://{username}:{password}@{ip}:{port}/",
            }
    changeProxy()
    delay = 3
    titles = []
    if ping_on_startup == "true":
        n = 1
    else:
        n = 0
    while 1 == 1:
        
        print(output("requesting product endpoint..."))
        r = requests.get("https://"+site+"/products.json", proxies = proxies )
        pwp = ""
        if(r.status_code == 200):
            print(output("Status 200, keeping proxy"))
        elif(r.status_code == 401):
            print(output("Detected password page, retrying..."))
            pwp = "true"
        else:
            print(output("detected ratlimit, switching proxies!"))
            changeProxy()
        data = {}
        if pwp == "":
            data = json.loads(r.text)
        if data != old and pwp == "":
            p = data["products"]
            for prod in p:
                title = prod["title"]
                handle = prod["handle"]
                v = prod["variants"]
                img = prod["images"]
                try:
                    img = img[0]["src"]
                except:
                    img = "https://cdn.discordapp.com/icons/916438652073173002/b29fa312928c23aeb39d741f5248cc12.webp?size=128"
                bs = "\s".replace("s","")
                img = img.replace(bs,"")
                if img in titles:
                    sleep(0)
                else:
                    if n != 0:
                        print(output("found new product!"))
                        titles.append(img)
                        c = ""
                        for id in v:
                            vid = id["id"]
                            size = id["title"]
                            if size == "Default Title":
                                size = "ATC"
                            c += "["+str(size)+"](https://"+site+"/cart/"+str(vid)+":1)" + " "
                        product = "[PRODUCTLINK](https://"+site+"/products/"+handle+")"
                        c += " | " + product
                        t = threading.Thread(target=webhook,args=("" + title,c,img))
                        t.start()

        n = 1
        old = data 
        sleep(delay)
sites = []
with open(str("sites.txt")) as f:
    sites = f.readlines()

for site in sites:
    t = threading.Thread(target=monitor,args=(site,"d"))
    t.start()
input()