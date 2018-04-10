
import sys
import select
import socket


#input like: python client.py 127.0.0.1 5000
def Main(): 

   
    client_name = raw_input("Write your Name: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5) 

    h = sys.argv[1]
    p = int(sys.argv[2])
    s.connect((h,p))

    print("Connection established")
    count1 = 0; 

    while 1:
        connected_now = [sys.stdin, s]

        for s_sock in connected_now:
            if s_sock == s:
                data = s_sock.recv(1024)
                if not data:
                    s.close()
                    sys.exit()
                else:
                    print data 
            else:
            	print(client_name + ">")
            	if count1 == 0:
            		s.send(client_name)
            		count1= count1 + 1
                msg = raw_input(client_name + ">  ")
                s.send(msg)
                if(msg == 'quit'):
                	s.close()
                	sys.exit
                	break


if __name__=="__main__":
    Main()

