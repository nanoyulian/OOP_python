# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 06:01:28 2018

@author: nano
"""

import networkx as nx  
import matplotlib.pyplot as plt
import numpy as np

## Ambil Komunitas Terbesar dan Tampilkan
#G = nx.Graph()
#
## 1. Load Graph Awal (Keseluruhan)
#with open('f2_edgelist_map_id','U') as f:
#    for line in f.readlines():
#        line = line.strip().split(' ')
#        #print line
#        G.add_edge(line[0],line[1])
#
#print "Jumlah Nodes : ", G.number_of_nodes()
#
#i = 1
#with open('output_lemon_sp','U') as f:
#    for line in f.readlines():
#        if not line.strip().startswith("#"):
#            #split baris berdasarkan koma, masukkan dalam set
#            line = line.replace(" ", "")
#            line = line.strip().split(',')
#            #overlap_com = overlap_com.union(line)
#            G_maxcom = G.subgraph(line)
#    i +=1
#    
#
##print G_maxcom.edges('7554')
#print G_maxcom.number_of_nodes()
#print G_maxcom.number_of_edges()
##cari qlique yg menggambarkan paper 
##hapus qlique yg memiliki vertex yang sama 
#
#clique_author = nx.cliques_containing_node(G_maxcom)
##print clique_author
#
#list_of_clique = []
#for auth in clique_author:
#    for c in clique_author[auth]:
#        list_of_clique.append(c)
#
#for c in list_of_clique:
#    print c
#
#nx.write_edgelist(G_maxcom,"sp_edgelist")
#
#pos = nx.spring_layout(G_maxcom)
#plt.figure("Lemons Max. Communities")
#plt.rcParams['axes.facecolor'] = '#ffffb3'
#nx.draw_networkx(G_maxcom, pos, with_labels = True, width = 0.2, alpha = 0.4,font_size=8) 
#plt.show()

from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

cvpr_keyword = ""
sp_keyword = ""

with open('keywords_cvpr','U') as f:
    for line in f.readlines():
        line = line.strip().split(',')
        for words in line:
            #print words.lstrip().lower()
            cvpr_keyword = cvpr_keyword+ " " + words.lstrip().lower() 

with open('keywords_sp','U') as f:
    for line in f.readlines():
        line = line.strip().split(',')
        for words in line:
            #print words.lstrip().lower()
            sp_keyword = sp_keyword + " " + words.lstrip().lower() 
            
#print YOUR_TEXT

tags = make_tags(get_tag_counts(cvpr_keyword), maxsize=120)
create_tag_image(tags, 'tagcloud_cvpr.png', size=(900, 600), fontname='Lobster')

tags = make_tags(get_tag_counts(sp_keyword), maxsize=120)
create_tag_image(tags, 'tagcloud_sp.png', size=(900, 600), fontname='Lobster')