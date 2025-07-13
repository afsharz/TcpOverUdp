import socket

class TcpServer:
    def __init__(self):
        self.udp_socket = self.udp_socket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        self.bound_addr = None
        self.connections = {} 
        self.accept_queue = [] 
        self.is_listening = False
        self.receiver_thread = None

    def bind(self,addr:str,port:int):
        self.udp_socket.bind((addr,port))   
        print(f"UDP server bound to {addr} : {port}")


    def listen(self,queue_size=10):
        self.queue_size=queue_size

        while 1:
            pass


    def accept(self):
        pass