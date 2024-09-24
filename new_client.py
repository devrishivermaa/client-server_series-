import socket
import pickle 

ip = "127.0.0.1"
def add_sum(s,p,n,t):
    size = n//5
    r1,r2= p*size, (p+1)*size-1
    req=["REQUEST",1,p,r1,r2,n,t]
    s.sendto(pickle.dumps(req),(ip,3000+p))
    res,address = s.recvfrom(1024)
    return pickle.loads(res)[0] 

def run(n,t):
    sum =0
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    for p in range(5):
        ps = add_sum(sock,p,n,t)
        sum=sum+ps
        
    print("total sum is ", sum)

              
     

if __name__ =="__main__":
    n = 500
    t = 3
    run(n,t)



