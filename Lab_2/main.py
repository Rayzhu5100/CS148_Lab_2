
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)  # Prepare a sever socket
serverPort = 443

serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is now ready to receive")

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        message.decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        message = "\nHTTP\1.1 200 OK\n"
        connectionSocket.send(message.encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        message_error = ('\nHTTP\1.1 404 Not Found\n')
        print("Inside Exception")
        connectionSocket.send(message_error.encode())
        connectionSocket.close()
serverSocket.close()
sys.exit()