# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:40:20 2016
@author: nano
proses crawl dan scrappying with BS4

Referensi : 
http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-filters
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
http://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup
http://stackoverflow.com/questions/2136267/beautiful-soup-and-extracting-a-div-and-its-contents-by-id
http://stackoverflow.com/questions/20968562/how-to-convert-a-bs4-element-resultset-to-strings-python

Tujuan : Scrapping artikel2x populer di www.detik.com
Algorithm : 
1. set url yang akan di crawl dan scrap
2. filter tag dan id yang berisi link berita populer
3. filter semua tag <a> yg ada berdasarkan hasil langkah 2, dan simpan isi 
   dari attribut href="links" (link) ke dalam sebuah list/array
4. Crawling untuk setiap link dari list hasil langkah 3. 
   filter tag dan id utk setiap link berita populer
   simpan content(artikel/image) dari setiap berita populer ke dalam list/array
5. simpan array content(artikel/image) ke dalam file (xml) untuk digunakan lebih lanjut
6. selesai
"""
from bs4 import BeautifulSoup
import urllib

import time
start_time = time.time()


#koneksi ke url dan baca , simpan dalam variabel r (string)
r = urllib.urlopen('http://www.detik.com').read()
#buat objek dari BeautifulSoup(r) dgn parameter string
soup = BeautifulSoup(r) 
#print type(soup)

#melakukan prettify pada string html, sekaligus slicing dari karakter 0-10000
#html =  soup.prettify()[0:10000]

#mencari Filter <Div id> untuk berita terpopuler di detik simpan di dalam variabel popular
popular = soup.find("div",attrs={'id':'box-pop'})
#print popular

#definisikan list popnews link, buat nampung link berita populer dan jdl_artikel
popnews_link_list = []
jdl_artikel = []

#menelusuri popular.contents[1] yg ada tag <a> 
for pop_news in popular.contents[1].find_all("a") :
   #mendapatkan isi dari attribut <href> dan tambahkan pada list
   popnews_link_list.append(pop_news.get('href'))
   #print link berita populer
   #print pop_news.get('href')  
   #enter   
   #print "\n"

#menelusuri popular.contents[1] yg ada tag <span class = normal> judul
for pop_news in popular.contents[1].findAll("span",{"class":"normal"}) :
   #mendapatkan isi dari attribut <href> dan tambahkan pada list
   jdl_artikel.append(pop_news.string)
   #print link berita populer
   #print pop_news.string
   #enter   
   #print "\n"
   
#crawling ke url yang ada di list
artikel_populer = []
#belum dites yg dibawah ini msh ada kemungkinan error
for link_pop in popnews_link_list :
    soup_pop = BeautifulSoup (urllib.urlopen(link_pop).read())   
   
    #pastikan bukan popup konten Dewasa
    if soup_pop.title.string != "18+ Materi Khusus Dewasa" :
        #search class = 'detail_text' atau 'text_detail'
        soup_pop_artikel = soup_pop.find("div",{'class':'detail_text'})
        if soup_pop_artikel == None : 
            soup_pop_artikel = soup_pop.find('div',{'class':'text_detail'})
        #print soup_pop_artikel
        #print "\n"
        #append tiap artikel populer ke array
        artikel_populer.append(soup_pop_artikel)
    else : 
        artikel_populer.append("Konten Dewasa 18+")   
    
#cek isi list artikel_populer harus sama dengan jumlah jdl_artikel
#for x in artikel_populer : print x,"\n"

print "Waktu Proses Scrapping :", time.time() - start_time, "Detik"
start_time = time.time() 
#prosess cleaning artikel bersihkan tag script di msg2x artikel
artikel_populer_noscript = []
for x in artikel_populer :
    y = BeautifulSoup(str(x))
    for scripttag in y.find_all('script'):
        scripttag.extract()
    #print y,"\n"
    artikel_populer_noscript.append(y)

artikel_populer_notag = []

import xml.etree.cElementTree as ET
def remove_tags(text):
    return ''.join(ET.fromstring(text).itertext())
   
for x in artikel_populer_noscript : 
    x = remove_tags(str(x))
    #print x,"\n"    

print "Waktu Proses Cleaning :", time.time() - start_time, "Detik"
print "jumlah artikel Populer :", len(artikel_populer_noscript)

#Import list judul dan artikel populer ke file XML

    