from setuptools import setup

setup(
    name='raspi-lora',
    version='0.1',
    packages=['raspi_lora'],
    url='https://gitlab.com/the-plant/raspi-lora',
    license='MIT',
    author='Anne Wood',
    author_email='anne.w@fastmail.us',
    description='LoRa RF9x library for Raspberry Pi inspired by RadioHead',
    install_requires=[
        'RPi.GPIO',
        'spidev'],
)
