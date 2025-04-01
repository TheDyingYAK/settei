# This will be my script to setup Arch Linux

import subprocess

# List of packages to install
packages = ["neovim", "neofetch"]

def is_installed(pkg):
    """Check if a package is already installed."""
    try:
        subprocess.run(["pacman", "-Q", pkg], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def install_packages():
    """Install required packages if they are not already installed."""
    for pkg in packages:
        if not is_installed(pkg):
            print(f"Installing {pkg}...")
            subprocess.run(["sudo", "pacman", "-S", "--noconfirm", pkg], check=True)
        else:
            print(f"{pkg} is already installed.")

if __name__ == "__main__":
    install_packages()

