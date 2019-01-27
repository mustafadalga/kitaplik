from tkinter import *
from tkinter import messagebox
from backend import Veritabani

veritabani=Veritabani("kitaplar.db")

class Window:
        def __init__(self,window):
                window=window
                window.title("Kitaplık")
                window.iconbitmap("icon.ico")
                window.configure(background="#C0C0C0")

                yatay = int(window.winfo_screenwidth()/2 - 300)
                dikey = int(window.winfo_screenheight()/2 - 200)
                window.resizable(width=False,height=False)
                window.geometry("650x300+{}+{}".format(yatay,dikey))

                lblbaslik=Label(window,text="Başlık",background="#C0C0C0",font='Helvetica 10 bold')
                lblbaslik.place(x=0,y=10,width=60,height=24)

                lblyazar=Label(window,text="Yazar",background="#C0C0C0",font='Helvetica 10 bold')
                lblyazar.place(x=340,y=10,width=60,height=24)

                lblyil=Label(window,text="Yıl",background="#C0C0C0",font='Helvetica 10 bold')
                lblyil.place(x=0,y=44,width=60,height=24)

                lblisbn=Label(window,text="ISBN",background="#C0C0C0",font='Helvetica 10 bold')
                lblisbn.place(x=340,y=44,width=60,height=24)

                self.baslik=StringVar()
                self.txtbaslik=Entry(window,textvariable=self.baslik)
                self.txtbaslik.place(x=70,y=10,width=220,height=24)

                self.yazar=StringVar()
                self.txtyazar=Entry(window,textvariable=self.yazar)
                self.txtyazar.place(x=400,y=10,width=220,height=24)

                self.yil=StringVar()
                self.txtyil=Entry(window,textvariable=self.yil)
                self.txtyil.place(x=70,y=44,width=220,height=24)

                self.isbn=StringVar()
                self.txtisbn=Entry(window,textvariable=self.isbn)
                self.txtisbn.place(x=400,y=44,width=220,height=24)

                self.liste=Listbox(window)
                self.liste.place(x=10,y=78,width=440,height=184)

                scroll=Scrollbar(window)
                scroll.place(x=460,y=120,height=100)

                self.liste.configure(yscrollcommand=scroll.set)
                scroll.configure(command=self.liste.yview)

                self.liste.bind("<<ListboxSelect>>",self.satir_sec)

                btngoruntule=Button(window,text="Hepsini Gör",width=18,command=self.kitapGoruntule,background="#BE1D2C",fg="#ffffff")
                btngoruntule.place(x=490,y=78,width=130,height=24)

                btnara=Button(window,text="Kitap Ara",width=18,command=self.kitapAra,background="#BE1D2C",fg="#ffffff")
                btnara.place(x=490,y=110,width=130,height=24)

                btnekle=Button(window,text="Kitap Ekle",width=18,command=self.kitapEkle,background="#BE1D2C",fg="#ffffff")
                btnekle.place(x=490,y=142,width=130,height=24)

                btnguncelle=Button(window,text="Kitap Güncelle",width=18,command=self.kitapGuncelle,background="#BE1D2C",fg="#ffffff")
                btnguncelle.place(x=490,y=174,width=130,height=24)

                btnsil=Button(window,text="Kitap Sil",width=18,command=self.kitapSil,background="#BE1D2C",fg="#ffffff")
                btnsil.place(x=490,y=206,width=130,height=24)

                btnkapat=Button(window,text="Kapat",width=18,command=window.destroy,background="#BE1D2C",fg="#ffffff")
                btnkapat.place(x=490,y=238,width=130,height=24)
                    
        def entrySifirla(self):
                self.txtbaslik.delete(0,END)
                self.txtyazar.delete(0,END)
                self.txtyil.delete(0,END)
                self.txtisbn.delete(0,END)

        def rakamKontrolu(self,deger):
                try:
                        sonuc = int(deger)
                except ValueError:
                        return 0
                else:
                        return 1

        def kitapGoruntule(self):
                self.liste.delete(0,END)
                for satir in veritabani.goruntule():
                        self.liste.insert(END,satir)

        def kitapAra(self):
                if len(self.baslik.get().strip()) != 0 or len(self.yazar.get().strip())!=0 or len(self.yil.get().strip())!=0 or len(self.isbn.get().strip())!=0:
                        if len(self.yil.get().strip())!=0 and self.rakamKontrolu(self.yil.get().strip())==0:
                                messagebox.showwarning("Uyarı","Lütfen yılı rakam şeklinde giriniz!")
                        elif len(self.isbn.get().strip())!=0 and self.rakamKontrolu(self.isbn.get().strip())==0:
                                messagebox.showwarning("Uyarı","Lütfen isbn numarasını rakam şeklinde giriniz!")
                        else:
                                sonuc=veritabani.ara(self.baslik.get().strip(),self.yazar.get().strip(),self.yil.get().strip(),self.isbn.get().strip())
                                self.liste.delete(0,END)
                                if len(sonuc)==0:
                                        messagebox.showwarning("Uyarı", "Aradığınız kriterlere uygun bir sonuç bulunamadı")
                                else:
                                        for satir in sonuc:
                                                self.liste.insert(END,satir)
                                        self.entrySifirla()
                else:
                        messagebox.showwarning("Uyarı", "Arama yapmak için bir kriter giriniz!")

        def kitapEkle(self):
                if  len(self.baslik.get().strip()) == 0 or len(self.yazar.get().strip())==0 or len(self.yil.get().strip())==0 or len(self.isbn.get().strip())==0:
                        messagebox.showwarning("Uyarı", "Lütfen boş alanları doldurunuz!")
                else:
                        if self.rakamKontrolu(self.yil.get().strip())==0:
                                messagebox.showwarning("Uyarı", "Lütfen yılı rakam şeklinde giriniz!")
                        elif self.rakamKontrolu(self.isbn.get().strip())==0:
                                messagebox.showwarning("Uyarı", "Lütfen isbn numarasını rakam şeklinde giriniz!")
                        else:
                                veritabani.ekle(self.baslik.get().strip(),self.yazar.get().strip(),self.yil.get().strip(),self.isbn.get().strip())
                                messagebox.showinfo("Bildirim", "Kayıt işlemi başarıyla tamamlandı")
                                self.kitapGoruntule()
                                self.entrySifirla()


        def satir_sec(self,event):
                try:
                        index=self.liste.curselection()[0]
                        self.secilen_satir=self.liste.get(index)
                        self.txtbaslik.delete(0,END)
                        self.txtbaslik.insert(END,self.secilen_satir[1])
                        self.txtyazar.delete(0,END)
                        self.txtyazar.insert(END,self.secilen_satir[2])
                        self.txtyil.delete(0,END)
                        self.txtyil.insert(END,self.secilen_satir[3])
                        self.txtisbn.delete(0,END)
                        self.txtisbn.insert(END,self.secilen_satir[4])
                except IndexError:
                        pass


        def kitapSil(self):
                try:
                        veritabani.sil(self.secilen_satir[0])
                        messagebox.showinfo("Bildirim", "Silme işlemi başarıyla tamamlandı")
                        self.secilen_satir=None
                        self.kitapGoruntule()
                        self.entrySifirla()
                except IndexError:
                        messagebox.showwarning("Uyarı", "Lütfen silmek istediğiniz kitabı seçiniz!")
                except TypeError:
                        messagebox.showwarning("Uyarı", "Lütfen silmek istediğiniz kitabı seçiniz!")


        def kitapGuncelle(self):
                if  len(self.baslik.get().strip()) == 0 or len(self.yazar.get().strip())==0 or len(self.yil.get().strip())==0 or len(self.isbn.get().strip())==0:
                        messagebox.showwarning("Uyarı", "Lütfen boş alanları doldurunuz!")
                else:
                        if self.rakamKontrolu(self.yil.get().strip())==0:
                                messagebox.showwarning("Uyarı", "Lütfen yılı rakam şeklinde giriniz!")
                        elif self.rakamKontrolu(self.isbn.get().strip())==0:
                                messagebox.showwarning("Uyarı", "Lütfen isbn numarasını rakam şeklinde giriniz!")
                        else:
                                veritabani.guncelle(self.secilen_satir[0],self.baslik.get().strip(),self.yazar.get().strip(),self.yil.get().strip(),self.isbn.get().strip())
                                messagebox.showinfo("Bildirim", "Güncelleme işlemi başarıyla tamamlandı")
                                self.kitapGoruntule()
                                self.entrySifirla()

form=Tk()
calistir=Window(form)
calistir.kitapGoruntule()
form.mainloop()
