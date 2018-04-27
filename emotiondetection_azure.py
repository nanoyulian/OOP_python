########### Python 2.7 #############
#import library
import requests
import operator
import time

def calculate_atensi(count_pos, num_faces):
    """
    fungsi menghitung nilai atensi dari emosi yang terdeteksi (neg,net,pos).
    
    :param count_pos : jumlah face yang dikategorikan (netral+negatif)
    :param num_faces : jumlah wajah yg terdeteksi dari hasil API faceID azure.

    :return atensi : (persentase)
    """
    
    return (count_pos / num_faces) * 100
    

def load_image(path):
    """
    fungsi mengambil image pada folder/path tertentu untuk dianalisis.
    
    :param path : lokasi tempat menyimpan image
    
    """
    
    # To Do

    return 0 


def send_notification():
    """
    fungsi mengirimkan notif ke dosen dan sistem lain terkait kondisi kelas berdasarkan atensi.
    """
    
    # To Do 

    return "Success, atensi kelas .... "
    
################## ENTRY POINT #################################
if __name__ == "__main__":
    
    #akan selalu dijalankan selama selang waktu tertentu...     
    while True:
        # proses stop selama 60 detik / akan diulangi selama 60 detik. 
        time.sleep(60)
        #key untuk 30hari
        subscription_key = "6214eaf40be54d2fa87acc86ae7acab1"
        assert subscription_key
        #url face API
        face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
        #lokasi image
        image_url = 'https://familyhut.files.wordpress.com/2008/09/foto-bersama1.jpg'
        #header yg dikirim
        headers = { 'Ocp-Apim-Subscription-Key': subscription_key }
        #parameter url API, see docs reference nya face API
        params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender,emotion',
        }
        #execute API Url    
        response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
        #jumlah face yang dideteksi    
        num_faces = len(response.json())
        #print num_faces
        #print response.json()
        
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
        print "Level Atensi (0-100) : ", calculate_atensi(count_pos,num_faces)    
        
        #insert data ke thingspeak (database online service API) SESUAIKAN KOLOM2XNYA.. INI MASIH ADA JENIS KELAMINNYA JADI DIISI undefined_jeniskel
        url_insert = "https://api.thingspeak.com/update?api_key=9DV9Y5S7FKZAR5P0&field1=" + 'undefined_jenisKel' + "&field2=" + emotion_detected
        #proses timeoout dalam second
        data = {
            'timeout': 60
        }   
        response = requests.post(url_insert,data=data)
        
        print "status insert ", response
        #hitung rata-rata emotion dari semua faceid
        #emotion_rate = detect_emotion_rate()

####################################
