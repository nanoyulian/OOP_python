#import library
import requests
import operator

#auth token from kairos
auth_headers = {
    'app_id': 'f6f274da',
    'app_key': 'c72f796ffab35add9b29b0b0c1d70785'
}

#API url
url = 'https://api.kairos.com/v2/media'

#files folder tempat nyimpan gambar yang akan dideteksi
# silahkan diatomatisasi 
files = {
    'source': open('media/fotokelas.jpg')
}

#proses timeoout dalam second
data = {
    'timeout': 60
}

#manggil service kairos post
response = requests.post(url, files=files, data=data, headers=auth_headers)

print response.json()

print "JK : " , response.json()['frames'][0]['people'][0]['demographics']['gender']
jk = response.json()['frames'][0]['people'][0]['demographics']['gender']
emotions_dict = response.json()['frames'][0]['people'][0]['emotions']

#ambil nilai tertinggi di emotions
stats = emotions_dict
emotion_detected = max(stats.iteritems(), key=operator.itemgetter(1))[0]
print "Emotion : ", emotion_detected

#insert data ke thingspeak (database online service API)
url_insert = "https://api.thingspeak.com/update?api_key=9DV9Y5S7FKZAR5P0&field1=" + jk + "&field2=" + emotion_detected
response = requests.post(url_insert,data=data)
print "status insert ", response

# HINT : 
# INGAT SATU GAMBAR BISA BANYAK FACE ID!!!!! ARTINYA TIAP FACE ID MASUKKAN MJD 1 RECORD.. HINT : BUAT FUNCTION BUAT ITERASI.. 
# https://www.tutorialspoint.com/python/python_functions.htm
# https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds
# https://medium.com/@petehouston/capture-images-from-raspberry-pi-camera-module-using-picamera-505e9788d609

#analisis CUKUP MODUS..  