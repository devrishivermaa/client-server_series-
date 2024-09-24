import socket 
import pickle
udp_ip = "127.0.0.1"
udp_port = 3000
def run():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((udp_ip,udp_port))

    while True:
        data,address = sock.recvfrom(1024)
        req = pickle.loads(data)

        if req["operation"]=="ADD":
            res = req["number1"]+req["number2"]
            resp = {"sum":res}
            sock.sendto(pickle.dumps(resp),address)

if __name__ =="__main__":
    run()
