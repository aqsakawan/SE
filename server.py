import socket 
import thread
import time
import select


if __name__=="__main__":
    connected_now = []
    count1 = 0
    port= 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1",port))
    s.listen(10)
    shut_down =0

    connected_now.append(s)
    print "Waiting for new connections.."
    
    while 1:
        r,w,e = select.select(connected_now,[],[]) #Help from stackoverflo to solve issue of multithreading
        #checks for incoming data-if they are redable, writable or gives error 
        #this blocks the porgram unless timoeut occurs
        for s_sock in r: #for present sockets in connected_now that are readable
            if s_sock == s: #if there is a server socket that we establised present in connected_now
                client, addr = s.accept() #server accepts the client: fetches the socket and address
                connected_now.append(client) #adds the socket in the connected_now list
                count1= 0 #kind of informal lock 
            else:  
                try:
                    if count1 == 0:
                        name = c_sock.recv(4096)
                        print(name + " Connected to client!") #name over here of client
                        count1= count1+1
                    data = s_sock.recv(4096)
            #prints on server side
                    if data:
                        for socket in connected_now:
                         if socket != s and socket != s_sock:
                            try: 
                                socket.send(data)
                            except:
                                socket.close()
                                connected_now.remove(socket)
                            if data == "quit":
                                socket.close()
                                connected_now.remove(socket)

                except:
                    s_sock.close()
                    connected_now.remove(s_sock)
                    # = 1
                    continue

    s.close()