# -*- coding: utf-8 -*-
# Module: KEYS-L3
# Created on: 11-10-2021
# Authors: -∞WKS∞-
# Version: 1.1.0

import base64, requests, sys, xmltodict
import headers
import cookies
import json
from cdm import cdm, deviceconfig
from base64 import b64encode
from getPSSH import get_pssh
from wvdecryptcustom import WvDecrypt
from cdm.formats import wv_proto2_pb2 as wv_proto2

import logging
logging.basicConfig(level=logging.DEBUG)



MDP_URL = input('\nInput MPD URL: ')
# lic_url = input('License URL: ')
# hardcoded for kinopoisk.ru
lic_url = 'https://widevine-proxy.ott.yandex.ru/proxy'

pssh = get_pssh(MDP_URL)
# pssh = 'AAAAZXBzc2gAAAAA7e+LqXnWSs6jyCfc1R0h7QAAAEUIARIQy8Z1jMAZRKm1xt0uRD4eRhoNd2lkZXZpbmVfdGVzdCIgNDMxNTA4MjQ4OWQ4NzY3N2IyMWY3YzgzNTkzZmNiNzM='
# pssh = 'AAAAZXBzc2gAAAAA7e+LqXnWSs6jyCfc1R0h7QAAAEUIARIQy8Z1jMAZRKm1xt0uRD4eRhoNd2lkZXZpbmVfdGVzdCIgNDMxNTA4MjQ4OWQ4NzY3N2IyMWY3YzgzNTkzZmNiNzM='

# params from mdp_url:
# ottsession=5945048d6f844d1699054cc5d44548f1&
# puid=339572866&
# video_content_id=4315082489d87677b21f7c83593fcb73&

print(f'{chr(10)}PSSH obtained.\n{pssh}')

def WV_Function(pssh, lic_url, cert_b64=None):
	"""main func, emulates license request and then decrypt obtained license
	fileds that changes every new request is signature, expirationTimestamp, watchSessionId, puid, and rawLicenseRequestBase64 """
	wvdecrypt = WvDecrypt(init_data_b64=pssh, cert_data_b64=cert_b64, device=deviceconfig.device_android_generic)                   
	# widevine_license = requests.post(url=lic_url, data=wvdecrypt.get_challenge(), headers=headers.headers)
	request = b64encode(wvdecrypt.get_challenge())
	signature = cdm.hash_object
	widevine_license = requests.post(url=lic_url, headers=headers.headers,
		json={
		"rawLicenseRequestBase64": str(request, "utf-8" ), 
		# "rawLicenseRequestBase64": "CAQ=",
		"puid": 				'339572866',
		# "watchSessionId": 		str(cdm.sessionIdTest),
		"watchSessionId": 		'2f3b9d88f052449ab6dfa8be60f58e6d',
		"contentId": 			'4315082489d87677b21f7c83593fcb73',
		"contentTypeId": 		'21',
		"serviceName": 			'ott-kp',
		"productId": 			'2',
		"monetizationModel": 	'SVOD',
		"expirationTimestamp": 	'1638945824',
		"verificationRequired": 'true',
		"signature": 			str(signature), 
		# "signature":'b6ca3161c8bd38105e87770458aee16191214cfa', That is fucking amazon aws signing protocol!! V4!!
		"version":				'V4'

		}
		)
	print(f'{chr(10)}widevine_license: {str(signature)}{chr(10)}')
	print(f'{chr(10)}widevine_license: {widevine_license.content}{chr(10)}')
  
	license_b64 = b64encode(widevine_license.content)
	# license_b64 = json.loads(widevine_license.content.decode())['license']
	wvdecrypt.update_license(license_b64)
	Correct, keyswvdecrypt = wvdecrypt.start_process()
	if Correct:
		return Correct, keyswvdecrypt   
correct, keys = WV_Function(pssh, lic_url)

print()
for key in keys:
	print('--key ' + key)
