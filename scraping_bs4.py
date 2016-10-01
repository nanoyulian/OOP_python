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
#import requests
import time
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

class DetikCrawlScrap:
    
    #class variable for popular news
    popnews_link_list = []
    jdl_artikel = []  
    artikel_populer_notag_noenter = []
       
    def __init__(self):      
        r = urllib.urlopen('http://www.detik.com').read()     
        self.soup = BeautifulSoup(r,"lxml")     
        self.start_time = time.time()
    
    def __remove_tags(self,text):
        return ''.join(ET.fromstring(text).itertext())
                
    def popular_news_process(self):
        popular = self.soup.find("div",attrs={'id':'box-pop'})       
       
        for pop_news in popular.contents[1].find_all("a") :
           self.popnews_link_list.append(pop_news.get('href'))
        
        #menelusuri popular.contents[1] yg ada tag <span class = normal> judul
        for pop_news in popular.contents[1].findAll("span",{"class":"normal"}) :
           self.jdl_artikel.append(pop_news.string)
        
        artikel_populer = []
        for link_pop in self.popnews_link_list :
            soup_pop = BeautifulSoup (urllib.urlopen(link_pop).read())              
            #pastikan bukan popup konten Dewasa
            if soup_pop.title.string != "18+ Materi Khusus Dewasa" :
                #search class = 'detail_text' atau 'text_detail'
                soup_pop_artikel = soup_pop.find("div",{'class':'detail_text'})
                if soup_pop_artikel == None : 
                    soup_pop_artikel = soup_pop.find('div',{'class':'text_detail'})               
                artikel_populer.append(soup_pop_artikel)                
            else : 
                artikel_populer.append("Konten Dewasa 18+")          
            
        artikel_populer_noscript = []
        for x in artikel_populer :
            y = BeautifulSoup(str(x))
            for scripttag in y.find_all('script'):
                scripttag.extract()
            #print ap_bs
            artikel_populer_noscript.append(y)
        
        artikel_populer_notag = []                 
        for x in artikel_populer_noscript : 
            y = self.__remove_tags(str(x))   
            #print y
            artikel_populer_notag.append(y)                
        
        for x in artikel_populer_notag :
            y = x.replace("\n", "")
            #print y,"\n"
            self.artikel_populer_notag_noenter.append(y)
    
    ##Import list judul dan artikel populer ke file XML
    #There are three helper functions useful
    # for creating a hierarchy of Element nodes. 
    # Element() creates a standard node, 
    #SubElement() attaches a new node to a parent,
    # and Comment() creates a node that serializes using XML’s comment syntax.
    
    def export_pop_toxml(self,filename,arr_jdl,arr_artikel):
        def prettify(elem):           
            rough_string = ET.tostring(elem, 'utf-8')
            reparsed = minidom.parseString(rough_string)
            return reparsed.toprettyxml(indent="  ")

        articles = Element('articles')
        comment = Comment('Generated from detik.com')
        articles.append(comment)
        for x,y in zip(arr_jdl,arr_artikel) :
            article = SubElement(articles, 'article')
            article_title = SubElement(article, 'article_title')
            article_title.text = x
            article_content = SubElement(article,'article_content')
            article_content.text = y
   
        tree = ET.ElementTree(articles)
        tree.write(filename)

##### APLIKASI START DISINI (MAIN) #########
pop = DetikCrawlScrap()
pop.popular_news_process()
pop.export_pop_toxml("articleOOP.xml",pop.jdl_artikel,pop.artikel_populer_notag_noenter)
#pop.__artikel_populer_notag_noenter


   