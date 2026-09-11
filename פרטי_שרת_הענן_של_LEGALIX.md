# Legalix Engineering — Master Cloud Production Server Configuration
## שרת הענן הראשי של Legalix ב-Google Cloud (GCP)

---

### 🖥️ פרטי השרת שהוקם ופעיל כעת:
* **שם השרת (Instance Name):** `legalix-master-server`
* **אזור (Zone):** `europe-west3-a` (Frankfurt, Germany)
* **פרויקט (GCP Project):** `legalix-tax`
* **סוג מכונה:** `e2-standard-4` (4 vCPUs, 16GB RAM)
* **דיסק מערכת:** `100 GB SSD (Ubuntu 24.04 LTS)`
* **כתובת IP פנימית:** `10.156.0.2`
* **כתובת IP חיצונית קבועה (EXTERNAL IP):** **`35.242.250.144`**
* **סטטוס:** **`RUNNING (פעיל 24/7/365)`**

---

### 🚀 פקודת התקנה ופריסה אוטונומית של יוגי על שרת הענן:
להרצה ישירה ב-Cloud Shell:

```bash
gcloud compute ssh legalix-master-server --zone=europe-west3-a --command="
sudo apt update && sudo apt install -y python3-pip python3-venv git libreoffice zip && \
sudo git clone https://github.com/heshbonaimplus/legalix-engineering-core.git /opt/legalix && \
sudo python3 -m venv /opt/legalix/venv && \
sudo /opt/legalix/venv/bin/pip install --upgrade pip && \
sudo /opt/legalix/venv/bin/pip install openseespy scipy numpy python-docx mcp requests && \
echo 'Legalix Engineering Core installed successfully on Cloud Server!'
"
```
