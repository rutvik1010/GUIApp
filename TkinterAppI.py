__author__ = 'Rutvik'
from Tkinter import *
import Tkinter as tk
import os#For QuickLaunch
from PIL import Image, ImageTk
from bs4 import BeautifulSoup
import pyttsx
import sys
import time
import requests#For web crawling
import datetime#For date on the "TO DO LIST"
from tkFileDialog import *
from tkMessageBox import *
import webbrowser#For hyperlinks (NEWS)
#----------------------------------------------------Main Frame---------------------------------------------------------
Gui = Tk()
Gui.config(bg='black')
Gui.geometry("600x650") #Width x Height
Gui.title("PyBoard Myugen")
Gui.iconbitmap(default='Apathae-Satellite-2-Documents.ico')
Gui.resizable(0, 0)
#--------------------------------------------------NEWS FRAME-----------------------------------------------------------
news_label = Label(Gui,text = "Top News in India", font="Verdana 10 bold",fg="white",bg="black")
news_label.place(x=110,y=0)
text_pad = Text(Gui)
text_pad.place(x=0,y=26,height=220,width=348)
inst_label =Label(Gui, text="Click on the text to read the full story", font="Verdana 6", bg="white")
inst_label.place(x=0,y=27)
list_title = [0]
list_link = [0]
values = 0
values1 = 0


def callback1(event):
    url = list_link[0]
    webbrowser.open_new(url)


def callback2(event):
    url = list_link[1]
    webbrowser.open_new(url)


def callback3(event):
    url = list_link[2]
    webbrowser.open_new(url)


def callback4(event):
    url = list_link[3]
    webbrowser.open_new(url)


def callback5(event):
    url = list_link[4]
    webbrowser.open_new(url)


def callback6(event):
    url = list_link[5]
    webbrowser.open_new(url)


def callback7(event):
    url = list_link[6]
    webbrowser.open_new(url)


def callback8(event):
    url = list_link[7]
    webbrowser.open_new(url)


def callback9(event):
    url = list_link[8]
    webbrowser.open_new(url)


def callback0(event):
    url = list_link[9]
    webbrowser.open_new(url)
url = "http://www.ndtv.com/top-stories"
connect = requests.get(url)
raw_code_news = connect.text
soup_code_news = BeautifulSoup(raw_code_news, "lxml")
soup_code_news.prettify()
for i in soup_code_news.find_all("div", {"class": "nstory_header"}):
    info_news1 = i.string
    if values <= 10:
        list_title.insert(values, info_news1)
        values += 1
for i in soup_code_news.find_all("div", {"class": "nstory_header"}):
    info_news12 = i.find("a")["href"]
    if values1 <= 10:
        list_link.insert(values1, info_news12)
        values += 1
label1 = Label(text_pad, text=list_title[0].lstrip(), bg="white", font="Verdana 6", fg="blue")
label1.place(x=0, y=20)
label1.bind("<Button-1>", callback1)
label2 = Label(text_pad, text=list_title[1].lstrip(), bg="white", font="Verdana 6", fg="red")
label2.place(x=0, y=40)
label2.bind("<Button-1>", callback2)
label3 = Label(text_pad, text=list_title[2].lstrip(), bg="white", font="Verdana 6", fg="blue")
label3.place(x=0, y=60)
label3.bind("<Button-1>", callback3)
label4 = Label(text_pad, text=list_title[3].lstrip(), bg="white", font="Verdana 6", fg="red")
label4.place(x=0, y=80)
label4.bind("<Button-1>", callback4)
label5 = Label(text_pad, text=list_title[4].lstrip(), bg="white", font="Verdana 6", fg="blue")
label5.place(x=0, y=100)
label5.bind("<Button-1>", callback5)
label6 = Label(text_pad,text=list_title[5].lstrip(),bg="white",font="Verdana 6",fg="red")
label6.place(x=0,y=120)
label6.bind("<Button-1>", callback6)
label7 = Label(text_pad,text=list_title[6].lstrip(),bg="white",font="Verdana 6",fg="blue")
label7.place(x=0,y=140)
label7.bind("<Button-1>", callback7)
label8 = Label(text_pad,text=list_title[7].lstrip(),bg="white",font="Verdana 6",fg="red")
label8.place(x=0,y=160)
label8.bind("<Button-1>", callback8)
label9 = Label(text_pad,text=list_title[8].lstrip(),bg="white",font="Verdana 6",fg="blue")
label9.place(x=0,y=180)
label9.bind("<Button-1>", callback9)
label0 = Label(text_pad,text=list_title[9].lstrip(),bg="white",font="Verdana 6",fg="red")
label0.place(x=0,y=200)
label0.bind("<Button-1>", callback0)
#------------------------------------------------------To Do List-------------------------------------------------------
date = datetime.datetime.now().date()
text_label = Label(Gui, text="To Do List", font="Verdana 10 bold", fg="white", bg="black")
text_label.place(x=428, y=0)
text_label1 = Label(Gui, text=date, font="Verdana 5 bold", fg="white", bg="black")
text_label1.place(x=520, y=0)
f2 = tk.Frame(width=250, height=250, background="white")
f2.place(in_=Gui, x=350, y=25)
new = tk.Frame(width=250, height=250, background="white")
new.place(in_=f2, x=0, y=0)
text = Text(new)
text.place(x=0, y=25, width=250, height=200)
filename = None


