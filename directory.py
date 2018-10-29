import time

from spade.agent import Agent
from spade.message import Message
from spade.behaviour import CyclicBehaviour

from emoji import emojize

class Directory(Agent):

	class ServerBehaviour(CyclicBehaviour):

		async def on_start(self):
			print('\nServer running...')

		async def run(self):
			message = await self.receive(timeout=1)
			try:
				if message.body == 'file':
					print('It\'s file!')
				elif message.body == 'cpu':
					print('It\'s cpu!')
				else:
					self.kill(exit_code=1)
				asyncio.sleep(1)
			except:
				pass

	def setup(self):
		self.behaviour = self.ServerBehaviour()
		self.add_behaviour(self.behaviour)

if __name__ == '__main__':
	peer = Directory('foo', 'bar')
	peer.start()

	while not peer.behaviour.is_killed():
		try:
			time.sleep(1)
		except KeyboardInterrupt:
			break
	peer.stop()


# directoryserver@jabb3r.org
# dirserver