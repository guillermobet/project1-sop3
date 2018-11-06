import time
import base64
import asyncio

from random import randint

from getpass import getpass

from emoji import emojize
from coolname import generate_slug

from spade.agent import Agent
from spade.message import Message
from spade.behaviour import CyclicBehaviour

class DummyPeer(Agent):

	class Behaviour1(CyclicBehaviour):

		async def run(self):
			sleep = randint(0,5)
			print('Running behaviour 1, sleep is {}'.format(sleep))
			await asyncio.sleep(sleep)

	class Behaviour2(CyclicBehaviour):

		async def run(self):
			sleep = randint(0,5)
			print('Running behaviour 2, sleep is {}'.format(sleep))
			await asyncio.sleep(sleep)
		

	class Behaviour3(CyclicBehaviour):

		async def run(self):
			sleep = randint(0,5)
			print('Running behaviour 3, sleep is {}'.format(sleep))
			await asyncio.sleep(sleep)
		
	class Behaviour4(CyclicBehaviour):

		async def run(self):
			sleep = randint(0,5)
			print('Running behaviour 4, sleep is {}'.format(sleep))
			await asyncio.sleep(sleep)
		
	class Behaviour5(CyclicBehaviour):

		async def run(self):
			sleep = randint(0,5)
			print('Running behaviour 5, sleep is {}'.format(sleep))
			await asyncio.sleep(sleep)

	def setup(self):
		self.behaviour1 = self.Behaviour1()
		self.behaviour2 = self.Behaviour2()
		self.behaviour3 = self.Behaviour3()
		self.behaviour4 = self.Behaviour4()
		self.behaviour5 = self.Behaviour5()
		self.add_behaviour(self.behaviour1)
		self.add_behaviour(self.behaviour2)
		self.add_behaviour(self.behaviour3)
		self.add_behaviour(self.behaviour4)
		self.add_behaviour(self.behaviour5)

if __name__ == '__main__':
	jid = input('JID: ')
	password = getpass()
	peer = DummyPeer(jid, password)
	peer.start()

	while not peer.is_alive():
		try:
			time.sleep(1)
		except KeyboardInterrupt:
			break
	peer.stop()