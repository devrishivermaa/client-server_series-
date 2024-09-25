import socket 
import pickle
ip = "127.0.0.1"

def run(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((ip,port))

    while True:
        data,address = sock.recvfrom(1024)
        req = pickle.loads(data)

        if req[0]=="REQUEST":
            partition = req[2]
            n=req[5]
            t=req[6]
            s=req[3]
            e=req[4]
            sum,temp=0,0
            for i in range(s,e+1):
                temp = i**t
                sum=sum+temp


            
            resp = [sum,partition,n,t,s,e]
            sock.sendto(pickle.dumps(resp),address)


run(3000)

