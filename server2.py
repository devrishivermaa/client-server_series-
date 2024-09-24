import socket 
import pickle
udp_ip = "127.0.0.1"
udp_port = 3002
def run():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((udp_ip,udp_port))

    while True:
        data,address = sock.recvfrom(1024)
        req = pickle.loads(data)

        if req["operation"]=="ADD":
            res = req["number"]+2
            resp = {"res":res}
            sock.sendto(pickle.dumps(resp),address)

if __name__ =="__main__":
    run()
