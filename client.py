import os
import socket
import time
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65433  # The port used by the server


try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        result = s.connect((HOST, PORT))
        pid = os.fork()
        if pid > 0:
            count = 0
            while True:
                count += 1
                s.sendto(f'{count}'.encode(), (HOST, PORT))
                time.sleep(2)
                if(count == 9): count = 0
            # os.waitpid(pid, 0)
            # pgid = os.getpgid(0)
            # os.killpg(pgid, signal.SIGTERM)
finally:
    s.close()
