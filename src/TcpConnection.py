class TCPConnection:
    def __init__(self):
        self.state = 'CLOSED'  # CLOSED, LISTEN, SYN_SENT, ESTABLISHED, etc.
        self.local_addr = None
        self.remote_addr = None
        self.send_seq = 0
        self.recv_seq = 0
        self.send_buffer = []
        self.recv_buffer = []
        self.send_window = 1024  # sliding window size
        self.recv_window = 1024
        self.udp_socket = None
        self.send_thread = None
        self.recv_thread = None