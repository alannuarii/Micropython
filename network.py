import network
import urequests

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect("KANTOR PLTD KTM", "daihatsu")

while not wifi.isconnected():
    print("Tidak konek cuy")

if wifi.isconnected():
    print("Terkoneksi ke jaringan WiFi")
    print(wifi.ifconfig())
    try:
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        response = urequests.get(url)
        print(response.status_code)
        print(response.text)
        response.close()
        
    except OSError:
        print('Error')


