import socket


def serverProgram():
    # get host name
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host,port))  # binding host address and port together

    server_socket.listen(1)  # server socket can listen to one client
    connection, address = server_socket.accept()   # connection is ip and address is port number
    print("Connection from: "+str(address))
    while True:
        # receive data stream
        data = connection.recv(1024).decode()

        if not data:
            #if data is not received
            break
        print("from client->" + data)
        server_message = input("->")
        connection.send(server_message.encode())

    connection.close()


if __name__ == '__main__':
    serverProgram()

