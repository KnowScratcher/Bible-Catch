# this script will get the bible from web
# and save it into 1-out folder
# 
# NOTE: please cd to Bible-Catch

import requests
from bs4 import BeautifulSoup
for chapter in range(1,51):
    raw = requests.get(f"https://o-bible.com/cgibin/ob.cgi?version=hb5&version=kjv&book=gen&chapter={chapter}",verify=False)
    raw.encoding = "Big5"
    html = BeautifulSoup(raw.text,"html.parser")

    ch = html.find_all("td",class_="v b5")
    en = html.find_all("td",class_="v en")
    if len(en) != len(ch) and input(f"資料長度不對，確定要繼續(en={len(en)},ch={len(ch)})?[y/N]") != "y":
        exit()

    s = ""
    for i in range(len(en)):
        s += ch[i].get_text().replace(" ","")+"\n"
        s += en[i].get_text()+"\n"
    with open(f"./1-out/{chapter}.txt","w",encoding="UTF-8") as f:
        f.write(s)