import paramiko

servers = [
    {"name": "linux1", "host": "3.110.83.185"},
    {"name": "linux2", "host": "3.110.160.253"}
]

username = "ubuntu"
key_file = "APAC.pem"

for server in servers:
    print("\n==============================")
    print(f"Checking Server: {server['name']}")
    print("==============================")

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            hostname=server["host"],
            username=username,
            key_filename=key_file,
            timeout=10
        )

        # Uptime check
        stdin, stdout, stderr = ssh.exec_command("uptime")
        print("\n>>> UPTIME")
        print(stdout.read().decode())

        # Ping check
        stdin, stdout, stderr = ssh.exec_command("ping -c 2 8.8.8.8")
        print("\n>>> INTERNET PING TEST")
        print(stdout.read().decode())

        # Memory check
        stdin, stdout, stderr = ssh.exec_command("free -m")
        print("\n>>> MEMORY USAGE")
        print(stdout.read().decode())

        # Disk check
        stdin, stdout, stderr = ssh.exec_command("df -h")
        print("\n>>> DISK USAGE")
        print(stdout.read().decode())

        # Network Interface
        stdin, stdout, stderr = ssh.exec_command("ip a")
        print("\n>>> NETWORK INTERFACE")
        print(stdout.read().decode())

        # CPU Load
        stdin, stdout, stderr = ssh.exec_command("cat /proc/loadavg")
        print("\n>>> CPU LOADAVG")
        print(stdout.read().decode())

        # Disk Inodes
        stdin, stdout, stderr = ssh.exec_command("df -i")
        print("\n>>> DISK INODES")
        print(stdout.read().decode())

        # Default Gateway
        stdin, stdout, stderr = ssh.exec_command("ip route")
        print("\n>>> DEFAULT GATEWAY")
        print(stdout.read().decode())

        # SSH Service Status
        stdin, stdout, stderr = ssh.exec_command("systemctl status ssh")
        print("\n>>> SSH Status")
        print(stdout.read().decode())

        # Kernel OS & Info
        stdin, stdout, stderr = ssh.exec_command("cat /etc/os-release")
        print("\n>>> Kernel OS")
        print(stdout.read().decode())

        ssh.close()

    except Exception as e:
        print(f"Connection Failed: {e}")

