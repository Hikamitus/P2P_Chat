
class Server:
    def __init__(self, host = 'localhost', port = 666, username = 'Unknow'):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.myname = username;
        self.host = host;
        self.port = port;
        self.un = 2;
        self.conn = None;
        self.user = None;
        self.msgs = ['Messages'];
        
    def connect(self):
        self.sock.bind(( self.host, self.port ))
        self.sock.listen(self.un)
        self.conn, self.user = self.sock.accept();
        if self.conn and self.user:
            print(f'Conectado com {self.user}');
            return True
    
    def show_msgs(self):
        if system('clear') == 0:
            system('cls')
        for msg in self.msgs:
            print(msg);
    
    def recieve(self):
        while True:
            dados = self.conn.recv(1024)
            if dados and dados != self.msgs[-1]:
                self.msgs.append(dados.decode());
                self.show_msgs();
            else: return
        
    def chat(self):
        self.connect();
        Thread(target = self.recieve).start()
        while True:
            msg = input (' ')
            self.conn.send(f'{self.myname}: {msg}'.encode());
            self.msgs.append('You: %s'%(msg));
                    
from threading import Thread
from os import system
import socket

room = Server(username = 'Server', host = 'localhost', port = 8000);
room.chat()
room.sock.close()
