#!/usr/bin/env python3
import os
import sys
import time
import paramiko


def service_restart(_service):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
    # SSH connect
    ssh.connect(hostname, port, username, password)
    ssh.exec_command(f'systemctl stop {_service}')
    print(f'Service Stopping: {_service}...')
    time.sleep(4)
    print(f'Service Restart: {_service}...')
    ssh.exec_command(f'systemctl restart {_service}')
    # Fechando SSH
    time.sleep(2)
    ssh.close()


if not len(sys.argv) >= 2:
    print(f'Usage: python {sys.argv[0]} <hostname> <port> <service>')
    exit()

# Args
hostname = sys.argv[2]
port = int(sys.argv[3])
service = sys.argv[4]
username = os.getenv('LDAP_USER', 'USER')
password = os.getenv('LDAP_PASS', 'PASS')

if not username and not password:
    print("Please, make sure your username and password to SSH connect.")
    print("Tip:\nexport LDAP_USER=user1\nexport LDAP_PASS=admin123")

# Getting Started
service_restart(service)
