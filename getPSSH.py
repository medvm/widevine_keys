import requests, xmltodict, json

def get_pssh(mpd_url):
    pssh = ''
    try:
        r = requests.get(url=mpd_url)
        r.raise_for_status()
        xml = xmltodict.parse(r.text)
        mpd = json.loads(json.dumps(xml))
        periods = mpd['MPD']['Period']
    except Exception as e:
        pssh = input(f'\nUnable to find PSSH in MPD: {e}. \nEdit getPSSH.py or enter PSSH manually: ')
        return pssh
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
        pssh = input('Unable to find PSSH in mpd. Edit getPSSH.py or enter PSSH manually: ')
    return pssh