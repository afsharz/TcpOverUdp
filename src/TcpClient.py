import socket
import random

class TcpClient:
    def __init__(self):
        self.udp_socket = self.udp_socket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        #random_port=random.randint(100,65535)
        #self.udp_socket.bind(("0.0.0.0",random_port))
        self.bound_addr = None
        self.connection = None  
        self.is_listening = False
        self.receiver_thread = None

    def bind(self,addr:str,port:int):
        self.udp_socket.bind((addr,port))   
        print(f"UDP server bound to {addr} : {port}")


    def connect(self,addr:str,port:int):
        pass
    