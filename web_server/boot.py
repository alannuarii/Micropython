import esp
esp.osdebug(None)

import network
from machine import Pin

import time
try:
  import usocket as socket
except:
  import socket

SSID = "OOO"
PASSWORD = "1sampai8"
MAX_RETRIES = 20  # waktu maksimum untuk menunggu koneksi WiFi (dalam hitungan detik)

station = network.WLAN(network.STA_IF)
station.active(True)

print("Mencoba terhubung ke Wi-Fi...")
station.connect(SSID, PASSWORD)

retries = 0
while not station.isconnected() and retries < MAX_RETRIES:
    retries += 1
    print("Menunggu koneksi Wi-Fi... ({}/{})".format(retries, MAX_RETRIES))
    time.sleep(1)

if station.isconnected():
    print("Koneksi Wi-Fi berhasil.")
    print(station.ifconfig())
else:
    print("Gagal terhubung ke Wi-Fi.")

led = Pin(2, Pin.OUT)

