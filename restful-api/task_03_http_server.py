#!/usr/bin/python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type='text/plain'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self._set_headers(200, 'application/json')
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self._set_headers()
            self.wfile.write(b"OK")
        else:
            self._set_headers(404, 'text/plain')
            self.wfile.write(b"Endpoint not found")

    def do_POST(self):
        self._set_headers(405)
        self.wfile.write(b"Method Not Allowed")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()

