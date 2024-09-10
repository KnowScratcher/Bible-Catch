# this script will filer out God from the raw file
# 
# NOTE: please cd to Bible-Catch

import os

for i in os.listdir("1-out"):
    s = open(f"./1-out/{i}",encoding="UTF-8").readlines()
    constructor = ""
    for j in range(0,len(s),2):
        if "神" not in s[j] and "god" not in s[j+1].lower():
            constructor += s[j]+s[j+1]
    with open(f"./ok-out/{i}","w",encoding="UTF-8") as f:
        f.write(constructor)
