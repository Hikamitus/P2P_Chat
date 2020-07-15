class Client:
    def __init__(self, host = '127.0.0.1', port = 8080, username='Unknown'):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.myname = username;
        self.host = host;
        self.port = port;
        self.conn = None;
        self.user = None;
        self.msgs = ['Messages'];
        
    def connect(self):
        self.sock.connect(( self.host, self.port ))
        if self.sock:
            print('Conectado com %s'%(self.sock));
            return True
        else:
            return False
    
    def show_msgs(self):
        try:
            system('clear');
        except:
            system('cls');
        for msg in self.msgs:
            print(msg);
    
    def recieve(self):
        while True:
            dados = self.sock.recv(1024)
            if dados and dados != self.msgs[-1]:
                self.msgs.append('%s'%(dados.decode()));
                self.show_msgs();
                     
    def chat(self):
        self.connect()
        try:
            Thread(target = self.recieve).start()
        except: print(Exception ())
        while True:
            msg = input(' ');
            self.sock.send(f'{self.myname}: {msg}'.encode());
            self.msgs.append(f'You: {msg}');

from threading import Thread, Lock
from os import system
import socket

room = Client(username='Client', host='localhost', port=8000);
room.chat()
