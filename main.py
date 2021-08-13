from tkinter import *
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
from PIL import ImageTk,Image

URL = "https://www.instagram.com/"

def verileri_al(kullanici_adi):
    son_url = URL + kullanici_adi

    request = Request(son_url, headers={'User-Agent':'Mozilla/5.0'})
    html_verisi = urlopen(request).read()

    soup = BeautifulSoup(html_verisi, 'html.parser')

    veri = soup.find("meta",property="og:description").attrs['content']

    veri = veri.split("-")[0]

    veri = veri.split(" ")

    pp_url = soup.find("meta",property="og:image").attrs['content']

    def dl_jpg(pp_url, file_path, kullanici_adi):
        full_path = file_path + kullanici_adi + ".jpg"
        urllib.request.urlretrieve(pp_url, full_path)

    dl_jpg(pp_url,"images/", kullanici_adi)
    
    kullanici_takipci = Label(frame, text="takipci sayisi: "+veri[0])
    kullanici_takipci.pack()
    kullanici_takip = Label(frame, text="takip edilen sayisi: "+veri[2])
    kullanici_takip.pack() 
    kullanici_gonderi = Label(frame, text="gonderi sayisi: "+veri[4])
    kullanici_gonderi.pack()  

    pp_yol = "C:\\Users\\tugra\\OneDrive\\Masaüstü\\PYTHON_PROJE\\instagram-bilgi\\images\\"+ kullanici_adi + ".jpg"
    pp = Image.open(pp_yol)
    pp = ImageTk.PhotoImage(pp)
    pp_label = Label(frame)
    pp_label.pack()
    pp_label.configure(image=pp)
    pp_label.image = pp
    

    




root = Tk()


canvas = Canvas(root, height=700, width=700)
canvas.pack()

frame = Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

kullanici_adi_text = Label(frame, text="kullanici adi giriniz:")
kullanici_adi_text.pack()

kullanici_adi_entry = Entry(frame, width=20)
kullanici_adi_entry.pack()

def gonder():
    kullanici_adi = kullanici_adi_entry.get()
    verileri_al(kullanici_adi)

kullanici_adi_gonderbutton = Button(frame, text="Bul", command=gonder)
kullanici_adi_gonderbutton.pack()