def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)


def saveFile():
    global filename
    try:
        t = text.get(0.0, END)
        f = open(filename, 'w')
        f.write(t)
        f.close()
    except:
        saveAs()


def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt',initialfile=date)
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Unable to save file...")


def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
note_save = Button(Gui, text="New", command=lambda: newFile(), bg="black", fg="white")
note_save.place(x=350, y=26, width=62.5)
note_save = Button(Gui, text="Open", command=lambda: openFile(), bg="black", fg="white")
note_save.place(x=412.5, y=26, width=62.5)
note_save = Button(Gui, text="Save", command=lambda: saveFile(), bg="black", fg="white")
note_save.place(x=475, y=26, width=62.5)
note_save = Button(Gui, text="SaveAs", command=lambda: saveAs(), bg="black", fg="white")
note_save.place(x=537.5, y=26, width=62.5)
#----------------------------------------------------QUICK LAUNCH ICON FUNCTIONS----------------------------------------


def chromec():
    os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    engine = pyttsx.init()
    engine.setProperty('rate', 180)
    voices = engine.getProperty('voices')
    engine.say("Starting Google Chrome in a moment")
    engine.runAndWait()


def steamc():
    os.startfile("C:\Program Files (x86)\Steam\Steam.exe")
    engine = pyttsx.init()
    engine.setProperty('rate', 180)
    voices = engine.getProperty('voices')
    engine.say("Starting Steam in a moment")
    engine.runAndWait()


def iepc():
    os.startfile(r"C:\Program Files (x86)\JetBrains\PyCharm Community Edition 4.5.3\bin\pycharm.exe")
    engine = pyttsx.init()
    engine.setProperty('rate', 180)
    voices = engine.getProperty('voices')
    engine.say("Starting JetBeans in a moment")
    engine.runAndWait()
#---------------------------------------------------------WEATHER FUNCTION----------------------------------------------
url = "https://www.google.com/search?q=temperature+bufalo&oq=tem&aqs=chrome.0.69i59j69i65j69i57j0l3.6442j0j4&sourceid=chrome&es_sm=93&ie=UTF-8#q=temperature+buffalo"
source_code = requests.get(url)
plain_text = source_code.text
bs4text = BeautifulSoup(plain_text, "lxml")
for values in bs4text.findAll('span', {'class': "wob_t"}):
    current_temperature = values.string
    break
list1 = [0]
list2 = [0]
listfinal = []
i = 0
k = 0
url = "http://www.wkbw.com/weather"
source_code = requests.get(url)
plain_text = source_code.text
bs4text = BeautifulSoup(plain_text, "lxml")
for values in bs4text.findAll('span', {'class': "text--primary",}):
  if i <= 7:
     values1 = values.string
     i += 1
     list1.insert(i, values1)
for values in bs4text.findAll('span', {'class': "text--secondary",}):
  if k <= 7:
     values2 = values.string
     k += 1
     list2.insert(k, values2)
new = dict(zip(list1, list2))
del new[0]
Value1 = list1[1] + list2[1]
Value2 = list1[2] + list2[2]
Value3 = list1[3] + list2[3]
Value4 = list1[4] + list2[4]
Value5 = list1[5] + list2[5]
Value6 = list1[6] + list2[6]
Value7 = list1[7] + list2[7]
Value8 = list1[8] + list2[8]


def back():
    Weather = Button(Gui, text="Weather Report", command=weatherc, image=weatherfin, bg="white")
    Weather.place(x=0, y=550, height=100, width=600)


def weather_voice_c():
    engine = pyttsx.init()
    engine.setProperty('rate', 150)
    voices = engine.say(" The current temperature is : " + current_temperature)
    voices = engine.say(Value1)
    voices = engine.say(Value2)
    voices = engine.say(Value3)
    voices = engine.say(Value4)
    voices = engine.say(Value5)
    voices = engine.say(Value6)
    voices = engine.say(Value7)
    voices = engine.say(Value8)
    engine.runAndWait()


