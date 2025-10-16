 This covers **Linux** and **macOS** users beginner-friendly guidance on Linux/macOS troubleshooting section 👇

---

## 🐧 **Common Issues & Fixes (Linux & macOS Users)**

### ⚠️ **1. “Address already in use”**

**Reason:**
Another process is already using the port you selected (e.g., 80 or 8080).

**Fix:**
Run this command to check what’s using the port:

```bash
sudo lsof -i :8080
```

Then kill that process (replace `<PID>` with the process ID):

```bash
sudo kill <PID>
```

Now restart your `rose_server` — it should run fine!

---

### 🔒 **2. “Permission denied” when using port 80**

**Reason:**
Just like Windows, ports below **1024** require *root (admin)* privileges.

**Fix:**
Either run the app with:

```bash
sudo python3 rose_server.py
```

or use a higher port like **8080**, **8888**, or **9000** — these don’t need root privileges.

---

### 🧱 **3. Firewall blocking connections (UFW / iptables)**

**Reason:**
Your system firewall may be blocking the HTTP port.

**Fix (UFW):**

```bash
sudo ufw allow 8080/tcp
sudo ufw reload
```

**Fix (iptables):**

```bash
sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
```

After that, restart your server — it should be reachable on your local network!

---

### 🌐 **4. Can’t access server from other devices (on same LAN)**

**Reason:**
By default, `localhost` binds to the local machine only.

**Fix:**
Start the server using `0.0.0.0` as the host — that makes it accessible to other devices on the same Wi-Fi/LAN:

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

Or if your app has a “Public Mode” toggle, enable that option.

Then visit from another device using:

```
http://<your_computer_IP>:8080
```

---

### 📁 **5. “Access denied” or “No permission to read directory”**

**Reason:**
You may not have read access to the folder you’re serving.

**Fix:**
Use a directory inside your **Home folder**, like:

```
/home/username/Desktop
```

Avoid system directories (like `/root` or `/etc`) unless you know what you’re doing.

---

### 💡 **Pro Tip**

Keep your ports above **1024**, avoid using `sudo` unless necessary,
and double-check firewall settings if your browser says *“This site can’t be reached.”*

---

