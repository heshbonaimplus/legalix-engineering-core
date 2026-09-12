#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Systemd Service Installer for GCP Ubuntu VM
"""

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

import subprocess
subprocess.run("systemctl daemon-reload && systemctl enable legalix.service && systemctl restart legalix.service", shell=True, check=True)
print("LEGALIX_SYSTEMD_SERVICE_ACTIVE")
