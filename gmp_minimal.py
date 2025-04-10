import socket
import logging

# Configure logging (adjust level to logging.INFO or logging.ERROR to reduce verbosity)
logging.basicConfig(level=logging.INFO, format='%(message)s')

def read_until_done(sock):
    buffer, results = b"", []
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            logging.debug("Connection closed by server.")
            break
        buffer += chunk

        if b"ACK\r\n" in buffer:
            buffer = buffer.split(b"ACK\r\n", 1)[1]
            logging.debug("ACK received.")

        if b"DONE" in buffer:
            segment, _, buffer = buffer.partition(b"DONE")
            if segment:
                decoded_segment = segment.decode().strip()
                results.append(decoded_segment)
                logging.debug(f"Result segment: {decoded_segment}")
            logging.debug("DONE marker found.")
            break

    return results

def ask_PV(*args):
    command = chr(1).join(args)#"-gmp"+chr(1)+"x\r\n"# f"-gmp"+chr(1)+value
    if not command.endswith('\r\n'):
        command += '\r\n'    
    print(command)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect(("127.0.0.1",1236))
        sock.sendall(command.encode())
        results = read_until_done(sock)
        print(f" {args}, {results}")    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.sendall("-x".encode())
        sock.close()
        
#ask_PV('-gmp','x')
ask_PV('-pg', '3','400')
#ask_PV('-x')
