#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys 


class SIPRegisterHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        self.wfile.write(b"Hemos recibido tu peticion")
        print(self.client_address)
        dicc = {}
        print("El cliente nos manda: ", line.decode('utf-8'))
        for line in self.rfile:
            mensaje = line.decode('utf-8')
            if mensaje[0] == 'REGISTER':
            	dicc = {self.client_address[0]: self.client_address[1]}
            	self.wfile.write(b'200 OK')
            	print(dicc)





if __name__ == "__main__":

    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
