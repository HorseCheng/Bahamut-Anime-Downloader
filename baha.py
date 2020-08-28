# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
import requests
import re
import os
import natsort
import shutil
import time

cookie=""
with open ("cookie.txt",'r') as f:
    cookie=f.read().strip("\n")
if cookie=="":
    print("請記得將cookie填寫至cookie.txt\n") 
    import sys
    sys.exit()

sninput=input("請輸入指令+想下載的動畫sn號碼: \n\
    -a 下載當季所有動畫(all)\n\
    -b 下載當季第一集至該集動畫(beginning)\n\
    -e 下載當季該集至最後一集動畫(end)\n\
    -o 只下載該集動畫(one)\n\
    -m 後面接續多個該季其他想下載的集數(後面請以空白做區隔)(multiple)\n\
    範例:\n\
    -b 16870\n\
    -m 16870 37 38 39\n")
sn=re.findall("[0-9]+",sninput)[0]

headers={"sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","dnt":"1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}   
headers["cookie"] = cookie 
headers["origin"] ="https://ani.gamer.com.tw"
headers["referer"] = f"https://ani.gamer.com.tw/animeVideo.php?sn={sn}"

finder=requests.get(f"https://ani.gamer.com.tw/animeVideo.php?sn={sn}",headers=headers)
downloadlist=re.findall('<a href="\?sn=(.*?)">.*?</a>', finder.text)
if(downloadlist==[]): downloadlist=[sn]
namelist=re.findall('<a href="\?sn=.*?">(.*?)</a>', finder.text)

index=downloadlist.index(sn)

if ("-a" in sninput):
    downloadlist = downloadlist
elif ("-b" in sninput):
    downloadlist = downloadlist[0:index+1]
elif ("-e" in sninput):
    downloadlist = downloadlist[index:]
elif ("-m" in sninput):
    temp=[sn]
    inputs=re.findall("[0-9.]+",sninput)[1:]
    for i in inputs:
        temp.append(downloadlist[namelist.index(i)])
    downloadlist = temp
else:
    downloadlist = [ downloadlist[index] ]

downloadlist = list(sorted(set(downloadlist)))
print(f"一共有 {len(downloadlist)} 集需要下載")
print(f"下載清單(sn): {downloadlist}")

deviceid= requests.get("https://ani.gamer.com.tw/ajax/getdeviceid.php",headers=headers).json()["deviceid"]

times=0
reschoice=-1 #Download highest resolution
for times, i in enumerate(downloadlist):
    sn=i
    html=requests.get(f"https://ani.gamer.com.tw/animeVideo.php?sn={sn}",headers=headers)
    filename=re.findall("<title>(.*) 線上看 - 巴哈姆特動畫瘋</title>" , html.text)[0]
    print(f"\n即將下載... {sn}: '{filename}'")

    vip=requests.get(f"https://ani.gamer.com.tw/ajax/token.php?adID=0&sn={sn}&device={deviceid}",headers=headers).json()["vip"]
    
    requests.get(f"https://ani.gamer.com.tw/ajax/unlock.php?sn={sn}&ttl=0",headers=headers) #unlock
    requests.get(f"https://ani.gamer.com.tw/ajax/checklock.php?device={deviceid}&sn={sn}",headers=headers) #checklock

    if(not vip ):
        print("等待 30 秒 廣告時間中...")
        requests.get(f"https://ani.gamer.com.tw/ajax/unlock.php?sn={sn}&ttl=0",headers=headers) #unlock
        requests.get(f"https://ani.gamer.com.tw/ajax/unlock.php?sn={sn}&ttl=0",headers=headers) #unlock
        requests.get(f"https://ani.gamer.com.tw/ajax/videoCastcishu.php?sn={sn}&s=194699",headers=headers)
        time.sleep(10)
        requests.get(f"https://ani.gamer.com.tw/ajax/unlock.php?sn={sn}&ttl=0",headers=headers) #unlock
        requests.get(f"https://ani.gamer.com.tw/ajax/unlock.php?sn={sn}&ttl=0",headers=headers) #unlock
        time.sleep(20)  
        requests.get(f"https://ani.gamer.com.tw/ajax/videoCastcishu.php?sn={sn}&s=194699&ad=end",headers=headers)
    time.sleep(1)  
    requests.get(f"https://ani.gamer.com.tw/ajax/videoStart.php?sn={sn}",headers=headers)
    try:
        resolutionurl=requests.get(f"https://ani.gamer.com.tw/ajax/m3u8.php?sn={sn}&device={deviceid}",headers=headers).json()["src"]
    except:
        try:
            requests.get(f"https://ani.gamer.com.tw/ajax/videoCastcishu.php?sn={sn}&s=194699&ad=end",headers=headers)
            requests.get(f"https://ani.gamer.com.tw/ajax/videoStart.php?sn={sn}",headers=headers)
            resolutionurl=requests.get(f"https://ani.gamer.com.tw/ajax/m3u8.php?sn={sn}&device={deviceid}",headers=headers).json()["src"]
        except:
            resolutionurl=requests.get(f"https://ani.gamer.com.tw/ajax/m3u8.php?sn={sn}&device={deviceid}",headers=headers)
            print(resolutionurl.json()["error"]["message"])
            print("可嘗試更新cookie資訊")
            import sys
            sys.exit(0)
        
    #resolutionurl="https:\/\/gamer-cds.cdn.hinet.net\/vod_gamer\/_definst_\/smil:gamer2\/1105960c61553a4166f4b71bfb2e8fb9cb2710df\/hls-s-ae-2s.smil\/playlist.m3u8?token=s8ub07nihuER0aQDTkPPzA&expires=1598302260&bahaData=HorseCheng%3A16870%3A0%3APC%3A25761"
    resolutionm3u8=requests.get(resolutionurl.replace("\\",""), headers=headers).content
    with open("resolution.m3u8","wb") as f:
        f.write(resolutionm3u8)
        
    resolution=""
    with open("resolution.m3u8","r") as f:
        resolution=f.read()
    
    innlist = re.findall("(chunklist_.*)\n", resolution)
    reslist = re.findall("RESOLUTION=(.*)", resolution)
    if (times==0):
        for res in reslist:
           print(f"{res}")
        reschoice=input("請選擇下載解析度 (AXB可輸入A即可): ")  
    try:
        matching=[i for i, e in enumerate(reslist) if (reschoice in e) ] [0]
        inn=resolutionurl.replace( "playlist", re.findall("chunklist_b[0-9]+", innlist[matching])[0] )
    except :
        if(times==0):print("輸入與選項不符 自動選擇下載最高解析度")
        inn=resolutionurl.replace( "playlist", re.findall("chunklist_b[0-9]+", innlist[-1])[0] )
    
    print()
    try: os.makedirs("temp")
    except:pass
    try: os.makedirs("dump")
    except:pass
    try: os.makedirs("output")
    except:pass
    
    title = re.findall(".*smil/*",inn)[0]
    m3u8url = re.findall("chunklist.*",inn)[0]
    
    m3u8html=requests.get(title+m3u8url,headers=headers)
    
    num=0
    if(m3u8html.status_code == 200):
        with open("a.m3u8",'wb') as f:
          f.write(m3u8html.content)
    else: print("error!")
    
    with open ("a.m3u8","r") as f:
        m3u8files=f.readlines()
    
    keyurl=re.findall('URI="(.*)"',m3u8files[4])[0]
    key=requests.get(keyurl,headers=headers)
    with open("a.key" ,"wb" ) as f:
        f.write(key.content)
    
    with open("a.key","rb") as f:
        key=f.read()
        
    length=int ( ((len(m3u8files)-7)+0.5) //2 )
    cnt=1
    for i in range(6,len(m3u8files),2):
        target=m3u8files[i]
        print(f"downloading {cnt}/{length}", end='\r', flush=True)
        content=requests.get(title+target,headers=headers, stream=True)    
        num=0
        if(content.status_code == 200):
            with open(f"temp/a_{cnt}.ts",'wb') as f:
             	f.write(content.content)
            cnt+=1
        else: print("error!")
        
    filelist=""
    for i in natsort.natsorted(os.listdir('temp')):  
        video=None
        with open(f"temp/{i}","rb") as f:
            video=f.read()
        cryptor = AES.new(key, AES.MODE_CBC,video[0:16])
        with open (f"dump/{i}", "wb") as f:
            f.write(cryptor.decrypt(video))
        print(f"{i} is decrypted!", end='\r', flush=True)
        filelist+=f"file {i}\n"
        
    with open("dump/list.txt","w") as f:
        f.write(filelist)
    
    os.system(f'ffmpeg -y -f concat -i "dump/list.txt" -c copy "output/{filename}.mp4"') 
    
    try:shutil.rmtree("dump")
    except:pass
    try: shutil.rmtree("temp")
    except:pass