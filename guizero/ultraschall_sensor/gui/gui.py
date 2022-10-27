import guizero as gz
import serial
import time

config = {"ser": serial.Serial(), "connected": False}

def connect():
    config["ser"] = serial.Serial("COM" + str(sl_comport.value), 9600, timeout=1)
    config["connected"] = True
    bt_disconnect.enable()
    bt_read.enable()
    bt_connect.disable()
    sl_comport.disable()

def disconnect():
    config["ser"].close()
    config["connected"] = False
    bt_connect.enable()
    bt_read.disable()
    bt_disconnect.disable()
    sl_comport.enable()


def read_distance():
    if config["connected"]:
        config["ser"].write(bytes([0xA0]))
        # wait for 100 ms
        time.sleep(0.1)
        # read 3 bytes from sensor
        out = config["ser"].read(3)
        # Calculate distance based on received bytes
        distance = ((out[0] << 16) + (out[1] << 8) + out[2]) / 10000

        # Checking whether measured value is within the permissible distance
        if not 2 <= round(distance) <= 450:
            # If not, an error message is output
            tb_out.value = "---"
        else:
            sl_out.value = int(round(distance))
            tb_out.value = f"Distance: {distance:.0f}cm"


app = gz.App("Distance Display")

boxleft = gz.Box(app, align="left", border=1, width="fill", height="fill")

boxright = gz.Box(app, align="right", border=1, width="fill", height="fill")

# Configbox
configbox = gz.TitleBox(boxleft, "Config", align="top", width="fill", layout="grid")

lb_comport = gz.Text(configbox, "COM-Port:", align="left", width="fill", grid=[0, 0])
sl_comport = gz.Slider(configbox, start=1, end=20, align="right", width="fill", grid=[1, 0])
sl_comport.value = 6

# Controlbox
controlbox = gz.TitleBox(boxleft, "Control", align="top", width="fill", height="fill")


# Connect/Read
bt_connect = gz.PushButton(controlbox, text="Connect", width="fill", align="top", command=connect)
bt_disconnect = gz.PushButton(controlbox, text="Disconnect", width="fill", align="top", command=disconnect, enabled=False)
bt_read = gz.PushButton(controlbox, text="Read", width="fill", align="top", command=read_distance, enabled=False)
bt_read.repeat(200, read_distance)

# Output
tb_out = gz.Text(boxright, width="fill", height="fill", enabled=False)
sl_out = gz.Slider(boxright, width="fill", start=2, end=100, enabled=True)


app.display()
