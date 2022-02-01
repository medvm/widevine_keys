from bs4 import BeautifulSoup
import requests, xmltodict, json

def __strip_duplicates__(x):
  return list(dict.fromkeys(x))

def __get_pssh_generic__(mpd_url):
    page = requests.get(mpd_url)
    soup = BeautifulSoup(page.text)
    pssh = soup.findAll("cenc:pssh")
    pssh_index = []
    for item in pssh:
        pssh_index.append(item.getText())
    pssh_list = __strip_duplicates__(pssh_index)
    #Display PSSH options
    option_count = 0
    for item in pssh_list:
        print("Option #[" + str(option_count) + "]\n" + item + "\n\n")
        option_count += 1
    select = input("Select Option:")
    return pssh_list[int(select)]

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
        try:
            return __get_pssh_generic__(mpd_url)
        except:
            pssh = input('Unable to find PSSH in mpd. Edit getPSSH.py or enter PSSH manually: ')
    return pssh
