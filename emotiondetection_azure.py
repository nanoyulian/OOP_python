########### Python 2.7 #############
#import library
import requests
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
print response.json()

####################################
