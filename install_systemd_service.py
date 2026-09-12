#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Systemd Service Installer for GCP Ubuntu VM
"""

import subprocess
import time
import os

SERVICE_CONTENT = """[Unit]
Description=Legalix Engineering Production 24/7 Cloud Host
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/legalix
ExecStart=/opt/legalix/venv/bin/python3 /opt/legalix/legalix_production_daemon.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
"""

with open("/etc/systemd/system/legalix.service", "w") as f:
    f.write(SERVICE_CONTENT)

subprocess.run("systemctl daemon-reload && systemctl enable legalix.service && systemctl restart legalix.service", shell=True, check=True)
print("Systemd service active and running 24/7!")
print("Waiting 5 seconds for Cloudflare URL...")
time.sleep(5)

url_file = "/opt/legalix/CURRENT_TUNNEL_URL.txt"
if os.path.exists(url_file):
    with open(url_file, "r") as f:
        url = f.read().strip()
    print("\n=======================================================")
    print(f"🚀 YOUR PERMANENT LIVE CHATGPT URL:")
    print(f"{url}")
    print("=======================================================\n")
else:
    print("Check /opt/legalix/service_logs/tunnel.log for URL")
