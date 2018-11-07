import time
import asyncio

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
				if request.metadata['type'] == 'sff':
					file_name = request.body
					files = self.files

					async with self.lock_dict:
						if(files[file_name]==None):
							reply.body = 'file does not exits'
						else:
							old_list = files[file_name]
							new_list = [peer for peer in old_list if self.active[peer]]
							reply.body = ','.join(peer for peer in new_list)
							new_list = files[file_name].append(request.sender)
							files[file_name] = new_list
					await self.send(reply)
				
				elif request.metadata['type'] == 'exit':
					async with self.lock_active:
						self.active[request.sender] = False

				elif request.metadata['type'] == 'enter':
					async with self.lock_active:
						self.active[request.sender] = True

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
		self.files = dict()
		self.active = dict()
		self.lock_dict = asyncio.Lock()
		self.lock_active = asyncio.Lock()

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