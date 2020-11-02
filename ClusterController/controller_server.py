from piClusterNetworking import server


class ControllerServer(server.Server):
    def __init__(self, host_ip, host_port):
        super().__init__(host_ip, host_port)
        
    
    def message_handler(self, message):
        try:
            self.send_all(message)

        except Exception as e:
            print(f'message_handler error: {e}')


def main():
    s = ControllerServer("192.168.86.100", 8000)


if __name__ == '__main__':
    main()
