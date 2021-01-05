import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='raspi-lora',
    version='0.2',
    packages=['raspi_lora'],
    url='https://github.com/the-plant/raspi-lora',
    license='MIT',
    author='Anne Wood',
    author_email='anne.w@fastmail.us',
    description='LoRa RFM9x library for Raspberry Pi inspired by RadioHead',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
