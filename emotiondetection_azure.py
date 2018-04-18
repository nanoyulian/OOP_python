########### Python 2.7 #############
#import library
import requests
import operator

def detect_emotion_rate(list_emotions):
    
    return 0

################## ENTRY POINT #################################
if __name__ == "__main__":

    #key untuk 30hari
    subscription_key = "6214eaf40be54d2fa87acc86ae7acab1"
    assert subscription_key
    #url face API
    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
    #lokasi image
    image_url = 'https://how-old.net/Images/faces2/main007.jpg'
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
    
    # kelompok mood : 
    # negative = sadness, disgust, contempt, anger, fear
    list_sad = []
    list_contempt = []
    list_anger = []
    list_fear = []
    list_disgust = []
    # netral = netral
    list_neutral = []
    # positive = happiness, surprise    
    list_happy = []
    list_surprise = []
    
    #tambahkan masing-masing jenis emosi dr semua face ke dalam list jenis emosi msg2x
    for i in range(0,num_faces): 
        list_sad.append(response.json()[i]['faceAttributes']['emotion']['sadness'])
        list_disgust.append(response.json()[i]['faceAttributes']['emotion']['disgust'])
        list_contempt.append(response.json()[i]['faceAttributes']['emotion']['contempt'])
        list_anger.append(response.json()[i]['faceAttributes']['emotion']['anger'])
        list_fear.append(response.json()[i]['faceAttributes']['emotion']['fear'])
        list_neutral.append(response.json()[i]['faceAttributes']['emotion']['neutral'])
        list_surprise.append(response.json()[i]['faceAttributes']['emotion']['surprise'])
        list_happy.append(response.json()[i]['faceAttributes']['emotion']['happiness'])
    
    #hitung rata-rata emosi dari semua face per jenis emosi
    #tambahkan dan klasifikasikan ke dalam kategori negatif, netral, dan positif 
    rate_sad = sum(list_sad) / float(len(list_sad))
    rate_contempt = sum(list_contempt) / float(len(list_contempt))
    rate_anger = sum(list_anger) / float(len(list_anger))
    rate_fear = sum(list_fear) / float(len(list_fear))
    rate_disgust = sum(list_disgust) / float(len(list_disgust))
    #rata-rata emosi negatif
    rate_negative = (rate_sad + rate_contempt + rate_anger + rate_disgust) / 4.0 
    #rataan emosi netral
    rate_neutral = sum(list_neutral) / float(len(list_neutral))
    #rataan emosi positif
    rate_happy = sum(list_happy) / float(len(list_happy))
    rate_surprise = sum(list_surprise) / float(len(list_surprise))
    rate_positive = rate_happy + rate_surprise / 2.0 
    
    #simpan hasilnya nilai rataan dalam dictionary kategori emosi
    dict_group_emotions = {'negative' : rate_negative, 'neutral' : rate_neutral, 'positive' : rate_positive }
    emotion_detected = max(dict_group_emotions.iteritems(), key=operator.itemgetter(1))[0]
    print "Emotion : ", emotion_detected
    #kolom yang diambil faceId, faceAttributes[emotion], gender, age
    
    
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
