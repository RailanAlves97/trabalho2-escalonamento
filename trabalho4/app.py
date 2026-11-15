import logging, os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
PORT = int(os.environ.get("PORT", "8000"))
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
ENABLE_CRASH = os.environ.get("ENABLE_CRASH", "false").lower() == "true"

logging.basicConfig(level=LOG_LEVEL, stream=sys.stdout,
                    format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("app")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/crash" and ENABLE_CRASH:
            log.error("Falha controlada solicitada. Encerrando com codigo 1")
            logging.shutdown()
            os._exit(1)
        body = f"Servico no ar. PID do processo: {os.getpid()}\n".encode()
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        log.info("requisicao: %s", fmt % args)

if __name__ == "__main__":
    log.info("Iniciando na porta %s (log=%s)", PORT, LOG_LEVEL)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()