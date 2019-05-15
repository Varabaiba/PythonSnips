# Borrowed from: https://stackoverflow.com/questions/37465157/pairing-bluetooth-devices-with-passkey-password-in-python-rfcomm-linux
# Untested yet

#Finally I am able to connect to a device using PyBlueZ. I hope this answer will help others in the future. I tried the following:

#First, import the modules and discover the devices.

import bluetooth, subprocess
nearby_devices = bluetooth.discover_devices(duration=4,lookup_names=True,
                                                      flush_cache=True, lookup_class=False)
#When you discover the device you want to connect, you need to know port, the address and passkey. With that information do the next:

name = name      # Device name
addr = addr      # Device Address
port = 1         # RFCOMM port
passkey = "1111" # passkey of the device you want to connect

# kill any "bluetooth-agent" process that is already running
subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)

# Start a new "bluetooth-agent" process where XXXX is the passkey
status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)

# Now, connect in the same way as always with PyBlueZ
try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((addr,port))
except bluetooth.btcommon.BluetoothError as err:
    # Error handler
    pass
#Now, you are connected!! You can use your socket for the task you need:

s.recv(1024) # Buffer size
s.send("Hello World!")
# Official PyBlueZ documentation is available here:
# https://github.com/karulis/pybluez/blob/master/docs/index.html
