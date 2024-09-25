import socket 
import pickle
ip = "127.0.0.1"

def run(port,max_req=10):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((ip,port))

    for i in range (max_req):
        data,address = sock.recvfrom(1024)
        req = pickle.loads(data)

        if req[0]=="REQUEST":
            partition = req[2]
            n=req[5]
            t=req[6]
            s=req[3]
            e=req[4]
            sum,temp=0,0
            for j in range(s,e+1):
                temp = j**t
                sum=sum+temp


            
            resp = [sum,partition,n,t,s,e]
            sock.sendto(pickle.dumps(resp),address)

run(3002,max_req=10)

