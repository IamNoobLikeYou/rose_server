import subprocess
import webbrowser
import tkinter as tk
from tkinter import messagebox, filedialog
import os

server_process = None
animation_id = None

def start_server():
    global server_process
    port = port_entry.get().strip() or "8000"
    directory = dir_entry.get().strip() or os.getcwd()

    if server_process:
        messagebox.showinfo("Already Running", "Server is already running!")
        return

    # Validate port
    try:
        port_num = int(port)
        if not (1 <= port_num <= 65535):
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Port", "Please enter a valid port number (1–65535).")
        return

    # Validate directory
    if not os.path.isdir(directory):
        messagebox.showerror("Invalid Directory", "Please select a valid directory path.")
        return

    try:
        # Start the HTTP server in the specified directory (cross-platform)
        # Detect Python command (python3 for Linux/Mac, python for Windows)
        python_cmd = "python3" if os.name != "nt" else "python"
        
        # Platform-specific configuration
        if os.name == "nt":  # Windows
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
            
            server_process = subprocess.Popen(
                [python_cmd, "-m", "http.server", str(port_num)],
                cwd=directory,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                startupinfo=startupinfo,
                creationflags=subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP
                if hasattr(subprocess, "CREATE_NO_WINDOW")
                else subprocess.CREATE_NEW_PROCESS_GROUP
            )
        else:  # Linux/Mac
            server_process = subprocess.Popen(
                [python_cmd, "-m", "http.server", str(port_num)],
                cwd=directory,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True  # Unix equivalent of CREATE_NEW_PROCESS_GROUP
            )

        status_label.config(text=f"🟢 Server running on port {port_num}", fg="#00ff88")
        start_animation()
        webbrowser.open(f"http://localhost:{port_num}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start server: {e}")

def stop_server():
    global server_process
    if server_process:
        try:
            server_process.terminate()
            server_process.wait(timeout=2)
            server_process = None
            stop_animation()
            status_label.config(text="🔴 Server stopped", fg="#ff5555")
            messagebox.showinfo("Stopped", "Server stopped successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop server: {e}")
    else:
        messagebox.showinfo("No Server", "No server is running currently.")

def browse_directory():
    directory = filedialog.askdirectory(title="Select Directory for Server")
    if directory:
        dir_entry.delete(0, tk.END)
        dir_entry.insert(0, directory)

def start_animation():
    global animation_id
    colors = ["#00ff88", "#00dd77", "#00bb66", "#00dd77"]
    current = [0]
    
    def animate():
        status_label.config(fg=colors[current[0] % len(colors)])
        current[0] += 1
        animation_id = root.after(500, animate)
    
    animate()

def stop_animation():
    global animation_id
    if animation_id:
        root.after_cancel(animation_id)
        animation_id = None

def animate_name():
    colors = ["#ff6b6b", "#ff8787", "#ffa3a3", "#ff8787", "#ff6b6b", "#ff5252"]
    current = [0]
    
    def fade():
        name_label.config(fg=colors[current[0] % len(colors)])
        current[0] += 1
        root.after(800, fade)
    
    fade()

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, bg_color="#00ffaa", hover_color="#00dd88", 
                 text_color="#000000", width=150, height=45, radius=15):
        tk.Canvas.__init__(self, parent, width=width, height=height, 
                          bg="#0f0f0f", highlightthickness=0)
        
        self.command = command
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.width = width
        self.height = height
        self.radius = radius
        
        self.rect = self.create_rounded_rect(0, 0, width, height, radius, fill=bg_color)
        self.text = self.create_text(width/2, height/2, text=text, 
                                     font=("Segoe UI", 11, "bold"), fill=text_color)
        
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)
    
    def create_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, 
            x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2,
            x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2,
            x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)
    
    def on_enter(self, e):
        self.itemconfig(self.rect, fill=self.hover_color)
    
    def on_leave(self, e):
        self.itemconfig(self.rect, fill=self.bg_color)
    
    def on_click(self, e):
        if self.command:
            self.command()

class RoundedEntry(tk.Canvas):
    def __init__(self, parent, default_text="", width=250, height=40, radius=12):
        tk.Canvas.__init__(self, parent, width=width, height=height, 
                          bg="#0f0f0f", highlightthickness=0)
        
        self.width = width
        self.height = height
        self.radius = radius
        
        # Create rounded rectangle background
        self.rect = self.create_rounded_rect(0, 0, width, height, radius, 
                                             fill="#1a1a1a", outline="#333333", width=2)
        
        # Create entry widget
        self.entry = tk.Entry(self, font=("Consolas", 11), justify="center",
                             bg="#1a1a1a", fg="#00ffaa", insertbackground="#00ffaa",
                             bd=0, highlightthickness=0)
        self.entry.insert(0, default_text)
        
        self.create_window(width/2, height/2, window=self.entry, width=width-20)
        
        self.entry.bind("<FocusIn>", self.on_focus_in)
        self.entry.bind("<FocusOut>", self.on_focus_out)
    
    def create_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, 
            x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2,
            x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2,
            x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)
    
    def on_focus_in(self, e):
        self.itemconfig(self.rect, outline="#00ffaa", width=2)
    
    def on_focus_out(self, e):
        self.itemconfig(self.rect, outline="#333333", width=2)
    
    def get(self):
        return self.entry.get()
    
    def delete(self, first, last):
        self.entry.delete(first, last)
    
    def insert(self, index, string):
        self.entry.insert(index, string)

