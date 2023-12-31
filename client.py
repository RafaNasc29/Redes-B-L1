import os
import socket
import time
HOST = "192.168.1.127"  # The server's hostname or IP address
PORT = 65433  # The port used by the server


try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        result = s.connect((HOST, PORT))
        pid = os.fork()
        if pid > 0:
            while True:
                sendText = ['I', 'g', 'o', 'r',' ','R','a','f','a','e','l',' ', 'G','a','b','r','i','e','l']
                for letter in sendText:
                    s.send(letter.encode())
                    
            # os.waitpid(pid, 0)
            # pgid = os.getpgid(0)
            # os.killpg(pgid, signal.SIGTERM)
finally:
    s.close()
