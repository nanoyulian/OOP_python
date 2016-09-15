# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:40:20 2016
@author: nano
proses crawl dan scrappying with BS4

Referensi : 
http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-filters
http://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup
http://stackoverflow.com/questions/2136267/beautiful-soup-and-extracting-a-div-and-its-contents-by-id

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


#koneksi ke url dan baca , simpan dalam variabel r (string)
r = urllib.urlopen('http://www.detik.com').read()
#buat objek dari BeautifulSoup(r) dgn parameter string
soup = BeautifulSoup(r) 
print type(soup)
#melakukan prettify pada string html, sekaligus slicing dari karakter 0-10000
html =  soup.prettify()[0:10000]

#mencari Filter <Div id> untuk berita terpopuler di detik simpan di dalam variabel popular
popular = soup.find("div",attrs={'id':'box-pop'})
#print popular.contents[1]

#definisikan list popnews link, buat nampung link berita populer
popnews_link_list = []

#menelusuri popular.contents[1] yg ada tag <a> 
for pop_news in popular.contents[1].find_all("a") :
   #mendapatkan isi dari attribut <href> dan tambahkan pada list
   popnews_link_list.append(pop_news.get('href'))
   #print link berita populer
   print pop_news.get('href')
   #enter   
   print "\n"

        
     