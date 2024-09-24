import socket
import pickle 

udp_ip = "127.0.0.1"
udp_port = 3000

def add(num1,num2):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    req = {"operation":"ADD","number1":num1,"number2":num2}
    sock.sendto(pickle.dumps(req),(udp_ip,udp_port))

    response,_ = sock.recvfrom(1024)
    result = pickle.loads(response)

    print(result["sum"])

if __name__=="__main__":
    num1=5
    num2=10
    add(num1,num2)