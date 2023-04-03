import network
import urequests

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect("AURA", "1sampai8")

while not wifi.isconnected():
    print("Tidak konek cuy")

if wifi.isconnected():
    print("Terkoneksi ke jaringan WiFi")
    print(wifi.ifconfig())
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = urequests.get(url)
    print(response.status_code)
    print(response.text)


