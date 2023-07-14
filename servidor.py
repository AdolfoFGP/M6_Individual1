from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/landing.html'
        try:
            archivo = open(self.path[1:], 'r')
            archivo_abrir = archivo.read()
            self.send_response(200)
            
        except FileNotFoundError:
            archivo_abrir = 'Archivo no encontrado'
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(archivo_abrir, 'UTF-8'))


PORT = 8000

servidor = HTTPServer(('localhost', PORT), Handler)
print('Servidor conectado al puerto', PORT)
servidor.serve_forever()

