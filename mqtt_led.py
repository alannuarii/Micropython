import machine
import network
import time
from umqtt.simple import MQTTClient

# Tentukan pin yang digunakan untuk mengendalikan LED
led_pin = machine.Pin(2, machine.Pin.OUT)

# Fungsi untuk menyalakan LED dan mengirim pesan MQTT
def turn_on_led_and_publish():
    led_pin.on()
    publish_message("LED ON")

# Fungsi untuk mematikan LED dan mengirim pesan MQTT
def turn_off_led_and_publish():
    led_pin.off()
    publish_message("LED OFF")

# Fungsi untuk memeriksa koneksi Wi-Fi
def check_wifi_connection():
    while not wifi.isconnected():
        print("Menghubungkan ke Wi-Fi...")
        time.sleep(1)
    print("Terhubung ke Wi-Fi")

# Fungsi untuk mengirim pesan MQTT
def publish_message(message):
    client = MQTTClient("esp8266", mqtt_broker, port=mqtt_port)
    client.connect()
    client.publish(mqtt_topic, message)
    client.disconnect()

# Konfigurasi Wi-Fi
wifi_ssid = "KANTOR PLTD KTM"
wifi_password = "daihatsu"

# Konfigurasi MQTT
mqtt_broker = "test.mosquitto.org"  # Alamat broker MQTT publik
mqtt_port = 1883  # Port default untuk MQTT
mqtt_topic = "led/alan"

# Inisialisasi koneksi Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(wifi_ssid, wifi_password)

# Tunggu hingga terhubung ke Wi-Fi
check_wifi_connection()

# Main loop
while True:
    turn_on_led_and_publish()  # Nyalakan LED dan kirim pesan MQTT
    time.sleep(2)  # Tunggu selama 2 detik
    turn_off_led_and_publish() # Matikan LED dan kirim pesan MQTT
    time.sleep(2)  # Tunggu selama 2 detik lagi
