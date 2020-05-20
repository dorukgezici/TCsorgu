import xml.etree.ElementTree as ET

import requests

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

headers = {
    'Content-Type': 'application/soap+xml; charset=utf-8',
}


def check_tc_id(id, name, surname, birth_year):
    element = ET.fromstring(xml)
    element[0][0][0].text = str(id)
    element[0][0][1].text = str(name).replace('i', 'İ').upper()
    element[0][0][2].text = str(surname).replace('i', 'İ').upper()
    element[0][0][3].text = str(birth_year)
    data = ET.tostring(element, encoding="UTF-8")

    request = requests.post(
        "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx",
        data=data,
        headers=headers,
    )
    response_element = ET.fromstring(request.content)
    response_txt = response_element[0][0][0].text

    if response_txt == "true":
        return True
    else:
        return False
