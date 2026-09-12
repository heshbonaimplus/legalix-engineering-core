#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Production 24/7 Cloud Host Runner (Permanent Daemon)
"""
import subprocess, time, sys, os

# Kill any existing processes
subprocess.run("sudo pkill -f cloudflared; sudo pkill -f legalix_local_bridge", shell=True)
time.sleep(1)

# Start bridge on port 8080 in background
subprocess.Popen(["sudo", "nohup", "/opt/legalix/venv/bin/python3", "/opt/legalix/legalix_local_bridge.py", "8080"], stdout=open("/tmp/server.log", "w"), stderr=subprocess.STDOUT)
time.sleep(2)

# Start cloudflared in background writing to /tmp/tunnel.log
subprocess.Popen(["sudo", "nohup", "/usr/local/bin/cloudflared", "tunnel", "--url", "http://localhost:8080"], stdout=open("/tmp/tunnel.log", "w"), stderr=subprocess.STDOUT)

# Read URL from log
print("Connecting Cloudflare Tunnel to Google Cloud...")
url = None
for _ in range(30):
    time.sleep(1)
    if os.path.exists("/tmp/tunnel.log"):
        with open("/tmp/tunnel.log", "r") as f:
            content = f.read()
            for line in content.splitlines():
                if "trycloudflare.com" in line and "https://" in line:
                    for part in line.split():
                        if part.startswith("https://") and "trycloudflare.com" in part:
                            url = part.strip()
                            break
    if url:
        break

if url:
    print("\n=======================================================")
    print(f"🚀 LEGALIX LIVE PRODUCTION URL FOR CHATGPT:")
    print(f"{url}")
    print("=======================================================\n")
    print("Server is running permanently in background (24/7)!")
else:
    print("Tunnel initialized in background. Check /tmp/tunnel.log")
