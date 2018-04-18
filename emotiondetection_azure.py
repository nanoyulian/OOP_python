########### Python 2.7 #############
#import library
import requests

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
    
    response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
    num_faces = len(response.json())
    #print num_faces
    #print response.json()[0]
    #kolom yang diambil faceId, faceAttributes[emotion], gender, age
    
    #hitung rata-rata emotion dari semua faceid
    emotion_rate = detect_emotion_rate()




####################################
