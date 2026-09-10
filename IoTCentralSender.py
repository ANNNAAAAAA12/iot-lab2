import asyncio
import random
from azure.iot.device.aio import ProvisioningDeviceClient
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message

# Credenciales exactas de Azure IoT Central
scope_id = "0ne010B81EB"
device_id = "26a1012qbj0"
symmetric_key = "d6ODIUmamaN88mljj0DeC605Rvho65ymOTrzR3CAhkg="
provisioning_host = "global.azure-devices-provisioning.net"

async def main():
    # 1. Aprovisionamiento mediante DPS (Device Provisioning Service)
    print("Aprovisionando dispositivo con Azure IoT Central...")
    provisioning_client = ProvisioningDeviceClient.create_from_symmetric_key(
        provisioning_host=provisioning_host,
        registration_id=device_id,
        id_scope=scope_id,
        symmetric_key=symmetric_key,
    )

    result = await provisioning_client.register()
    if result.status != "assigned":
        print(f"Error en el registro: {result.status}")
        return

    print(f"¡Aprovisionado exitosamente! Hub de asignación: {result.registration_state.assigned_hub}")

    # 2. Conexión al Hub asignado
    device_client = IoTHubDeviceClient.create_from_symmetric_key(
        symmetric_key=symmetric_key,
        hostname=result.registration_state.assigned_hub,
        device_id=device_id,
    )

    await device_client.connect()
    print("¡Conectado exitosamente a Azure IoT Central!")

    # 3. Bucle de envío de telemetría
    try:
        while True:
            telemetry_data = {
                "temperatura": round(random.uniform(18.0, 30.0), 2),
                "humedad": round(random.uniform(40.0, 80.0), 2),
                "iluminacion": random.randint(100, 800)
            }
            
            msg = Message(str(telemetry_data))
            msg.content_encoding = "utf-8"
            msg.content_type = "application/json"

            await device_client.send_message(msg)
            print(f"Telemetría enviada a IoT Central: {telemetry_data}")
            await asyncio.sleep(10)
    except asyncio.CancelledError:
        pass
    finally:
        await device_client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())