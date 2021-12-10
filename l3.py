# -*- coding: utf-8 -*-
# Module: widevine_keys
# Created on: 10.12.2021
# Authors: medvm
# Version: 2.1.0

import base64, requests, sys, xmltodict
import headers
# import cookies
import json
from cdm import cdm, deviceconfig
from base64 import b64encode
from getPSSH import get_pssh
from wvdecryptcustom import WvDecrypt
from cdm.formats import wv_proto2_pb2 as wv_proto2
import logging
# logging.basicConfig(level=logging.DEBUG)

MDP_URL = input('\nInput MPD URL: ')
lic_url = input('License URL: ')
# hardcoded for kinopoisk.ru
# lic_url = 'https://widevine-proxy.ott.yandex.ru/proxy'

pssh = get_pssh(MDP_URL)

# params from mdp_url:
# ottsession=5945048d6f844d1699054cc5d44548f1&
# puid=339572866&
# video_content_id=4315082489d87677b21f7c83593fcb73&

print(f'{chr(10)}PSSH obtained.\n{pssh}')

def WV_Function(pssh, lic_url, cert_b64=None):
	"""main func, emulates license request and then decrypt obtained license
	fileds that changes every new request is signature, expirationTimestamp, watchSessionId, puid, and rawLicenseRequestBase64 """
	wvdecrypt = WvDecrypt(init_data_b64=pssh, cert_data_b64=cert_b64, device=deviceconfig.device_android_generic)                   
	response = requests.post(url=lic_url, headers=headers.headers, data=wvdecrypt.get_challenge())
	if response.status_code == 200:
		widevine_license = response
	elif response.status_code != 200:
		request = b64encode(wvdecrypt.get_challenge())
		response = requests.post(url=lic_url, headers=headers.headers,
		json={
		"rawLicenseRequestBase64": str(request, "utf-8" ), 
		})
		if response.status_code == 200:
			widevine_license = response
		else:
			request = b64encode(wvdecrypt.get_challenge())
			signature = cdm.hash_object
			widevine_license = requests.post(url=lic_url, headers=headers.headers,
			json={
			"rawLicenseRequestBase64": str(request, "utf-8" ), 
			"puid": 				'339572866',
			"watchSessionId": 		'ed0e355063ac48b783130a390dc27ba6',
			"contentId": 			'4315082489d87677b21f7c83593fcb73',
			"contentTypeId": 		'21',
			"serviceName": 			'ott-kp',
			"productId": 			'2',
			"monetizationModel": 	'SVOD',
			"expirationTimestamp": 	'1639009453',
			"verificationRequired": 'false',
			"signature": 			str(signature), 
			# "signature":'b6ca3161c8bd38105e87770458aee16191214cfa', That is fucking amazon aws signing protocol!! V4!!
			"version":				'V4'
			})	
	
	print(f'{chr(10)}license response status: {widevine_license}{chr(10)}')
	if widevine_license.status_code != 200:
		print(f'server did not issue license, check json params in POST request.{chr(10)}')

	try: 
		license_b64 = b64encode(widevine_license.content)
	except TypeError:
		license_b64 = json.loads(widevine_license.content.decode())['license']

	wvdecrypt.update_license(license_b64)
	Correct, keyswvdecrypt = wvdecrypt.start_process()
	if Correct:
		return Correct, keyswvdecrypt   
correct, keys = WV_Function(pssh, lic_url)

for key in keys:
	print('KID:KEY -> ' + key)
