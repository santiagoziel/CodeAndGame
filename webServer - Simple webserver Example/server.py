# echo-server.py

import socket, codecs, logging

def process_response(response):
    return (
        'HTTP/1.1 200 ON\r\n'
        f'Content-Length: {len(response)}\r\n'
        'Content-Type: text/html\r\n'
        '\r\n'
        f'{response}'
        '\r\n'
    )

def parse_http(http):
    if not http:
        return ''
    request, *headers, _, body = http.split('\r\n')
    method, path, protocol = request.split(' ')
    headers = dict(
        line.split(':', maxsplit=1)
        for line in headers
    )
    return method, path, protocol, headers, body

request = None
while True:
    try:
        HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        PORT = 5000  # Port to listen on (non-privileged ports are > 1023)
        with socket.socket() as s:
            s.bind((HOST, PORT))
            s.listen(1)
            conn, _ = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024).decode('utf-8')
                    request = parse_http(data)

                    if not data:
                        break
                    print(request[0], request[1])
                    if request[1] == '/':
                        response = codecs.open("hellow.html", 'r').read()
                    elif request[1] == '/about':
                        response = codecs.open("about.html", 'r').read()
                    else:
                        response = codecs.open("404.html", 'r').read()
                    http_reponse = process_response(response)
                    conn.sendall(http_reponse.encode('utf-8'))
    except Exception as e:
        logging.warning(e)
