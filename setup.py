import setuptools

setuptools.setup(
    name='raspi-lora',
    version='0.1',
    packages=['raspi_lora'],
    url='https://gitlab.com/the-plant/raspi-lora',
    license='MIT',
    author='Anne Wood',
    author_email='anne.w@fastmail.us',
    description='LoRa RFM9x library for Raspberry Pi inspired by RadioHead',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='lora rfm95 rfm9x rfm96 rfm97 rfm98 hardware raspberrypi',
    install_requires=[
        'RPi.GPIO',
        'spidev'],
)
