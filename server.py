import socket
import random
HOST = socket.gethostname()#getting computers ip
PORT = 41992 #Port assinged
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #making socket using AF_NET and SOCK_STREAM
 
s.bind((HOST, PORT)) #binding the host and port
s.listen(1) #listing to 1 connection


while True: #infinite loop
    print("Listening for a connection....")
    conn, addr = s.accept()#accepts connection from socket
    print ('Connected by', addr, "at port", PORT)   #display purposes
    num = random.randint(0,2)
    conn.send(bytes(str(num), 'utf-8'))
    
    
    
    
    
    
conn.close
