# מדריך חיבור דומיין קבוע ורשמי (api.legalix.ai / mcp.legalix.ai) לשרת הענן המרכזי
## פרוטוקול חיבור DNS + HTTPS SSL קבוע ב-Google Cloud

---

### 🌐 1. פרטי שרת הענן שלך:
* **כתובת ה-IP החיצונית והקבועה של השרת ב-Google Cloud:**  
  👉 **`35.242.250.144`**

---

### 🛠️ 2. שני השלבים הפשוטים לחיבור הדומיין הקבוע:

#### שלב א' — הגדרת רשומת DNS אצל רשם הדומיינים שלך (Cloudflare / GoDaddy / Namecheap):
היכנס לפאנל הניהול של הדומיין שלך (למשל ב-Cloudflare או אצל הרשם שבו רכשת את הדומיין של Legalix) והוסף רשומת **A Record**:
* **Type (סוג):** `A`
* **Name (שם תת-הדומיין):** `api` (או `mcp`)
* **IPv4 address (כתובת ה-IP):** `35.242.250.144`
* **Proxy status:** `DNS only` (אפור) או `Proxied` (כתום).
* **TTL:** `Auto`

---

#### שלב ב' — התקנת תעודת אבטחה SSL (HTTPS חינמי וקבוע ע״י יוגי בשרת):
ברגע שרשומת ה-DNS מוגדרת, אני מריץ פקודה אחת בשרת שמפעילה שרת Nginx ותעודת SSL של Let's Encrypt:
```bash
sudo certbot --nginx -d api.legalix.ai --non-interactive --agree-tos -m ifat@amarlaw.co.il
```

---

### 🏆 התוצאה:
יהיו לך כתובות MCP קבועות, ממותגות ויציבות לעד:
* 🏗️ **הנדסה:** `https://api.legalix.ai/mcp/engineering`
* 🏛️ **מיסוי:** `https://api.legalix.ai/mcp/taxland`
* ⚖️ **ליטיגציה:** `https://api.legalix.ai/mcp/megacase`
EOF
