#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Production 24/7 Cloud Host Runner (Permanent Daemon)
"""
import subprocess, time, sys, os

# Clean logs & processes
subprocess.run("sudo pkill -f cloudflared; sudo pkill -f legalix_local_bridge; sudo rm -f /tmp/server.log /tmp/tunnel.log", shell=True)
time.sleep(1)

# Start bridge
with open("/tmp/server.log", "w") as s_log:
    subprocess.Popen(["sudo", "/opt/legalix/venv/bin/python3", "/opt/legalix/legalix_local_bridge.py", "8080"], stdout=s_log, stderr=subprocess.STDOUT)
time.sleep(2)

# Start cloudflared
with open("/tmp/tunnel.log", "w") as t_log:
    subprocess.Popen(["sudo", "/usr/local/bin/cloudflared", "tunnel", "--url", "http://localhost:8080"], stdout=t_log, stderr=subprocess.STDOUT)

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
    print(f"LEGALIX LIVE PRODUCTION URL FOR CHATGPT:")
    print(f"{url}")
    print("=======================================================\n")
    print("Server is running permanently in background (24/7)!")
else:
    print("Tunnel initialized in background. Check /tmp/tunnel.log")
