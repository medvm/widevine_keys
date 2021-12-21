import requests

headers = {
    'authority': 'drmtoday.vieon.vn',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'x-dt-custom-data': 'eyJ1c2VySWQiOiIxMi1hZmRjM2Y5Zjc0OTM4YWE4M2JlMmEzMGE4YzA2MGY3NyIsInNlc3Npb25JZCI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUp2Y0dWeVlYUnZjbDlwWkNJNk1USXNJbk5sYzNOcGIyNUpaQ0k2SW1GbVpHTXpaamxtTFRjME9UTXRPR0ZoT0MwelltVXlMV0V6TUdFNFl6QTJNR1kzTnpFMk16a3pNakV3TURraUxDSjBhVzFsYzNSaGJYQWlPakUyTXprek1qRXdNRGtzSW5WelpYSkpaQ0k2SWpFeUxXRm1aR016WmpsbU56UTVNemhoWVRnelltVXlZVE13WVRoak1EWXdaamMzSW4wLmk5dzdYZlZZYWVwTmQyU2t4YWZhRVZRSXJSOXcxbHBxRXJ5WEFldTJjaU0iLCJtZXJjaGFudCI6InFuZXQifQ==',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '/',
    'origin': 'https://vieon.vn',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://vieon.vn/',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
}
params = (
    ('platform', 'BROWSER'),
    ('type', 'MOVIE'),
)
# params inserted below will be passed to data-raw

#All4 requires token and requestid; 

token = 'Q2xsZWdhZnfErPCGT5tK_TtDWlpbJr2NTHVKuNZj-XuWIXKEWgnqNKq3VXo8iNvpefX0PgDgKRN9tR8PFlk9ydqyx6NI4i4UofCGwYDoTFWCs-wVclHsKEjysOVzg4UMm5BEsyVoKAMMH32K8iUkn7Yw9vfWKmBh'
requestid="5291965"

#RTE requires releasePid

releasePid = "_qVpiY31v_oU"

# response = requests.post('https://widevine-proxy.ott.yandex.ru/proxy', headers=headers, cookies=cookies, data=data)
provider = 'kakaotv'
# print(f'{chr(10)}widevine_license: {response.content}')
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.options('https://api.ott.kinopoisk.ru/v12/license-affected-content-metadata?contentIds=4b63db58ab27e92b90a457e533b00007&serviceId=25', headers=headers)
# dash-cenc/hdr10_uhd_hevc_ec3.mpd
# https://strm.yandex.ru/vh-ottenc-converted/vod-content/4315082489d87677b21f7c83593fcb73/8614535x1631802676x41611665-4e76-41ac-93a7-5070b77b5f3c/dash-cenc/sdr_uhd_hevc_ec3.mpd

# 'GET /certificate HTTP/1.1'
