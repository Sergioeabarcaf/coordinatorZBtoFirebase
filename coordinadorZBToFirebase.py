# https://github.com/niolabs/python-xbee
from xbee import XBee, ZigBee
import serial

# Cambiar por puerto donde esta conectado el Xbee explorer
port = "/dev/ttyUSB0"

# Abrir puerto serial
ser = serial.Serial(port, 9600)

# Crear objeto Zigbee
xbee = XBee(ser)

# Obtener data enviada al coordinador y mostrarla por pantalla
while True:
    try:
        incoming = ser.readline().strip()
        print incoming
        res = xbee.wait_read_frame()
        print res
    except KeyboardInterrupt:
        break
ser.close()
