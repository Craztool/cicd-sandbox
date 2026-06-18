from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        html = (
            "<html><body><h1>Привет от CI/CD Sandbox V2!</h1>"
            "<p>ArgoCD управляет миром!</p></body></html>"
        )
        self.wfile.write(html.encode('utf-8'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Сервер запущен на порту {port}")
    server = HTTPServer(("", port), SimpleServer)
    server.serve_forever()
