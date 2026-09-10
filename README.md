# Laboratorio 2: Arquitectura Híbrida IoT (VM + Wokwi + Azure IoT Central)
**UNAB - IoT + Cloud + Sistemas Distribuidos**

---

## 📌 Descripción
Arquitectura IoT híbrida conectada a **Azure IoT Central** con 8 dispositivos: simuladores nativos de Azure, script de Python en Ubuntu/WSL y circuito ESP32 en Wokwi.

---

## 🛠️ Configuración de la VM (Ubuntu / WSL)

```bash
# Instalación e inicio del entorno
sudo apt update && sudo apt install -y python3 python3-pip python3-venv git
mkdir -p ~/lab2 && cd ~/lab2
python3 -m venv env
source env/bin/activate
pip install azure-iot-device

# Ejecución del emisor
python3 IoTCentralSender.py
🔌 Proyecto Wokwi (/wokwi)
sketch.ino: Firmware ESP32 (DHT22, potenciómetro, MQTT/DPS y comando setAlertLed).

diagram.json: Esquema y conexiones del circuito.

libraries.txt: Dependencias (PubSubClient, DHT sensor library, ArduinoJson).

Ejecución del monitor local:

Bash
python3 wokwi_sim.py
