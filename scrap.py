from bs4 import BeautifulSoup
import requests
import pandas as pd
import random
from time import sleep
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
link="https://www.akakce.com/davlumbaz.html"
r=requests.get(link,headers=headers)
soup=BeautifulSoup(r.content,"html.parser")


linkler=soup.find_all("ul",attrs={"class":"pl_v9 qv_v9"})
urun_link_list = []
for i in linkler:
    urun_link = i.find("a")['href']
    urun_link_list.append(urun_link)
    urun_link_list[0]
yenilink="https://www.akakce.com"+urun_link_list[0]
yenilink

sözlük={}
excel=[]
x=0
link=pd.read_excel("link.xlsx")


while x<10:
    yeniLink=link.values[x][0]
    r=requests.get(yeniLink,headers=headers)
    soup=BeautifulSoup(r.content,"html.parser")
    
    Model=soup.find("div",attrs={"class":"pdt_v8"})
    urunModeli=Model.find("h1").text

    urun_ozellikleri = soup.find("a",{"name":"urun-ozellikleri"}).parent.parent

    ozellikler_row = urun_ozellikleri.find_all("tr")


    for i in ozellikler_row:
        tds = i.find_all("td")
        attrs=tds[1].text
        attrs=attrs.replace(": \xa0 ","")
        kategori=tds[0].text

        sözlük[kategori]=attrs

    marka=urunModeli.split()[0]
    model=urunModeli.split()[1:]
    model1=""
    for i in model:
        model1=model1+" "+i
    

    try:
        cihaz=sözlük["Cihaz Tipi"]
    except:
        cihaz="null"
    try:      
        tasarım=sözlük["Tasarım"]
    except:
        tasarım="null"

    try:
        yuzey=sözlük["Yüzey Tipi"]
    except:
        yuzey="null"

    try:
        genislik=sözlük["Genişlik"]
    except:
        genislik="null"
    try:
        panel=sözlük["Genişlik"]
    except:
        panel="null"
    try:
        maxEmis=sözlük["Maximum Emiş Gücü"]
    except:
        maxEmis="null"
    try:
        dB=sözlük["Ses Seviyesi"]
    except:
        dB="null"
    try:
        kademe=sözlük["Kademe"]
    except:
        kademe="null"
    try:
        enerjiSınıfı=sözlük["Enerji Sınıfı"]
    except:
        enerjiSınıfı="null"
    try:
        aydınlatmalı=sözlük["Aydınlatmalı"]
    except:
        aydınlatmalı="null"
    try:
        lambaSay=sözlük["Lamba Sayısı"]
    except:
        lambaSay="null"
    try:
        lambaGuc=sözlük["Lamba Gücü"]
    except:
        lambaGuc="null"
    try:
        filtreMalz=sözlük["Filtre Malzemesi"]
    except:
        filtreMalz="null"
    try:
        yikananFiltre=sözlük["Yıkanabilir Filtre"]
    except:
        yikananFiltre="null"
    try:
        Derinlik=sözlük["Derinlik"]
    except:
        Derinlik="null"
    try:
        yukseklik=sözlük["Yükseklik"]
    except:
        yukseklik="null"
    try:
        guc=sözlük["Güç"]
    except:
        guc="null"
    try:
        renk=sözlük["Renk"]
    except:
        renk="null"
    x=x+1
    print(f"kod: {r.status_code} --- veri sayısı{x}")
    sleep(random.randint(4,8))

    excel.append([marka,model1,yenilink,cihaz,tasarım,yuzey,genislik,panel,maxEmis,dB,kademe,enerjiSınıfı,renk,aydınlatmalı,guc,filtreMalz,Derinlik,yukseklik,guc,renk])



df=pd.DataFrame(excel,columns=["marka","model","link","Cihaz Tipi","Tasarım","Yüzey Tipi","Genişlik","Kontrol Paneli","Maximum Emiş Gücü","Ses Seviyesi","Kademe","Enerji Sınıfı","Renk","Aydınlatmalı","Güç","Filtre Malzemesi","Derinlik","Yükseklik","Güç W","renk"])
df.to_excel("akakce1.xlsx")