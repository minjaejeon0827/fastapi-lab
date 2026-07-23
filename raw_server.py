# raw_server.py
# 터미널 실행 명령어: python raw_server.py
# 다른 터미널 실행 명령어
# curl http://localhost:8000/health

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("서버 실행 중: http://localhost:8000")
server.serve_forever()

# 아래 주석친 소스코드 필요 시 참고(2026.07.22 minjae)
# class Handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == "/health":
#             self.send_response(200)
#             self.send_header("Content-Type", "application/json")
#             self.end_headers()
#             self.wfile.write(json.dumps({"status": "ok"}).encode())
#         elif self.path.startswith("/tasks/"):
#             # 경로에서 할 일 ID를 수동으로 잘라내야 함
#             task_id = self.path.split("/tasks/")[1]
#             self.send_response(200)
#             self.send_header("Content-Type", "application/json")
#             self.end_headers()
#             self.wfile.write(json.dumps({"task_id": task_id}).encode())
#         else:
#             self.send_response(404)
#             self.end_headers()