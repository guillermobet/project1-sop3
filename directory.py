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
			request = await self.receive(timeout=1)
			try:
				reply = Message(to=request.sender)
				if request.body == 'findfile':
					reply.body = 'ff listened'
					await self.send(reply)
				elif request.body == 'execfile':
					reply.body = 'ef listened'
					await self.send(reply)
				else:
					self.kill(exit_code=1)
				asyncio.sleep(1)
			except:
				pass

	def setup(self):
		self.behaviour = self.ServerBehaviour()
		self.add_behaviour(self.behaviour)

if __name__ == '__main__':
	peer = Directory('directoryserver@jabb3r.org', 'dirserver')
	peer.start()

	while peer.is_alive():
		try:
			time.sleep(1)
		except KeyboardInterrupt:
			break
	peer.stop()


# directoryserver@jabb3r.org
# dirserver
