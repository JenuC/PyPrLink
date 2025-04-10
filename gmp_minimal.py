import socket

def read_until_done(sock,debug=False):
    buffer, results = b"", []
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            print("Connection closed by server.")
            break
        buffer += chunk

        if b"ACK\r\n" in buffer:
            buffer = buffer.split(b"ACK\r\n", 1)[1]
            print("ACK received.")

        if b"DONE" in buffer:
            segment, _, buffer = buffer.partition(b"DONE")
            if segment:
                results.append(segment.decode().strip())
                print(f"Result segment: {segment.decode().strip()}")
            print("DONE marker found.")
            break

    return results



try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect(("127.0.0.1",1236))
    command = "-gmp"+chr(1)+"x\r\n"# f"-gmp"+chr(1)+value
    #print(command,command.encode('ascii'),f'{command.encode('ascii')}')
    sock.sendall(command.encode())
    
    # response = sock.recv(1024)
    # print(response.decode())
    # response = sock.recv(1024)
    # print(response.decode())
    # response = sock.recv(1024)
    # print(response.decode())
    
    results = read_until_done(sock)
    print(f"Final results: {results}")
    
except Exception as e:
    print(f"Error: {e}")
finally:
    sock.close()
    
    