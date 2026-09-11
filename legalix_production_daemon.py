#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Engineering — 24/7 Production Cloud Daemon & Watchdog Service
מנהל שרת ה-API ומנהרת הענן האוטונומית של Legalix הפועל 24/7 ברקע עם מנגנון שרידות ו-Auto-Restart
"""

import subprocess
import time
import sys
import os
import signal

SERVER_SCRIPT = "/home/yogi/lod_project/legalix_local_bridge.py"
CLOUDFLARED_BIN = "/home/yogi/bin/cloudflared"
LOG_DIR = "/home/yogi/lod_project/service_logs"

os.makedirs(LOG_DIR, exist_ok=True)

server_log = open(os.path.join(LOG_DIR, "server.log"), "a", encoding="utf-8")
tunnel_log = open(os.path.join(LOG_DIR, "tunnel.log"), "a", encoding="utf-8")

def start_server():
    print("[DAEMON] Starting Legalix Bridge Server on port 8080...")
    return subprocess.Popen([sys.executable, SERVER_SCRIPT], stdout=server_log, stderr=server_log)

def start_tunnel():
    print("[DAEMON] Starting Cloudflare Production Tunnel to port 8080...")
    return subprocess.Popen([CLOUDFLARED_BIN, "tunnel", "--url", "http://localhost:8080"], stdout=tunnel_log, stderr=tunnel_log)

def main():
    print("================================================================================")
    print("🚀 Legalix Engineering 24/7 Production Daemon Started")
    print("================================================================================")
    
    srv_proc = start_server()
    time.sleep(2)
    tun_proc = start_tunnel()
    
    def cleanup(signum, frame):
        print("\n[DAEMON] Shutting down gracefully...")
        srv_proc.terminate()
        tun_proc.terminate()
        sys.exit(0)
        
    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)
    
    while True:
        time.sleep(10)
        # Check server health
        if srv_proc.poll() is not None:
            print("[WATCHDOG ALERT] Bridge server stopped unexpectedly! Restarting...")
            srv_proc = start_server()
            
        # Check tunnel health
        if tun_proc.poll() is not None:
            print("[WATCHDOG ALERT] Cloudflare tunnel stopped unexpectedly! Restarting...")
            tun_proc = start_tunnel()

if __name__ == '__main__':
    main()
