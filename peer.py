import time
import base64
import asyncio
import keyboard

from getpass import getpass

from emoji import emojize
from coolname import generate_slug

from spade.agent import Agent
from spade.message import Message
from spade.template import Template
from spade.behaviour import CyclicBehaviour

def welcome():

		print(emojize('\n\tWelcome to :pear:-to-:pear:!', use_aliases=True))
		print(emojize('\nThe awesome computer-processing :computer:  and file-transfer :cd:  peer-to-peer platform', use_aliases=True))
		print('\nIf you wanna be a super (not-so) secret agent, you gotta sign up into a XMPP server')
		print('If you already have credentials for a XMPP server, please log into your server:')
		jid = input('\nJID: ')
		password = getpass()
		return jid, password

class Peer(Agent):

	class PeerMenu(CyclicBehaviour):
		
		async def on_start(self):

			print('\nAwesome, you\'re now connected to a XMPP server')
			print(emojize('\nSince I\'m a smarty pants, I already know your name, BUT YOU\'RE A (not-so) SECRET AGENT NOW!', use_aliases=True))
			print(emojize('From now on, your super (not-so) secret agent name will be... :game_die: :slot_machine:', use_aliases=True))

			print(emojize('\n\t{}!'.format(self.cool_name).upper() + ' (That\'s funny though :rolling_on_the_floor_laughing:)', use_aliases=True))
			print(emojize('\nSuch an awesome name, {}! You\'re officially a :pear:-to-:pear: super (not-so) secret agent now :detective:'.format(self.cool_name)))

			print(emojize('\nNow, let\'s tell our director Mr. Groovy Bear :bear: that you\'re a new super (not-so) secret agent... (this might take a while, he\'s a busy bear)', use_aliases=True))

		async def run(self):
			print(emojize('\n\t:pear:-to-:pear: menu:\n', use_aliases=True))
			print(emojize('\t:keycap_digit_one:  Search for a file', use_aliases=True))
			print(emojize('\t:keycap_digit_two:  Execute a file', use_aliases=True))
			print(emojize('\t:keycap_digit_nine:  Exit', use_aliases=True))
			
			try:
				action = int(input('\nChoose one of the options: '))

				message = Message(to='directoryserver@jabb3r.org')
				if action == 1:
					message.body = 'sff'
					await self.send(message)
				elif action == 2:
					message.body = 'sef'
					await self.send(message)
				elif action == 9:
					self.kill(exit_code=1)
				elif action is not None:
					print('\nOption unavailable, try again...')
				else:
					pass

			except:
				pass

	class SenderFindFile(CyclicBehaviour):

		async def run(self):
			try:
				message = await self.receive(timeout=1)
				if message.body == 'findfile':
					print('Sender find file')
				else:
					pass
			except:
				pass

	class SenderExecuteFile(CyclicBehaviour):

		async def run(self):
			try:
				message = await self.receive(timeout=1)
				if message.body == 'execfile':
					print('Sender exec file')
				else:
					pass
			except:
				pass

	class ReceiverFindFile(CyclicBehaviour):

		async def run(self):
			try:
				message = await self.receive(timeout=1)
				if message.body == 'findfile':
					print('Receiver find file')
				else:
					pass
			except:
				pass

	class ReceiverExecuteFile(CyclicBehaviour):

		async def run(self):
			try:
				message = await self.receive(timeout=1)
				if message.body == 'execfile':
					print('Receiver exec file')
				else:
					pass
			except:
				pass

	def setup(self):
		self.cool_name = ' '.join(generate_slug(2).split('-'))
		templates = [Template() for i in range(4)]
		types = ['sff', 'sef', 'rff', 'ref']

		for (index, template) in enumerate(templates):
			template.metadata = {'type': types[index]}
		
		menu = self.PeerMenu()
		sff = self.SenderFindFile()
		sef = self.SenderExecuteFile()
		rff = self.ReceiverFindFile()
		ref = self.ReceiverExecuteFile()
		self.add_behaviour(menu)
		self.add_behaviour(sff, templates[0])
		self.add_behaviour(sef, templates[1])
		self.add_behaviour(rff, templates[2])
		self.add_behaviour(ref, templates[3])


if __name__ == '__main__':
	# jid, password = welcome()
	peer = Peer('guillermobet@jabb3r.org', 'guillebeta')
	peer.start()
	peer.web.start(hostname="127.0.0.1", port="10000")

	while peer.is_alive():
		try:
			time.sleep(1)
		except KeyboardInterrupt:
			break
	peer.stop()



'''
	while True:
		try:
			action = int(menu())
			if action == 1:
				pass # do 1
			elif action == 2:
				pass # do 2
			elif action == 9:
				print(emojize('\nWe know being a super (not-so) secret agent is hard :downcast_face_with_sweat:', use_aliases=True))
				print(emojize('\nWe hope to have you someday in another super (not-so) secret mission. Bye! :waving_hand:'))
				exit(0)
			else:
				print('\nI think we don\'t have that option, try again...')
		except ValueError:
			print('\nYikes! It seems like you mistyped your option, try again...')
		except KeyboardInterrupt:
			print('\nForcefully ending agent activity...')
			exit(1)
'''