# Termux Lightweight FTP Server

A standalone Python-based FTP server designed to run natively on Android via Termux. It automatically detects and installs missing dependencies (`pyftpdlib`) on startup and shares your specified directory across your local network.

## Features
- **Zero-Setup Dependencies:** Auto-installs `pyftpdlib` using `pip` if missing.
- **Native Termux Support:** Configured out-of-the-box to serve Termux home directory or `/sdcard`.
- **Local Network Ready:** Binds to `0.0.0.0:2121` for instant connections from file managers like CX File Explorer or PC clients.

## Auth (FTP not FTPS)
- User: `Admin`
- Pass: `1234`
