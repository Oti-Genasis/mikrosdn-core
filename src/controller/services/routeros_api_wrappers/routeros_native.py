import socket
import ssl

class RouterOSAPI:
    def __init__(self, host, username, password, port=8729, use_ssl=True):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.use_ssl = use_ssl
        self.sock = None

    def connect(self):
        raw_sock = socket.create_connection((self.host, self.port))
        if self.use_ssl:
            self.sock = ssl.wrap_socket(raw_sock)
        else:
            self.sock = raw_sock

    def login(self):
        # TODO: Implémenter le protocole de login RouterOS (challenge/response)
        pass

    def send_command(self, command):
        # TODO: Encoder la commande selon le protocole RouterOS
        pass

    def close(self):
        if self.sock:
            self.sock.close()