
# -*- coding: UTF-8 -*-
#from imageai.Prediction import ImagePrediction
import socket
import os
import sys
import struct
import time

i = 0
def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('169.254.55.105', 8088))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    print("Wait")

    while True:
        sock, addr = s.accept()
        deal_data(sock, addr)
        #break
    s.close()


def deal_data(sock, addr):
    print("Accept connection from {0}".format(addr))
    global i
    #i = 0
    while True:
        os.system('fswebcam -S 5 imag'+str(i)+'.jpg')
        filepath = 'imag'+str(i)+'.jpg'
        i = i+1
        fhead = struct.pack(b'128sl', bytes(os.path.basename(filepath).encode('utf-8')), os.stat(filepath).st_size)
        sock.send(fhead)
        print('client filepath: {0}'.format(filepath))
        fp = open(filepath, 'rb')
        while 1:
            data = fp.read(1024)
            if not data:
                print('{0} file send over...'.format(filepath))
                break
            sock.send(data)
            msg = sock.recv(1)
            print(msg)
            if msg == 'A':
                print('rise up')
        sock.close()

        break


if __name__ == '__main__':
    socket_service()
