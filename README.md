# Overview

This project is a Python library for using HopeRF RFM95/96/97/98 LoRa radios with a Raspberry Pi. The design was inspired by the [RadioHead](http://www.airspayce.com/mikem/arduino/RadioHead) project that is popular on Arduino-based platforms. Several handy features offered by RadioHead are present here, including encryption, addressing, acknowledgments and retransmission. The motivation of this project is to allow Raspberry Pis to communicate with devices using the [RadioHead RF95](http://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) driver along with [RHReliableDatagram](http://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html) and [RHEncryptedDriver](http://www.airspayce.com/mikem/arduino/RadioHead/classRHEncryptedDriver.html).

# Usage
### Installation
Requires Python >= 3.5. [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) and [spidev](https://pypi.python.org/pypi/spidev) will be installed as requirements
```
pip install raspi-lora
```

### Getting Started
Here's a quick example that sets things up and sends a message:
```
from raspi_lora import LoRa, ModemConfig

# This is our callback function that runs when a message is received
def on_recv(payload):
    print("From:", payload.header_from)
    print("Received:", payload.message)
    print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))

# Use chip select 0. GPIO pin 17 will be used for interrupts
# The address of this device will be set to 2
lora = LoRa(0, 17, 2, modem_config=ModemConfig.Bw125Cr45Sf128, tx_power=14, acks=True)
lora.on_recv = on_recv

lora.set_mode_rx()

# Send a message to a recipient device with address 10
# Retry sending the message twice if we don't get an  acknowledgment from the recipient
message = "Hello there!"
status = lora.send_to_wait(message, 10, retries=2)
if status is True:
    print("Message sent!")
else:
    print("No acknowledgment from recipient")
    
# And remember to call this as your program exits...
lora.close()
```

### Encryption
If you'd like to send and receive encrypted packets, you'll need to install the [PyCryptodome](https://pycryptodome.readthedocs.io) package. If you're working with devices running RadioHead with RHEncryptedDriver, I recommend using the AES cipher.
```
pip install pycryptodome
```

and in your code:
```
from Crypto.Cipher import AES
crypto = AES.new(b"my-secret-encryption-key", AES.MODE_EAX)
```
then pass in `crypto` when instantiating the `LoRa` object:
```
lora = LoRa(0, 17, 2, crypto=crypto)
```

### Configuration
##### Initialization
```
LoRa(channel, interrupt, this_address, freq=915, tx_power=14,
      modem_config=ModemConfig.Bw125Cr45Sf128, acks=False, crypto=None)
```
**`channel`** SPI channel to use (either 0 or 1, if your LoRa radio is connected to CE0 or CE1, respectively)

**`interrupt`** GPIO pin (BCM-style numbering) to use for the interrupt

**`this_address`** The address number (0-254) your device will use when sending and receiving packets.

**`freq`** Frequency used by your LoRa radio. Defaults to 915Mhz

**`tx_power`** Transmission power level from 5 to 23. Keep this as low as possible. Defaults to 14

**`model_config`** Modem configuration. See [RadioHead docs](http://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#ab9605810c11c025758ea91b2813666e3). Default to Bw125Cr45Sf128.

**`receive_all`** Receive messages regardless of the destination address

**`acks`** If `True`, send an acknowledgment packet when a message is received and wait for an acknowledgment when transmitting a message. This is equivalent to using RadioHead's RHReliableDatagram

**`crypto`** An instance of PyCryptodome Cipher.AES (see above example)


##### Other options:
A `LoRa` instance also has the following attributes that can be changed:
- **cad_timeout** Timeout for channel activity detection. Default is 0
- **retry_timeout** Time to wait for an acknowledgment before attempting a retry. Defaults to 0.2 seconds
- **wait_packet_sent_timeout** Timeout for waiting for a packet to transmit. Default is 0.2 seconds

##### Methods
###### `send_to_wait(data, header_to, header_flags=0)`
Send a message and block until an acknowledgment is received or a timeout occurs. Returns `True` if successful
- ``data`` Your message. Can be a string or byte string
- ``header_to`` Address of recipient (0-255). If address is 255, the message will be broadcast to all devices and **`send_to_wait()`** will return `True` without waiting for acknowledgments
- ``header_flags`` Bitmask that can contain flags specific to your application

###### `send(data, header_to, header_id=0, header_flags=0)`
Similar to `send_to_wait` but does not block or wait for acknowledgments and will always return `True`
- ``data`` Your message. Can be a string or byte string
- ``header_id`` Unique ID of message (0-255)
- ``header_to`` Address of recipient (0-255). If address is 255, the message will be broadcast to all devices
- ``header_flags`` Bitmask that can contain flags specific to your application

###### `set_mode_rx()`
Set radio to RX continuous mode

###### `set_mode_tx()`
Set radio to TX mode

###### `set_mode_idle()`
Set radio to idle (disabling receiving or transmitting)

###### `sleep()`
Set radio to low-power sleep mode

###### `wait_packet_sent()`
Blocks until a packet has finished transmitting. Returns `False` if a timeout occurs

###### `close()`
Cleans up GPIO pins and closes the SPI connection. This should be called when your program exits.


#### Callbacks
`on_recv(payload)` 
Callback function that runs when a message is received
`payload` has the following attributes:
`header_from`, `header_to`, `header_id`, `header_flags`, `message`, `rssi`, `snr`

# Resources
[RadioHead](http://www.airspayce.com/mikem/arduino/RadioHead/) - The RadioHead project. Very useful source of information on working with LoRa radios.

[Forked version of RadioHead for Raspberry Pi](https://github.com/hallard/RadioHead) - A fork of the original RadioHead project that better accommodates the Raspberry Pi. Currently is a few years out of date.

[pySX127x](https://github.com/mayeranalytics/pySX127x) - Another Python LoRa library that allows for a bit more configuration. 

[Adafruit CircuitPython module for the RFM95/6/7/8](https://github.com/adafruit/Adafruit_CircuitPython_RFM9x) - LoRa library for CircuitPython

