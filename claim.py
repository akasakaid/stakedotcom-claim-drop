
# date : 12/03/2022
# change author not make you a programmer !
# follow my github : https://github.com/AkasakaID

import os
import sys
import time
import json
from datetime import datetime
try:
	import requests
except ImportError:
	sys.exit("- module not installed !")

garis = "- " * 30

def akasakaid_captcha():
	key = open("key.txt").read()
	if len(key) == 0:
		sys.exit("- isi key anti-captcha dulu bang!")
	data = {"clientKey":key,"task":{"type":"HCaptchaTaskProxyless","websiteURL":"https://stake.games","websiteKey":"7830874c-13ad-4cfe-98d7-e8b019dc1742"}}
	rena = requests.post("https://api.anti-captcha.com/createTask",json=data).json()
	if rena["errorId"] != 0:
		sys.exit(rena)
	elif rena["errorId"] == 0:
		kamu = rena["taskId"]
		while True:
			data = {"clientKey":key,"taskId":kamu}
			iofi = requests.post("https://api.anti-captcha.com/getTaskResult",json=data).json()
			if iofi["errorId"] == 0 and iofi["status"] == "ready":
				return iofi["solution"]["gRecaptchaResponse"]
			elif iofi["errorId"] != 0:
				sys.exit(iofi)
			elif iofi["status"] == "processing":
				time.sleep(5)
				continue

def claim(token,akasakaid_code):
	coin = open("coin.txt","r").read()
	if len(coin) == 0:
		sys.exit("- mau claim coin apa bang? di isi dulu file coin.txt")
	akasakaid_data = {"query":"mutation ClaimConditionBonusCode($code: String!, $currency: CurrencyEnum!, $captcha: String!) {\n  claimConditionBonusCode(code: $code, currency: $currency, captcha: $captcha) {\n    bonusCode {\n      id\n      code\n      __typename\n    }\n    amount\n    currency\n    user {\n      id\n      balances {\n        available {\n          amount\n          currency\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n","operationName":"ClaimConditionBonusCode","variables":{"code":akasakaid_code,"currency":coin,"captcha":akasakaid_captcha()}}
	akasakaid_url = "https://api.stake.games/graphql"
	akasakaid_headers = {
		"accept": "*/*",
		"accept-language": "en-US,en;q=0.9",
		"content-length": str(len(str(akasakaid_data))),
		"content-type": "application/json",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
		"x-access-token": token,
		"x-language": "en"
	}
	akasakaid_mine = requests.post(akasakaid_url,headers=akasakaid_headers,json=akasakaid_data)
	open("hasil.json","a+").write(akasakaid_mine.text + "\n")
	if "You have already claimed this bonus code" in akasakaid_mine.text:
		print("- you've already claimed this code !")
		return
	elif "errors" in akasakaid_mine.text and akasakaid_mine.json()["data"] == None:
		print(f"- error : " + akasakaid_mine.json()['errors'][0]['message'])
		return
	elif akasakaid_mine.json()["data"] != None:
		akasakaid_reward = akasakaid_mine.json()["data"]["claimConditionBonusCode"]["amount"]
		print("- bonus amount " + akasakaid_reward)
		for bagian_akasakaid in akasakaid_mine.json()["data"]["claimConditionBonusCode"]["user"]["balances"]:
			if bagian_akasakaid["available"]["currency"] == coin:
				print(f"- account balance " + bagian_akasakaid['available']['amount'] + " " + bagian_akasakaid["available"]["currency"])
				break
		return

def main():
	os.system("cls" if os.name == "nt" else "clear")
	if len(akasakaid_sayang_siska) == 0:
		sys.exit("- enter the account token first !")
	akasakaid_code = input('- enter drop code : ')
	akasakaid_sayang_siska = open("token.txt").read().splitlines()
	print(f"- total accounts : {len(akasakaid_sayang_siska)}")
	print()
	for akasakaid_sayang_etna,akasakaid_sayang_mika in enumerate(akasakaid_sayang_siska):
		print(f"- akun ke {akasakaid_sayang_etna+1}/{len(akasakaid_sayang_siska)}")
		claim(akasakaid_sayang_mika,akasakaid_code)
		print(garis)
		time.sleep(2)

def set_up():
		if not os.path.exists('token.txt'):
			open('token.txt','a+')
		if not os.path.exists('key.txt'):
			open('key.txt','a+')
		if not os.path.exists('coin.txt'):
			open('coin.txt','a+')
		if len(open('token.txt').read().splitlines()) == 0:
			print('- enter the account token first !')
			sys.exit()
		if len(open('key.txt').read()) == 0:
			print('- enter the key anti-captcha first !')
			sys.exit()
		if len(open('coin.txt').read()) == 0:
			print('- enter the type of coin you want to claim !')
			sys.xit()

if __name__ == '__main__':
	try:
		set_up()
		main()
	except KeyboardInterrupt:
		sys.exit()