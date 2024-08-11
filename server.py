import http.server
import socketserver
import subprocess
import os
import webbrowser
import time

PORT = 8000
PROJECT_DIR = 'F:/FinalProject'

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/run_graph_script':
            try:
                result = subprocess.run(['python', os.path.join(PROJECT_DIR, 'graph.py')], capture_output=True, text=True)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(result.stdout.encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(str(e).encode())
        else:
            # Serve the index.html and style.css files
            if self.path == '/':
                self.path = os.path.join(PROJECT_DIR, 'docs', 'index.html')
            elif self.path == '/style.css':
                self.path = os.path.join(PROJECT_DIR, 'docs', 'style.css')
            return super().do_GET()

def open_browser():
    time.sleep(1)  # Wait a bit for the server to start
    webbrowser.open(f'http://localhost:{PORT}')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    open_browser()
    httpd.serve_forever()
