#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Engineering — 24/7 Production Cloud Daemon & Watchdog Service
"""

import subprocess
import time
import sys
import os
import signal
import re

SERVER_SCRIPT = "/opt/legalix/legalix_local_bridge.py"
CLOUDFLARED_BIN = "/usr/local/bin/cloudflared"
LOG_DIR = "/opt/legalix/service_logs"
URL_FILE = "/opt/legalix/CURRENT_TUNNEL_URL.txt"

os.makedirs(LOG_DIR, exist_ok=True)

# Cleanup old processes
subprocess.run("pkill -f legalix_local_bridge; pkill -f cloudflared", shell=True)
time.sleep(1)

server_log = open(os.path.join(LOG_DIR, "server.log"), "a", encoding="utf-8")
tunnel_log = open(os.path.join(LOG_DIR, "tunnel.log"), "a", encoding="utf-8")

def start_server():
    return subprocess.Popen(["/opt/legalix/venv/bin/python3", SERVER_SCRIPT, "8080"], stdout=server_log, stderr=server_log)

def start_tunnel():
    return subprocess.Popen([CLOUDFLARED_BIN, "tunnel", "--url", "http://localhost:8080"], stdout=tunnel_log, stderr=tunnel_log)

def extract_and_save_url():
    log_path = os.path.join(LOG_DIR, "tunnel.log")
    for _ in range(30):
        time.sleep(1)
        if os.path.exists(log_path):
            with open(log_path, "r") as f:
                content = f.read()
                matches = re.findall(r"https://[a-zA-Z0-9.-]+\.trycloudflare\.com", content)
                if matches:
                    latest_url = matches[-1]
                    with open(URL_FILE, "w") as uf:
                        uf.write(latest_url)
                    return latest_url
    return None

def main():
    srv_proc = start_server()
    time.sleep(2)
    tun_proc = start_tunnel()
    
    url = extract_and_save_url()
    if url:
        print(f"\n=======================================================")
        print(f"🚀 LEGALIX LIVE PRODUCTION URL FOR CHATGPT:")
        print(f"{url}")
        print(f"=======================================================\n")
    
    def cleanup(signum, frame):
        srv_proc.terminate()
        tun_proc.terminate()
        sys.exit(0)
        
    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)
    
    while True:
        time.sleep(10)
        if srv_proc.poll() is not None:
            srv_proc = start_server()
        if tun_proc.poll() is not None:
            tun_proc = start_tunnel()
            extract_and_save_url()

if __name__ == '__main__':
    main()
