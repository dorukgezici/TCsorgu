#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import requests
import argparse

xml = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
      <TCKimlikNo></TCKimlikNo>
      <Ad></Ad>
      <Soyad></Soyad>
      <DogumYili></DogumYili>
    </TCKimlikNoDogrula>
  </soap12:Body>
</soap12:Envelope>"""
headers = {'Content-Type': 'application/soap+xml; charset=utf-8'}


def query(id, name, surname, birth_year):
    element = ET.fromstring(xml)
    element[0][0][0].text = id
    element[0][0][1].text = name
    element[0][0][2].text = surname
    element[0][0][3].text = birth_year
    data = ET.tostring(element, encoding="UTF-8")
    request = requests.post("https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx", data=data, headers=headers)
    response_element = ET.fromstring(request.content)
    txt = response_element[0][0][0].text
    if txt == "true":
        return True
    else:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TC Identity Number Check')
    parser.add_argument("id", type=str, help="TC Identity Number")
    parser.add_argument("name", type=str, help="First Name")
    parser.add_argument("surname", type=str, help="Last Name")
    parser.add_argument("birth_year", type=str, help="Birth Year")
    args = parser.parse_args()
    is_valid = query(args.id, args.name, args.surname, args.birth_year)
    print(is_valid)
