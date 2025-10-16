# 🌹 Rose Server

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)]()
[![Python](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![GitHub release](https://img.shields.io/github/v/release/IamNoobLikeYou/rose_server)]()

<p align="center">
  <img src="Screenshot%20of%20the%20application.png" alt="Rose Server Screenshot" width="600"/>
</p>

<p align="center">
  <strong>A beautiful, modern HTTP server launcher with GUI</strong>
</p>

<p align="center">
  Launch local web servers instantly • No command line needed • Works everywhere
</p>

---

## ✨ Features

- 🎨 **Beautiful Modern UI** - Sleek dark theme with rounded corners and smooth animations
- 📁 **Any Directory** - Serve files from any folder on your system with a built-in file picker
- 🔧 **Custom Ports** - Choose any port from 1 to 65535
- 🌐 **Auto Browser Launch** - Automatically opens your default browser when server starts
- ⚡ **Lightning Fast** - Server launches in under 2 seconds
- 💻 **Cross-Platform** - Works seamlessly on Windows, Linux, and macOS
- 🪶 **Lightweight** - Minimal resource usage, runs silently in background
- 🎯 **Beginner Friendly** - No technical knowledge required - just click and serve!

---

## 📸 Screenshots

<p align="center">
  <img src="Screenshot%20on%20windows.png" alt="Windows" width="400"/>
  <img src="Screenshot%20on%20linux.png" alt="Linux" width="400"/>
</p>

---

## 🚀 Quick Start

### 📥 Download & Install

#### 🪟 **Windows**

**Option 1: Standalone Executable (Recommended)**
1. Download `RoseServer.exe` from [Releases](https://github.com/IamNoobLikeYou/rose_server/releases)
2. Double-click to run - no installation needed!
3. That's it! 🎉

**Option 2: Run from Source**
```bash
git clone https://github.com/IamNoobLikeYou/rose_server.git
cd rose_server
python rose_server.py
```

#### 🐧 **Linux**

```bash
# Clone the repository
git clone https://github.com/IamNoobLikeYou/rose_server.git
cd rose_server

# Install dependencies (if needed)
sudo apt install python3 python3-tk  # Debian/Ubuntu
# or
sudo dnf install python3-tkinter      # Fedora
# or
sudo pacman -S tk                     # Arch

# Run Rose Server
python3 rose_server.py
```

#### 🍎 **macOS**

```bash
# Clone the repository
git clone https://github.com/IamNoobLikeYou/rose_server.git
cd rose_server

# Run (Python 3 is pre-installed on macOS)
python3 rose_server.py
```

---

## 💡 Usage

### Basic Usage

1. **Set Port** (optional) - Enter your desired port number (default: 8000)
2. **Choose Directory** - Click the 📁 button or paste a directory path
3. **Start Server** - Click the 🚀 **Start Server** button
4. **Access Your Files** - Your browser will open automatically to `http://localhost:PORT`
5. **Stop Server** - Click the ✕ **Stop Server** button when done

### Use Cases

- **Web Development** - Test static websites and single-page applications locally
- **File Sharing** - Share files with devices on your local network
- **Quick Demos** - Show your work without deploying to the cloud
- **Learning** - Perfect for students learning web development
- **IoT Projects** - Serve files to Raspberry Pi and other embedded devices

---

## 🛠️ Building from Source

### Create Windows Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build the executable
pyinstaller --onefile --windowed --icon=icon.ico --name="RoseServer" rose_server.py

# Find your executable in the 'dist' folder
```

### Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python)
- No additional dependencies!

---

## 📖 Documentation

### Directory Structure

```
rose_server/
├── source_code/
│   └── rose_server.py          # Main application
├── For_windows/
│   ├── RoseServer.exe          # Windows executable
│   └── icon.ico                # Windows icon
├── For_Linux/
│   └── Instructions.md         # Linux setup guide
├── For_MacOS/
│   └── Instructions.md         # macOS setup guide
├── troubleshooting_tips/
│   └── Common_Issues.md        # Troubleshooting guide
├── LICENSE                     # MIT License
└── README.md                   # This file
```

### Configuration

Rose Server works out of the box with sensible defaults:
- **Default Port**: 8000
- **Default Directory**: Current working directory
- **Browser**: System default browser

You can customize these at runtime through the GUI.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🔨 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. ✍️ Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🎉 Open a Pull Request

### Areas for Contribution

- [ ] Additional themes (light mode, custom colors)
- [ ] HTTPS support
- [ ] Custom server configurations
- [ ] Multi-language support
- [ ] macOS testing and optimization
- [ ] Documentation improvements

---

## 🐛 Bug Reports & Feature Requests

Found a bug or have an idea? [Open an issue](https://github.com/IamNoobLikeYou/rose_server/issues)!

Please include:
- Your operating system
- Python version (if running from source)
- Steps to reproduce the issue
- Screenshots (if applicable)

---

## 📊 Platform Support

| Platform | Status | Tested Version | Notes |
|----------|--------|----------------|-------|
| Windows 10/11 | ✅ Fully Supported | Windows 11 | Standalone .exe available |
| Ubuntu/Debian | ✅ Fully Supported | Ubuntu 22.04 | Requires python3-tk |
| Fedora | ✅ Fully Supported | Fedora 38 | Requires python3-tkinter |
| Arch Linux | ✅ Fully Supported | Latest | Requires tk package |
| Kali Linux | ✅ Fully Supported | 2024.1 | Tested and working |
| macOS | ⚠️ Should Work | Not tested | Community feedback welcome |

---

## 🎯 Roadmap

- [x] Core functionality (serve files from any directory)
- [x] Cross-platform support
- [x] Modern UI with animations
- [x] Windows executable
- [ ] HTTPS/SSL support
- [ ] Custom error pages
- [ ] Server logs viewer
- [ ] Saved configurations/presets
- [ ] Tray icon for background operation
- [ ] QR code generation for mobile access

---

## 💖 Acknowledgments

- Built with [Python](https://www.python.org/) and [Tkinter](https://docs.python.org/3/library/tkinter.html)
- Icons and design inspired by modern web aesthetics
- Thanks to all contributors and users for feedback!

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**TL;DR**: Free to use, modify, and distribute. Just keep the copyright notice.

---

## 💬 Connect

- **GitHub**: [@IamNoobLikeYou](https://github.com/IamNoobLikeYou)
- **Issues**: [Report bugs or request features](https://github.com/IamNoobLikeYou/rose_server/issues)
- **Discussions**: [Join the community](https://github.com/IamNoobLikeYou/rose_server/discussions)

---

## ⭐ Show Your Support

If Rose Server helped you, please consider:
- ⭐ Giving it a star on GitHub
- 🐛 Reporting bugs to help improve it
- 💡 Suggesting new features
- 📢 Sharing it with others who might find it useful

---

<p align="center">
  <strong>Created By <a href="https://github.com/IamNoobLikeYou">r0se4U</a> with love 💖</strong>
</p>

<p align="center">
  🌹 <strong>Happy Serving!</strong> 🌹
</p>

<p align="center">
  <sub>Made with Python, Tkinter, and lots of ☕</sub>
</p>
