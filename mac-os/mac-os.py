import os
import subprocess

# List of packages to install
packages = ["fzf", "bat", "eza", "tlrc", "thefuck"]

def check_homebrew():
    """Check if Homebrew is installed, install if not."""
    try:
        subprocess.run(["brew", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Homebrew is already installed.")
    except subprocess.CalledProcessError:
        print("Homebrew is not installed. Installing Homebrew...")
        os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')

def install_packages():
    """Install the required packages using Homebrew."""
    for package in packages:
        print(f"Installing {package}...")
        os.system(f"brew install {package}")

if __name__ == "__main__":
    install_packages()
    print("Installation complete.")
