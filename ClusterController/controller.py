from piClusterNetworking import client, messages


class Controller(client.Client):
	def __init__(self, server_host, server_port, pi_num):
		super().__init__(server_host, server_port, pi_num)
		self.pi_num = "Controller"
		
	def client_handler(self):
		while True:
			try:
				if self.connected:
					choice = int(input("1 Shutdown\n2 Reboot\n3 Test\nEnter Number: "))
					
					if choice == 1:
						message = messages.create_message("shutdown")
						self.sock.sendall(message)
					
					elif choice == 2:
						message = messages.create_message("reboot")
						self.sock.sendall(message)
						
					elif choice == 3:
						message = messages.create_message("test")
						self.sock.sendall(message)
						
					else:
						print("Invalid input. Try again...")
						continue
						
					print("Message sent to server")
					
				else:
					print("Client disconnected. Trying to reconnect...")
					self.connect()
				
			except Exception as e:
				print(f'controller error: {e}')
				self.connected = False

def main():
	c = Controller("192.168.86.100", 8000, "Controller")


if __name__ == '__main__':
	main()
