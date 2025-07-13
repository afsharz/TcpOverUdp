class TcpSegment:
    def __init__(self):
        self.src_port = 0
        self.dst_port = 0
        self.seq_num = 0
        self.ack_num = 0
        self.flags = {'SYN': False, 'ACK': False, 'FIN': False, 'RST': False}
        self.window_size = 0
        self.payload = b''
        self.payload_length = 0