#TODO: make it as standalone class
#      find information about how to use Models thingy in requests

import constants
import requests
import json

class BattleAnalyzer:
	def __init__(self):
		self.playerTag = 'VJ9QPRP2'
		self.head = {'Authorization':f'Bearer {constants.API_KEY}'}

	def changePlayerTag(self):
		self.playerTag = input('Your player tag (without #): ')

	def getProfileStats(self):
		try:
			pass
		except Exception as e:
			print('There is an error: ', e)

	def getChestCycle(self):
		url = f'https://api.clashroyale.com/v1/players/%23{self.playerTag}/upcomingchests'
		try:
			response = requests.get(url, headers = self.head)
			data = response.json()
			print(data)
			print('Your chest cycle: ')
			for chest in range(0, int(len(data['items']))):
				print(f"{chest + 1} (+{data['items'][chest]['index'] + 1}): {data['items'][chest]['name']}")

		except Exception as e:
			print(f'There is an error. Try again! ({e})')

	def getBattleLog(self):
		url = f'https://api.clashroyale.com/v1/players/%23{self.playerTag}/battlelog'
		try:
			response = requests.get(url, headers = self.head)
			data = response.json()
			print(response.content)
		except Exception as e:
			print(f'There is an error. Try again! ({e})')

if __name__ == '__main__':
	stats = BattleAnalyzer()
	stats.getChestCycle()