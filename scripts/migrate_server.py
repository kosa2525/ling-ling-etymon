import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html><head><meta charset="utf-8"></head><body>
            <script>
            // Mock DOM elements needed by app.js so it doesn't crash on load
            document.body.innerHTML = '<div id="view-container"></div><input id="global-search-input"/><div id="nav-today"></div><div id="nav-archive"></div><div id="nav-saved"></div><div id="nav-premium"></div>';
            </script>
            <script src="/app.js"></script>
            <script>
            fetch('/save', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(WORDS)
            }).then(() => {
                document.body.innerHTML += "<h2>Saved successfully!</h2>";
                window.close();
            });
            </script>
            </body></html>
            """
            self.wfile.write(html.encode("utf-8"))
        elif self.path == '/app.js':
            self.send_response(200)
            self.send_header('Content-Type', 'application/javascript; charset=utf-8')
            self.end_headers()
            with open('../app.js', 'r', encoding='utf-8') as f:
                self.wfile.write(f.read().encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/save':
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)
            os.makedirs('../data', exist_ok=True)
            with open('../data/words.json', 'wb') as f:
                f.write(data)
            self.send_response(200)
            self.end_headers()
            print("Migration completely successful! You can safely terminate me.")
            threading.Timer(1, self.server.shutdown).start()

print("Starting server on port 8080...")
server = HTTPServer(('127.0.0.1', 8080), Handler)
server.serve_forever()
