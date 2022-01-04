import requests, xmltodict, json, base64

headers2 = {
    'authority': 'ak-jos-c4assets-com.akamaized.net',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'origin': 'https://www.channel4.com',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.channel4.com/',
    'accept-language': 'en-US,en;q=0.9,es;q=0.8,de-DE;q=0.7,de;q=0.6,it;q=0.5',
}



def get_pssh(mpd_url):
    pssh = ''
    all4=0
    kid=""
    try:
        r = requests.get(url=mpd_url)

        r.raise_for_status()
        xml = xmltodict.parse(r.text)
        mpd = json.loads(json.dumps(xml))
        periods = mpd['MPD']['Period']

    except:
        pass
    try: 
        if isinstance(periods, list):
            for idx, period in enumerate(periods):
                if isinstance(period['AdaptationSet'], list):
                    for ad_set in period['AdaptationSet']:
                        if ad_set['@mimeType'] == 'video/mp4':
                            try:
                                for t in ad_set['ContentProtection']:
                                    if t['@schemeIdUri'].lower() == "urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed":
                                        pssh = t["cenc:pssh"]
                            except Exception:
                                pass   
                else:
                    if period['AdaptationSet']['@mimeType'] == 'video/mp4':
                            try:
                                for t in period['AdaptationSet']['ContentProtection']:
                                    if t['@schemeIdUri'].lower() == "urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed":
                                        pssh = t["cenc:pssh"]
                            except Exception:
                                pass   
        else:
            for ad_set in periods['AdaptationSet']:
                    if ad_set['@mimeType'] == 'video/mp4':
                        try:
                            for t in ad_set['ContentProtection']:
                                if t['@schemeIdUri'].lower() == "urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed":
                                    pssh = t["cenc:pssh"]
                        except Exception:
                            pass   
    except Exception:
        pass                      
    if pssh == '':
        print("failed standard method. attempting All4 method")
        all4=1
        r = requests.get(url=mpd_url,headers=headers2)

        r.raise_for_status()
        xml = xmltodict.parse(r.text)
        mpd = json.loads(json.dumps(xml))
        periods = mpd['MPD']['Period']

        try:
            def find_str(s, char):
                index = 0

                if char in s:
                    c = char[0]
                    for ch in s:
                        if ch == c:
                            if s[index:index+len(char)] == char:
                                return index

                        index += 1

                return -1
            teilifis =str(r.content)
            x=find_str(teilifis,"000000")
            stringy=str(r.content)
            y=x+36
            kid= stringy[x:y]
            print("kid is: "+str(kid))
        except:
            pssh = input('Unable to find PSSH in mpd. Edit getPSSH.py or enter PSSH manually: ')
        
    if all4>0:
    
        def get_pssh(keyId):
            array_of_bytes = bytearray( b'\x00\x00\x002pssh\x00\x00\x00\x00')
            array_of_bytes.extend(bytes.fromhex("edef8ba979d64acea3c827dcd51d21ed"))
            array_of_bytes.extend(b'\x00\x00\x00\x12\x12\x10')
            array_of_bytes.extend(bytes.fromhex( keyId.replace("-", "")))
            return base64.b64encode(bytes.fromhex(array_of_bytes.hex()))

        print("kid is:"+str(kid))
        kid = kid.replace('-', '')
        assert len(kid) == 32 and not isinstance(kid, bytes), "wrong KID length"    
        print("PSSH {}".format(get_pssh(kid).decode('utf-8')))
        pssh = get_pssh(kid)
    
    if pssh == '':
        pssh = input(f'\nUnable to find PSSH. cannot access MPD?: {e}. \nEdit getPSSH.py or enter PSSH manually: ')
        return pssh
    
        
    return pssh
    
