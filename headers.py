import requests

headers = {
    'authority': 'cms.35mm.online',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'origin': 'https://35mm.online',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://35mm.online/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,id;q=0.6,de;q=0.5,zh-TW;q=0.4,zh-CN;q=0.3,zh;q=0.2,uk;q=0.1',
}

params = (
    ('platform', 'BROWSER'),
    ('type', 'MOVIE'),
)

# response = requests.post('https://widevine-proxy.ott.yandex.ru/proxy', headers=headers, cookies=cookies, data=data)

# print(f'{chr(10)}widevine_license: {response.content}')
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.options('https://api.ott.kinopoisk.ru/v12/license-affected-content-metadata?contentIds=4b63db58ab27e92b90a457e533b00007&serviceId=25', headers=headers)
# dash-cenc/hdr10_uhd_hevc_ec3.mpd
# https://strm.yandex.ru/vh-ottenc-converted/vod-content/4315082489d87677b21f7c83593fcb73/8614535x1631802676x41611665-4e76-41ac-93a7-5070b77b5f3c/dash-cenc/sdr_uhd_hevc_ec3.mpd

# 'GET /certificate HTTP/1.1'
