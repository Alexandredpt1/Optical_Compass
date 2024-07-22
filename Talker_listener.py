import socket

def listener_bloquant(x):
    HOST = '127.0.0.1'
    PORT = x 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Listener_bloquant : En attente de connexion du script secondaire...')
        conn, addr = s.accept()
        with conn:
            print('Connecté par', addr)
            while True:
                data = conn.recv(1024)
                if data:
                    print('Données reçue:', data.decode())
                    return None
                    
                    
def talker(x):
    HOST = '127.0.0.1'
    PORT = x
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Talker : tentative de connexion")
        s.connect((HOST, PORT))
        s.sendall(b'ok')
        print("succés")


def listener_non_bloquant(x):
    HOST = '127.0.0.1'
    PORT = x
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Listener_non_bloquant : En attente de connexion du script secondaire...')
        s.setblocking(False)
        try:

            conn, addr = s.accept()
            
            with conn:
                print('Connecté par', addr)
                while True:
                    data = conn.recv(1024)
                    if data:
                        print('Données reçue:', data.decode())
                        
                        return False
                    
        except BlockingIOError:
            print("Listener_non_bloquant : Aucune tentative de connexion dans le délai imparti.")
            return True
        
def talker_bloquant(x):
    HOST = '127.0.0.1'
    PORT = x
    a = True
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        while a:

            try:
                print("Talker_bloquant : tentative de connexion")
                s.connect((HOST, PORT))
                s.sendall(b'ok')
                a = False
                print("succés")
                return None

            except:
                print("Talker_bloquant : échec")
                a = True