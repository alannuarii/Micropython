import urequests as requests
import ujson
from time import sleep
from machine import ADC


# Inisialisasi objek ADC
analog_value = ADC(0)

# URL REST API Flask
url = 'http://127.0.0.1:5432/'
headers = {"Content-Type": "application/json"}

while True:
    # Baca nilai ADC
    reading = analog_value.read_u16()
    vin = reading * 3.3 / 65535
    
    # Buat payload data
    data = {'digital': reading, 'analog': vin}
    
    # Kirim data ke REST API Flask
    #response = requests.post(url, headers, json=data)
    
    # Tampilkan respons dari REST API Flask
    print(data)
    
    # Tunggu selama 1 detik sebelum mengulangi loop
    sleep(1)