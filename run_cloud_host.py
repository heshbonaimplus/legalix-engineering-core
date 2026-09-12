#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Production 24/7 Cloud Host Runner
"""
import subprocess, time, sys, os

# Start bridge on port 8080
p_bridge = subprocess.Popen(["/opt/legalix/venv/bin/python3", "/opt/legalix/legalix_local_bridge.py", "8080"])
time.sleep(2)

# Start cloudflared
p_tunnel = subprocess.Popen(["/usr/local/bin/cloudflared", "tunnel", "--url", "http://localhost:8080"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

for line in p_tunnel.stdout:
    print(line, end='', flush=True)
    if "trycloudflare.com" in line and "https://" in line:
        url = line.strip().split()[-1]
        print(f"\n=======================================================")
        print(f"🚀 LEGALIX LIVE PRODUCTION URL FOR CHATGPT: {url}")
        print(f"=======================================================\n")
        break