# ------------------ UI ------------------
root = tk.Tk()
root.title("⚡ Local HTTP Server Launcher ⚡")
root.geometry("480x480")
root.resizable(False, False)
root.configure(bg="#0f0f0f")

# Set window icon (change 'icon.ico' to your icon file path)
try:
    root.iconbitmap("icon.ico")
except:
    pass  # If icon file not found, use default

# Title
title_label = tk.Label(root, text="🕸️ Python HTTP Server Launcher", 
                       font=("Segoe UI", 15, "bold"),
                       fg="#00ffaa", bg="#0f0f0f")
title_label.pack(pady=20)

# Port input section
port_frame = tk.Frame(root, bg="#0f0f0f")
port_frame.pack(pady=10)
tk.Label(port_frame, text="Port:", font=("Segoe UI", 12, "bold"), 
         fg="#ffffff", bg="#0f0f0f").pack(anchor="w", padx=5)
port_entry = RoundedEntry(port_frame, default_text="8000", width=200, height=40)
port_entry.pack(pady=5)

# Directory input section
dir_frame = tk.Frame(root, bg="#0f0f0f")
dir_frame.pack(pady=10)
tk.Label(dir_frame, text="Directory:", font=("Segoe UI", 12, "bold"), 
         fg="#ffffff", bg="#0f0f0f").pack(anchor="w", padx=5)

dir_input_frame = tk.Frame(dir_frame, bg="#0f0f0f")
dir_input_frame.pack(pady=5)

dir_entry = RoundedEntry(dir_input_frame, default_text=os.getcwd(), width=280, height=40)
dir_entry.pack(side=tk.LEFT, padx=5)

browse_btn = RoundedButton(dir_input_frame, "📁", browse_directory, 
                          bg_color="#333333", hover_color="#444444", 
                          width=45, height=40, radius=12)
browse_btn.pack(side=tk.LEFT)

# Buttons
btn_frame = tk.Frame(root, bg="#0f0f0f")
btn_frame.pack(pady=20)

start_btn = RoundedButton(btn_frame, "🚀 Start Server", start_server, 
                         bg_color="#00ffaa", hover_color="#00dd88", width=160, height=50)
start_btn.pack(side=tk.LEFT, padx=10)

stop_btn = RoundedButton(btn_frame, "✕ Stop Server", stop_server, 
                        bg_color="#ff3333", hover_color="#ff6666", 
                        text_color="#ffffff", width=160, height=50)
stop_btn.pack(side=tk.LEFT, padx=10)

# Status
status_label = tk.Label(root, text="🔴 Server not running", 
                       font=("Segoe UI", 12, "bold"),
                       fg="#ff5555", bg="#0f0f0f")
status_label.pack(pady=15)

# Footer - Created By
footer_frame = tk.Frame(root, bg="#0f0f0f")
footer_frame.pack(pady=15)

tk.Label(footer_frame, text="Created By ", font=("Segoe UI", 10), 
         fg="#888888", bg="#0f0f0f").pack(side=tk.LEFT)

name_label = tk.Label(footer_frame, text="r0se4U", font=("Segoe UI", 10, "bold"), 
                      fg="#ff6b6b", bg="#0f0f0f")
name_label.pack(side=tk.LEFT)

tk.Label(footer_frame, text=" with love", font=("Segoe UI", 10), 
         fg="#888888", bg="#0f0f0f").pack(side=tk.LEFT)

# Start name animation
animate_name()

# Footer
footer_frame = tk.Frame(root, bg="#0f0f0f")
footer_frame.pack(side=tk.BOTTOM, pady=10)

tk.Label(footer_frame, text="Created By ", font=("Segoe UI", 9), 
         fg="#666666", bg="#0f0f0f").pack(side=tk.LEFT)

name_label = tk.Label(footer_frame, text="r0se4U", font=("Segoe UI", 9, "bold"), 
                      fg="#ff6b6b", bg="#0f0f0f")
name_label.pack(side=tk.LEFT)

tk.Label(footer_frame, text=" with love", font=("Segoe UI", 9), 
         fg="#666666", bg="#0f0f0f").pack(side=tk.LEFT)

# Start name animation
animate_name()

# Footer
footer_frame = tk.Frame(root, bg="#0f0f0f")
footer_frame.pack(side=tk.BOTTOM, pady=10)

tk.Label(footer_frame, text="Created By ", font=("Segoe UI", 9), 
         fg="#666666", bg="#0f0f0f").pack(side=tk.LEFT)

name_label = tk.Label(footer_frame, text="r0se4U", font=("Segoe UI", 9, "bold"), 
                      fg="#ff6b6b", bg="#0f0f0f")
name_label.pack(side=tk.LEFT)

tk.Label(footer_frame, text=" with love", font=("Segoe UI", 9), 
         fg="#666666", bg="#0f0f0f").pack(side=tk.LEFT)

# Start name animation
animate_name()

root.mainloop()
