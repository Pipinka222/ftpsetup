import os
import sys

def install_vsftpd():
    os.system('sudo apt-get update')
    os.system('sudo apt-get install -y vsftpd')
    print("Done! Restart script to AUTOCONFIGURE.")
    return True

def start_vsftpd():
    os.system('sudo systemctl restart vsftpd')
    print(".\n---\n")
    print("You can now access the FTP server locally by going to ftp://", end='')
    ip = os.popen("ip route get 1 | awk '{print $NF; exit}'").read().strip()
    print(f"{ip}:21")
    print("Your username and password are the same as your Linux username and password")
    print("\nStarted all services! :)")

def stop_vsftpd():
    os.system('sudo systemctl stop vsftpd')
    print("---\nStopped all services!")

def autoconfig_vsftpd():
    with open('vsftpd.conf', 'a') as f:
        f.write(f"chown_username={os.getenv('USER')}\n")
    os.system('sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.backup')
    os.system('sudo cp vsftpd.conf /etc/vsftpd.conf')
    os.system('sudo systemctl restart vsftpd')
    print("You can now access the FTP server locally by going to ftp://", end='')
    ip = os.popen("ip route get 1 | awk '{print $NF; exit}'").read().strip()
    print(f"{ip}:21")
    print("Your username and password are the same as your Linux username and password")
    print("Done! Restart script to STOP or START FTP server")

def main():
    print("#####################################")
    print("#          FTP Config  v1.0         #")
    print("#####################################")
    print(" ")
    print("*   Enter '1' to START FTP server")
    print("*   Enter '0' to STOP FTP server")
    print("------------------------------------")
    print("*   Enter 'a' to AUTOCONFIG vsftpd")
    print("*   Enter 'i' to INSTALL vsftpd")
    print("------------------------------------")
    option = input("*   Enter your option: ").strip()

    if option == '1':
        start_vsftpd()
    elif option == '0':
        stop_vsftpd()
    elif option == 'a':
        autoconfig_vsftpd()
    elif option == 'i':
        install_vsftpd()
    else:
        print("Invalid option. Please enter '1', '0', 'a', or 'i'.")

if __name__ == '__main__':
    main()
