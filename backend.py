import sqlite3


class Veritabani:
     def __init__(self,db):
          self.baglan=sqlite3.connect(db)
          self.sorgu=self.baglan.cursor()
          self.sorgu.execute("CREATE TABLE IF  NOT EXISTS kitap(id INTEGER PRIMARY KEY ,baslik TEXT ,yazar TEXT, yil INTEGER,isbn INTEGER)")
          self.baglan.commit()

     def ekle(self,baslik,yazar,yil,isbn):
          self.sorgu.execute("INSERT INTO kitap VALUES(NULL,?,?,?,?) ",(baslik,yazar,yil,isbn))
          self.baglan.commit()

     def goruntule(self):
          self.sorgu.execute("SELECT * FROM kitap")
          sonuc=self.sorgu.fetchall()
          return sonuc
     
     def ara(self,baslik="",yazar="",yil="",isbn=""):
          if  baslik!="" and yazar!="" and yil!="" and isbn!="":
               self.sorgu.execute("SELECT * FROM kitap WHERE baslik LIKE ? AND yazar LIKE ? AND isbn LIKE ? AND yil like ?",('%'+baslik+'%','%'+yazar+'%','%'+isbn+'%','%'+yil+'%'))
          elif baslik!="":
               self.sorgu.execute("SELECT * FROM kitap WHERE baslik LIKE ?",('%'+baslik+'%',))
          elif yazar!="":
               self.sorgu.execute("SELECT * FROM kitap WHERE yazar LIKE ?",('%'+yazar+'%',))
          elif isbn!="":
               self.sorgu.execute("SELECT * FROM kitap WHERE isbn LIKE ?",('%'+isbn+'%',))
          elif yil!="":
               self.sorgu.execute("SELECT * FROM kitap WHERE yil LIKE ?",('%'+yil+'%',))
          sonuc=self.sorgu.fetchall()
          return sonuc

     def sil(self,id):
          self.sorgu.execute("DELETE FROM kitap WHERE id=?",(id,))
          self.baglan.commit()

     def guncelle(self,id,baslik,yazar,yil,isbn):
          self.sorgu.execute("UPDATE kitap SET baslik=?,yazar=?,yil=?,isbn=? WHERE id=?",(baslik,yazar,yil,isbn,id))
          self.baglan.commit()


     def __del__(self):
          self.baglan.close()