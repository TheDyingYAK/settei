import os
import subprocess

# List of packages to install via apt
apt_packages = ["fzf", "bat", "eza", "tlrc", "thefuck", "neofetch", "neofetch",]

def update_system():
    """Update the package lists to ensure we get the latest versions."""
    print("Updating package lists...")
    os.system("sudo apt update -y")

def install_apt_packages():
    """Install required packages using apt."""
    for package in apt_packages:
        print(f"Installing {package}...")
        os.system(f"sudo apt install -y {package}")

def install_pip_packages():
    """Ensure pip is installed and install thefuck via pip (optional)."""
    print("Ensuring pip is installed...")
    os.system("sudo apt install -y python3-pip")
    print("Upgrading pip...")
    os.system("pip3 install --upgrade pip")
    print("Installing thefuck via pip (in case apt version is outdated)...")
    os.system("pip3 install --user thefuck")

if __name__ == "__main__":
    update_system()
    install_apt_packages()
    install_pip_packages()
    print("Installation complete.")
