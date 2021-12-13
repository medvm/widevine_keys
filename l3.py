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
from urllib.parse import urlparse
import logging
# logging.basicConfig(level=logging.DEBUG)
MDP_URL = input('\nInput MPD URL: ')
lic_url = input('License URL: ')
# hardcoded for kinopoisk.ru
# lic_url = 'https://widevine-proxy.ott.yandex.ru/proxy'
responses = []
license_b64 = ''
pssh = get_pssh(MDP_URL)
params = None
params = urlparse(lic_url).query
# pssh = 'AAAAXHBzc2gAAAAA7e+LqXnWSs6jyCfc1R0h7QAAADwIARIQ7iYSc3cNGm7XKPe3hSn3MhoIdXNwLWNlbmMiGDdpWVNjM2NOR203WEtQZTNoU24zTWc9PSoAMgA='
# params from mdp_url:
# ottsession=5945048d6f844d1699054cc5d44548f1&
# puid=339572866&
# video_content_id=4315082489d87677b21f7c83593fcb73&

print(f'{chr(10)}PSSH obtained.\n{pssh}')

def WV_Function(pssh, lic_url, cert_b64=None):
	"""main func, emulates license request and then decrypt obtained license
	fileds that changes every new request is signature, expirationTimestamp, watchSessionId, puid, and rawLicenseRequestBase64 """
	wvdecrypt = WvDecrypt(init_data_b64=pssh, cert_data_b64=cert_b64, device=deviceconfig.device_android_generic)                   
	raw_request = wvdecrypt.get_challenge()
	request = b64encode(raw_request)
	signature = cdm.hash_object
# basic, mostly sites works
	responses.append(requests.post(url=lic_url, headers=headers.headers, data=raw_request, params=params))
# some another sites support
	responses.append(requests.post(url=lic_url, headers=headers.headers, params=params, 
		json={
		"rawLicenseRequestBase64": str(request, "utf-8" ), 
		}))
# kakaotv support
	responses.append(requests.post(url=lic_url, headers=headers.headers, params=params, 
		data=f'token={headers.token}&provider={headers.provider}&payload={str(request, "utf-8" )}'
		))
# xfinity.com support
	headers.headers['licenseRequest'] = str(request, "utf-8" )
	responses.append(requests.post(url=lic_url, headers=headers.headers, params=params,
		))
	del headers.headers['licenseRequest']
# rte.ie support
	responses.append(requests.post(url=lic_url, headers=headers.headers, params=params, 
		json={
		"getWidevineLicense": 
			{
			'releasePid': headers.releasePid,
			'widevineChallenge': str(request, "utf-8" )
			}, 
			}))
# kinopoisk support
	responses.append(requests.post(url=lic_url, headers=headers.headers, params=params, 
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
			"version":				'V4'
			}))
	for idx, response in enumerate(responses):
		try:
			str(response.content, "utf-8")
		except UnicodeDecodeError:
			widevine_license = response
			print(f'{chr(10)}license response status: {widevine_license}{chr(10)}')
			break	
		else:
			if len(str(response.content, "utf-8")) > 500:
				widevine_license = response
				print(f'{chr(10)}license response status: {widevine_license}{chr(10)}')
				break
		if idx == len(responses) - 1:
			print(f'{chr(10)}license response status: {response}')
			print(f'server reports: {str(response.content, "utf-8")}')
			print(f'server did not issue license, make sure you have correctly pasted all the required headers in the headers.py. Also check json/raw params of POST request.{chr(10)}')
			exit() 	
		
	lic_field_names = ['license', 'payload', 'getWidevineLicenseResponse']
	lic_field_names2 = ['license']
	
	open('license_content.bin', 'wb').write(widevine_license.content)

	try:
		if str(widevine_license.content, 'utf-8').find(':'):
			for key in lic_field_names:
				try: 
					license_b64 = json.loads(widevine_license.content.decode())[key]
				except:
					pass			
				else:
					for key2 in lic_field_names2:
						try: 
							license_b64 = json.loads(widevine_license.content.decode())[key][key2]
						except:
							pass
		else:
			license_b64 = widevine_license.content								
	except:
		license_b64 = b64encode(widevine_license.content)

	wvdecrypt.update_license(license_b64)
	Correct, keyswvdecrypt = wvdecrypt.start_process()
	if Correct:
		return Correct, keyswvdecrypt   

correct, keys = WV_Function(pssh, lic_url)

for key in keys:
	print('KID:KEY -> ' + key)
