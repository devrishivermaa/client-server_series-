import socket
import pickle 

udp_ip = "127.0.0.1"
def run():
    for i in range(5):
        udp_port = 3000+i
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        req = {"operation":"ADD","number":i}
        sock.sendto(pickle.dumps(req),(udp_ip,udp_port))
        res, address = sock.recvfrom(1024)
        res = pickle.loads(res)
        print(f"server{i} num is {res['res']}")

if __name__ =="__main__":
    run()



