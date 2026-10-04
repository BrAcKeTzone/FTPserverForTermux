import os
import sys
import subprocess

# Auto-install missing packages
try:
    from pyftpdlib.authorizers import DummyAuthorizer
    from pyftpdlib.handlers import FTPHandler
    from pyftpdlib.servers import FTPServer
except ImportError:
    print("[+] 'pyftpdlib' not found. Installing package via pip...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyftpdlib"])
    print("[+] Installation complete!\n")
    from pyftpdlib.authorizers import DummyAuthorizer
    from pyftpdlib.handlers import FTPHandler
    from pyftpdlib.servers import FTPServer


def main():
    authorizer = DummyAuthorizer()

    # Define target path: Standard Termux Home
    # Change to "/sdcard" if you want to share internal storage (requires 'termux-setup-storage')
    target_dir = os.path.expanduser("~")

    # Add user with full permissions (read/write/list/delete)
    authorizer.add_user("admin", "1234", target_dir, perm="elradfmwMT")

    handler = FTPHandler
    handler.authorizer = authorizer

    # Bind to 0.0.0.0 so local network devices can connect on port 2121
    server = FTPServer(("0.0.0.0", 2121), handler)

    print(f"FTP Server running on port 2121!")
    print(f"Serving directory: {target_dir}")
    print("Connect using your Android device's IP address (e.g., ftp://<your-ip>:2121)")
    
    server.serve_forever()

if __name__ == "__main__":
    main()