def weatherc():
    Weather1.config(state=DISABLED)
    label1 = Label(Gui, text=Value1,).place(x=150,y=560)
    label1 = Label(Gui, text=Value2, bg="white").place(x=150, y=580)
    label1 = Label(Gui, text=Value3, bg="white").place(x=150, y=600)
    label1 = Label(Gui, text=Value4, bg="white").place(x=150, y=620)
    label1 = Label(Gui, text=Value5, bg="white").place(x=20, y=560)
    label1 = Label(Gui, text=Value6, bg="white").place(x=20, y=580)
    label1 = Label(Gui, text=Value7, bg="white").place(x=20, y=600)
    label1 = Label(Gui, text=Value8, bg="white").place(x=20, y=620)
    label1 = Label(Gui, text="Current temperature is : " + current_temperature, font="Verdana 10 bold", bg="white").place(x=360, y=610)
    subotton = Button(Gui, text="Back", command=back,fg="red").place(x=520, y=560)
    weather_voice = Button(Gui, text="Voice", command=weather_voice_c,fg="red").place(x=400, y=560)
#----------------------------------------------------WORD OF THE DAY----------------------------------------------------


def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c

    return out
url = "http://www.merriam-webster.com/word-of-the-day/"
one = requests.get(url)
source_code1 = one.text
soup_text = BeautifulSoup(source_code1, "lxml")
soup_text.prettify()
for usefull in soup_text.find_all("div", {"class" : "word-header"}):
    new = soup_text.find("h1")
    dailyword = remove_html_markup(new)
    word_new = remove_html_markup(dailyword)
url_2 = "http://dictionary.cambridge.org/dictionary/english/"
url_3 = url_2 + word_new
one_2 = requests.get(url_3)
source_code1_2 = one_2.text
soup_text_2 = BeautifulSoup(source_code1_2, "lxml")
new_list = [0]
for usefull1 in soup_text_2.find_all("span", {"class": "def"}):
    meaning1 = usefull1.find_all(text=True)
    val33 = " ".join(meaning1)
    #print(val33)
    break


def wordc_voice():
    engine = pyttsx.init()
    engine.setProperty('rate', 180)
    voices = engine.getProperty('voices')
    engine.say("The meaning of the word " + word_new + " is")
    engine.say(val33)
    engine.runAndWait()


def wordc():
    newb = Button(Gui,bg="white")
    newb.place(x=0, y=450, height=100, width=600)
    label12 = Label(Gui,text = word_new + ": ", font="Times  10  ",bg="white")
    label12.place(x = 10, y= 480)
    label13 = Label(Gui,text =val33, font="Times  8 bold ",bg="white")
    label13.place(x = 100, y = 480)
    backbutton = Button(Gui, text="Back",command=wotdbc,fg="red")
    backbutton.place(x=520, y=460)
    backbutton = Button(Gui, text="Voice",command=wordc_voice,fg="red")
    backbutton.place(x=400, y=460)


def wotdbc():
    wotd = Button(Gui, text="Word of the Day",font="Verdana 15 bold",command=wordc, bg="white",fg="Blue")
    wotd.place(x=0, y=450, height=100 , width=600)
#Word of the Day
wotd = Button(Gui, text="Word of the Day", font="Verdana 15 bold", command=wordc, bg="white", fg="Blue")
wotd.place(x=0, y=450, height=100, width=600)
#----------------------------------------------------IMAGES FOR ICONS---------------------------------------------------
#STEAM
steamimg1 = Image.open('steam_icon_for_mac_redesign_by_drigermeow25-d84lggt.png')
steamimgres = steamimg1.resize((200, 200), Image.ANTIALIAS)
steamimgfin = ImageTk.PhotoImage(steamimgres)
#CHROME
chromeimg1 = Image.open('Google-Chrome.png')
chromeimgres = chromeimg1.resize((180, 180), Image.ANTIALIAS)
chromeimgfin = ImageTk.PhotoImage(chromeimgres)
#PYTHON
pyimg1 = Image.open('417967f5da0c9f827e47583c5871ea82.png')
pyimgres = pyimg1.resize((200, 200), Image.ANTIALIAS)
pyimgfin = ImageTk.PhotoImage(pyimgres)
#Weather
weather1 = Image.open("Status-weather-showers-day-icon.png")
weatherres = weather1.resize((100,100), Image.ANTIALIAS)
weatherfin = ImageTk.PhotoImage(weatherres)
#----------------------------------------------------ROW 2 BUTTONS------------------------------------------------------
#Chrome
Chrome = Button(Gui, text="Google Chrome", command=chromec, image=chromeimgfin)
Chrome.place(x=0, y=250, height=200, width=200)
#Steam
Steam = Button(Gui, text="Steam", command=steamc, image=steamimgfin)
Steam.place(x=200, y=250, height=200, width=200)
#Pycharm
IEP = Button(Gui, text="IEP", command=iepc, image=pyimgfin)
IEP.place(x=400, y=250, height=200, width=200)
#----------------------------------------------------ROW 3 BUTTONS------------------------------------------------------
#Weather Report
Weather1 = Button(Gui, text="Weather Report", command=weatherc, image=weatherfin, bg="white")
Weather1.place(x=0, y=550, height=100, width=600)
#----------------------------------------------------END----------------------------------------------------------------
Gui.mainloop()