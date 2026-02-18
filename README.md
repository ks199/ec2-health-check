# ec2-health-check
EC2 Linux Health Check Automation using Python (Paramiko)
This project automates the health verification of Linux EC2 instances in
Amazon Web Services
using Python and SSH.

# EC2 Health Check - Architecture Overview

## 1️⃣ Overview
This document explains the architecture of the EC2 Health Check automation project.  
The goal is to automate server health verification for Linux EC2 instances using Python.

---

## 2️⃣ Components

| Component        | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| **Python Script**| Uses Paramiko to SSH into EC2 instances and run Linux commands.            |
| **EC2 Instances**| Ubuntu 24.04 LTS servers; can be public or private subnet.                |
| **SSH Key**      | Private key (.pem) used for authentication. Passwords are not recommended. |
| **Paramiko**     | Python library for SSH connectivity and command execution.                 |

---

## 3️⃣ Network Architecture

[Local Machine / PowerShell / Linux VM]
|
| SSH (TCP 22)
|
[AWS EC2 Instances]
| Ubuntu OS
| Private IP (preferred)
| Public IP (only for testing)


**Notes:**

- For production, EC2 instances should ideally be in a private subnet.
- Use a bastion host for SSH access to private instances.
- Security: Limit SSH access using Security Groups (only trusted IPs).

---

## 4️⃣ Security Considerations

- Do **not** expose private keys publicly.  
- Use key-based SSH authentication only.  
- Monitor SSH logs: `/var/log/auth.log`.  
- Avoid password authentication on EC2.  
- Consider logging all script output to a secure location.

---

## 5️⃣ Future Improvements

- Automate across multiple regions and accounts.  
- Export results to CSV or JSON for reporting.  
- Add email/SMS notifications for failed checks.  
- Integrate with AWS Lambda for serverless execution.  

# Linux Commands Used in EC2 Health Check Script

## 1️⃣ `uptime`
- Shows how long the server has been running.
- Example Output: `05:48:12 up 1:17, 2 users, load average: 0.00, 0.00, 0.00`
- **Purpose:** Check if the server is stable and not frequently rebooting.

---

## 2️⃣ `ping -c 2 8.8.8.8`
- Sends 2 ICMP packets to 8.8.8.8 (Google DNS).
- **Purpose:** Verify internet connectivity from EC2.

---

## 3️⃣ `free -m`
- Displays memory usage in MB.
- **Purpose:** Ensure enough free memory for workloads.

---

## 4️⃣ `df -h`
- Shows disk usage in human-readable format (GB/MB).
- **Purpose:** Verify sufficient storage space.

---

## 5️⃣ `df -i`
- Shows inode usage for filesystems.
- **Purpose:** Ensure filesystems are not running out of inodes.

---

## 6️⃣ `ip a`
- Lists network interfaces and IP addresses.
- **Purpose:** Confirm proper network configuration.

---

## 7️⃣ `ip route`
- Displays the routing table.
- **Purpose:** Check default gateway and network paths.

---

## 8️⃣ `systemctl status ssh`
- Checks the status of the SSH service.
- **Purpose:** Ensure SSH is running for connectivity.

---

## 9️⃣ `cat /etc/os-release`
- Displays OS information (name, version, codename).
- **Purpose:** Verify kernel and distribution.

---

## 🔟 Optional: `top -b -n1 | head -5`
- Shows top CPU-consuming processes.
- **Purpose:** Monitor CPU usage and system load in real-time.

How to run
pip install paramiko
python ec2_health_check_v2.py
