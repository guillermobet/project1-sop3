import time
import base64
import asyncio

from getpass import getpass

from emoji import emojize
from coolname import generate_slug

from spade.agent import Agent
from spade.message import Message
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
	
	class PeerBehaviour(CyclicBehaviour):

		def peer_welcome(self):
			self.cool_name = ' '.join(generate_slug(2).split('-'))

			print('\nAwesome, you\'re now connected to a XMPP server')
			print(emojize('\nSince I\'m a smarty pants, I already know your name, BUT YOU\'RE A (not-so) SECRET AGENT NOW!', use_aliases=True))
			print(emojize('From now on, your super (not-so) secret agent name will be... :game_die: :slot_machine:', use_aliases=True))

			print(emojize('\n\t{}!'.format(self.cool_name).upper() + ' (That\'s funny though :rolling_on_the_floor_laughing:)', use_aliases=True))
			print(emojize('\nSuch an awesome name, {}! You\'re officially a :pear:-to-:pear: super (not-so) secret agent now :detective:'.format(self.cool_name)))

			print(emojize('\nNow, let\'s tell our director Mr. Groovy Bear :bear: that you\'re a new super (not-so) secret agent... (this might take a while, he\'s a busy bear)', use_aliases=True))		

		def menu(self):
			print(emojize('\n\t:pear:-to-:pear: menu:\n', use_aliases=True))
			print(emojize('\t:keycap_digit_one:  Search for a file', use_aliases=True))
			print(emojize('\t:keycap_digit_two:  Execute a file', use_aliases=True))
			print(emojize('\t:keycap_digit_nine:  Exit', use_aliases=True))
			return input('\nChoose one of the options above: ')

		async def on_start(self):
			# self.private_key = RSA.generate(2048)
			# self.public_key = self.private_key.publickey()
			# self.directory_public_key, username = self.welcome(cool_name, )
			self.peer_welcome()

		async def run(self):
			action = int(self.menu())
			message = Message(to='directoryserver@jabb3r.org')
			if action == 1:
				message.body = 'file'
				await self.send(message)
			elif action == 2:
				print(message)
				message.body = 'cpu'
				print(message.body)
				await self.send(message)
			elif action == 9:
				self.kill(exit_code=1)
			else:
				print('\nOption unavailable, try again...')
			await asyncio.sleep(1)

	def setup(self):
		self.behaviour = self.PeerBehaviour()
		self.add_behaviour(self.behaviour)

if __name__ == '__main__':
	jid, password = welcome()
	peer = Peer(jid, password)
	peer.start()

	while not peer.behaviour.is_killed():
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