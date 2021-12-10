import requests, xmltodict, json

def get_pssh(mpd_url):
    r = requests.get(url=mpd_url)
    r.raise_for_status()
    xml = xmltodict.parse(r.text)
    mpd = json.loads(json.dumps(xml))
    tracks = mpd['MPD']['Period']['AdaptationSet']
    for video_tracks in tracks:
        if video_tracks['@mimeType'] == 'video/mp4':
            try:
                for t in video_tracks['ContentProtection']:
                    if t['@schemeIdUri'].lower() == "urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed":
                        pssh = t["cenc:pssh"]
            except KeyError:
                for t in video_tracks['Representation'][0]['ContentProtection']:
                    if t['@schemeIdUri'].lower() == "urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed":
                        pssh = t["cenc:pssh"]['#text']
            except TypeError:
                pssh = input('Unable to find PSSH in mpd. Edit getPSSH.py or enter PSSH manually: ')        
    return pssh