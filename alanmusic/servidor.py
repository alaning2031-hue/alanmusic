import http.server, socketserver, os, sys, socket, webbrowser, threading
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8080
RED = '--red' in sys.argv
class H(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, '.webmanifest': 'application/manifest+json', '.js': 'text/javascript', '.svg': 'image/svg+xml'}
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()
    def log_message(self, *a): pass
def ip_local():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8', 80)); ip = s.getsockname()[0]; s.close(); return ip
    except Exception: return None
socketserver.TCPServer.allow_reuse_address = True
try:
    srv = socketserver.ThreadingTCPServer(('0.0.0.0' if RED else '127.0.0.1', PORT), H)
except OSError:
    print('El puerto 8080 ya esta en uso: cierra la otra ventana de AlanMusic y vuelve a abrir.')
    input('Enter para salir'); sys.exit(1)
print('=' * 58)
print('  AlanMusic 3.0 corriendo')
print('  En este PC:   http://localhost:%d' % PORT)
if RED:
    ip = ip_local()
    print('  En tu celular (misma red Wi-Fi):  http://%s:%d' % (ip or 'TU-IP', PORT))
    print('  * Agrega ese origen a tu clave de YouTube en Google Cloud.')
print('  Cierra esta ventana para detenerlo.')
print('=' * 58)
threading.Timer(0.8, lambda: webbrowser.open('http://localhost:%d/' % PORT)).start()
srv.serve_forever()
