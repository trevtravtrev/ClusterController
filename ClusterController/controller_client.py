import os
import time
from piClusterNetworking import client

class ControllerClient(client.Client):
    def __init__(self, server_host, server_port):
        super().__init__(server_host, server_port)
        
        
    def message_handler(self, message):
        try:
            if "shutdown" in message:
                print("Shutting down in 5 seconds...")
                time.sleep(5)
                os.system("sudo shutdown -h now")

            elif "reboot" in message:
                print("Rebooting in 5 seconds...")
                time.sleep(5)
                os.system("sudo shutdown -r now")

            elif "test" in message:
                print(f'Test message received: {message.get("test")}')

            else:
                print("Error: function not found in keys.")

        except Exception as e:
            print(f'message_handler error: {e}')


def main():
    c = ControllerClient("192.168.86.100", 8000)

if __name__ == '__main__':
	main()
