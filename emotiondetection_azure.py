########### Python 2.7 #############
#import library
import requests
import operator
import time

import cv2
import numpy as np


####################################

def calculate_atensi(count_pos, num_faces):
    """
    fungsi menghitung nilai atensi dari emosi yang terdeteksi (neg,net,pos).
    
    :param count_pos : jumlah face yang dikategorikan (netral+negatif)
    :param num_faces : jumlah wajah yg terdeteksi dari hasil API faceID azure.

    :return atensi : (persentase)
    """
    
    return (count_pos / num_faces) * 100

    
def load_image_data(path):
    """
    fungsi mengambil data_image (lokal disk) pada folder/path tertentu untuk dianalisis.
    
    :param path : lokasi tempat menyimpan image
    
    :references : https://github.com/Microsoft/ProjectOxford-ClientSDK/issues/45 (local images)
    """
    # contoh link gambar : 
    # sukses               https://asset.kompas.com/crop/0x33:1000x533/780x390/data/photo/2017/06/16/636088134.jpg
    # GAGAL INI:           http://www.fahutanipb.com/wp-content/uploads/2016/08/Foto-Bersama-HAPKA-XVI-1_9.jpg
    # sukses               https://familyhut.files.wordpress.com/2008/09/foto-bersama1.jpg

    with open( path, 'rb' ) as f:
        image_data = f.read()

    # To Do
    # Mekanisme ambil file gambarnya gimana??? terserah ente.. 

    
    return image_data 


def send_notification():
    """
    fungsi mengirimkan notif ke dosen atau sistem lain terkait kondisi kelas berdasarkan atensi.
    """
    
    # To Do 

    return "Success, atensi kelas .... "
    
################## ENTRY POINT #################################
if __name__ == "__main__":
    
    #akan selalu dijalankan selama selang waktu tertentu...     
    while True:
        #key untuk 30hari
        subscription_key = "6214eaf40be54d2fa87acc86ae7acab1"
        assert subscription_key
        #url face API
        face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
        
        #load image   SEMENTARA MASIH YG ONLINE.. TINGGAL GANTI YG LOKAL PATHNYA PAKE FUNGSI load_image     
        #image_url = 'foto-bersama1.jpg'      
        image_data = load_image_data('foto-bersama1.jpg')        
        #print image_data
        
        #header yg dikirim
        headers = { 
            'Ocp-Apim-Subscription-Key': subscription_key,
            #ini diperlukan karena ngirim dari local disk.!!
            'Content-type': 'application/octet-stream',
        }
        #parameter url API, see docs reference nya face API
        params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender,emotion',
        }
        #karena load dari disk json = None, kalau dari url baru pake json
        json = None
        #execute API Url    
        #response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
        response = requests.post(face_api_url, params=params, headers=headers, json=json, data= image_data)
        
        #jika response dari API sukses
        if response.status_code == 200:
                
            #jumlah face yang dideteksi    
            num_faces = len(response.json())
            #print num_faces
            print response.json()
            
            # kelompok mood : negative (sadness, disgust, contempt, anger, fear) 
            #                 positive (happiness, surprise, netral)    
            
            #jumlah face yang dikategorikan negative 
            count_neg = 0
            #jumlah face yang dikategorikan positif
            count_pos = 0
            #untuk setiap face cek dan kategorikan emosinya ke dalam kategori negatif atau positif
            for i in range(0,num_faces):
                #untuk setiap face dapetin kategori emosinya yang nilainya paling maksimal
                emotion = max(response.json()[i]['faceAttributes']['emotion'].iteritems(), key=operator.itemgetter(1))[0]
                print emotion        
                #kategori emotion di hitung
                if emotion == 'sadness' or emotion == 'fear' or emotion == 'disgust' or emotion == 'contempt' or emotion == 'anger':
                    # tambah ke jumlah face yg negatif
                    count_neg += 1
                else:
                    # tambah ke jumlah face yg positif (netral,happy,surprise)
                    count_pos += 1
                    
            #tampilkan jumlah face yg positif dan negatif
            print "count neg = %d , count_pos = %d " % (count_neg,count_pos)            
            #tampilkan level atensi
            atensi = 0.0 #*** To Do :) 
            print "Level Atensi (0-100) : ", calculate_atensi(count_pos,num_faces)    
            
            #insert data ke thingspeak (database online service API) SESUAIKAN KOLOM2XNYA.. INI MASIH ADA JENIS KELAMINNYA JADI DIISI undefined_jeniskel
            url_insert = "https://api.thingspeak.com/update?api_key=9DV9Y5S7FKZAR5P0&field1=" + 'undefined_jenisKel' + "&field2= %f" % atensi
            #proses timeoout dalam second
            data = {
                'timeout': 60
            }   
            response = requests.post(url_insert,data=data)
            
            print "status insert ", response
        
        else:
            print response.json()['error']['message']
            
         # proses stop selama X detik / akan diulangi selama X detik. 
        time.sleep(1*60)
####################################################################################
