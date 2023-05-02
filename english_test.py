# -*- coding: utf-8 -*-
import tkinter.ttk as ttk
import tkinter as tk
import csv
import tempfile as tf
import random as rd
import time
from pygame import mixer
from gtts import gTTS
ttl=0
ttlgrand = 0
gua = 0
enlist = []
wordlist = []
mixer.init()
def getlevel():
    a = levelchoose.get()
    if bool(a) == False:
        pass
    else:
        for wiget in win.winfo_children():
                wiget.destroy()
        #刪除選擇等級欄位
        fp = open(a+'.csv','r',encoding='utf-8')
        csv_reader = csv.reader(fp)
        data = list(csv_reader)
        ssss=0
        while(ssss<100):
            a = rd.randrange(len(data))
            if a not in enlist:
                enlist.append(a)
            else :
                ssss-=1
            ssss+=1
            for i in range(len(data)):
                 wordlist.append(list(filter(None, data[i])))
        #讀取對應等級的單字檔案並創造隨記考試list
        global detectenans,detectcnans,cnentry,enentry 
        cnlabel = tk.Label(win,text='中文') 
        cnlabel.grid(row=0,column=0)
        enlabel = tk.Label(win,text='英文') 
        enlabel.grid(row=1,column=0)
        cnentry = tk.Entry(win,)
        cnentry.grid(row=0,column=1)
        enentry = tk.Entry(win)
        enentry.grid(row=1,column=1)
        confirmbutton =tk.Button(win ,text='confirm',command=conform) 
        confirmbutton.grid(row=2,column=1)
        playbutton = tk.Button(win,text='play',command=play) 
        playbutton.grid(row=2,column=0)
        detectenans = tk.Label(win) 
        detectenans.grid(row=1,column=2)
        detectcnans = tk.Label(win) 
        detectcnans.grid(row=0,column=2) #獲取考試等級、產生亂數表、生成考試介面
def play():
    global startime,gua
    startime = time.time()
    with tf.NamedTemporaryFile(delete=1) as fp :
        ttl = gTTS(text= wordlist[enlist[gua]][0],lang='en')
        ttl.save('{}.mp3'.format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()
    print(wordlist[enlist[gua]]) #播放音檔
def conform():
    global gua,ttlgrand
    if cnentry.get() in wordlist[enlist[gua]]:
        detectcnans['text'] = '正確'
        ttlgrand+=0.5
    else :
        detectcnans['text'] = '錯誤'
    if enentry.get() == wordlist[enlist[gua]][0] :
        detectenans['text'] = '正確'
        ttlgrand+=0.5   
    else:detectenans['text'] = '錯誤' 
    if gua == 99:
        global startime
        end = time.time()
        for wiget in win.winfo_children():
                wiget.destroy()
        grand = tk.Label(win,text =str(ttlgrand),font=('Arial',25))
        grand.pack()
        usedtime = tk.Label(win,text='you use '+f"{(end-startime)/60:.2f}"+' min')
        usedtime.pack()
    gua +=1
win = tk.Tk()
win.title('English test')
win.geometry('300x100')
win.resizable(False,False)

#初始化
levelchoose = ttk.Combobox(win)
levelchoose['values'] = [' level 1 ',' level 2 ', ' level 3 ','level 4 ', ' level 5 ' , ' level 6 ']
levelchoose.pack()
confirm = tk.Button(text='confirm',command=getlevel)
confirm.pack()
win.mainloop()