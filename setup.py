from setuptools import setup

setup(name='TCsorgu',
    version='0.2',
    description="""
    TC Identity Number Check | Türkiye Cumhuriyeti (TC) Kimlik No Doğrulama\n\n
    - tcsorgu "TC_NO" "FIRST_NAME" "LAST_NAME" "BIRH_YEAR"\n
    - returns True or False
    """,
    url='http://github.com/dorukgezici/TCsorgu',
    author='Doruk Gezici',
    author_email='dorukgezici@gmail.com',
    license='MIT',
    packages=['TCsorgu'],
    install_requires=['requests'],
    scripts=['bin/TCsorgu'],
    zip_safe=False)
