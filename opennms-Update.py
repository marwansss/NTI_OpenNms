#!/usr/bin/env python3

import subprocess



#install python and pyenv
#-------------------------
subprocess.run(["sudo", "dnf", "update", "-y"])
subprocess.run(["sudo", "dnf", "install", "-y" , "gcc openssl-devel bzip2-devel libffi-devel zlib-devel wget make git"])
subprocess.run(["curl", "https://pyenv.run" , "|" , "bash"])
subprocess.run(["echo", "'export PYENV_ROOT=\"$HOME/.pyenv\"'", ">>" , "~/.bashrc"])
subprocess.run(["echo", "'export PATH=\"$PYENV_ROOT/bin:$PATH\"'", ">>", "~/.bashrc"])
subprocess.run(["echo", "\"$(pyenv init -)\""])
subprocess.run(["exec", "\"$SHELL\""])
subprocess.run(["sudo", "dnf", "python3-pip", "-y"])



#install and configure OpenNms
#------------------------------

package_name = ["glibc-all-langpacks","langpacks-en","makecache","https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm","postgresql14-server"]
for i in package_name:
    if i == 'makecache':
       subprocess.run(["sudo", "dnf", i])
       subprocess.run(["sudo", "dnf", "update", "-y"])
    else:
       subprocess.run(["sudo", "dnf", "install", "-y", i])


subprocess.run(["sudo" , "/usr/pgsql-14/bin/postgresql-14-setup", "initdb"])
subprocess.run(["sudo", "systemctl" ,"enable" , "--now" , "postgresql-14"])
subprocess.run(["sudo", "systemctl" ,"status" , "postgresql-14"])
subprocess.run(["sudo" ,"-i" ,"-u" ,"postgres" ,"createuser" ,"-P" ,"opennms"])
subprocess.run(["sudo", "-i", "-u", "postgres" ,"createdb" ,"-O" ,"opennms" ,"opennms"])
subprocess.run(["sudo", "-i", "-u", "postgres", "psql", "-c", "ALTER USER postgres WITH PASSWORD 'YOUR-POSTGRES-PASSWORD';"])
subprocess.run(["sudo", "sed", "-i", 's/scram-sha-256/md5/', "/var/lib/pgsql/14/data/pg_hba.conf"])
subprocess.run(["sudo", "systemctl" ,"reload" , "postgresql-14"])
subprocess.run(["sudo" , "dnf" , "-y" , "install" , "https://yum.opennms.org/repofiles/opennms-repo-stable-rhel9.noarch.rpm"])
subprocess.run(["sudo", "rpm" ,"--import" , "https://yum.opennms.org/OPENNMS-GPG-KEY"])
subprocess.run(["sudo", "dnf" ,"-y" , "install" , "opennms"])
subprocess.run(["sudo", "dnf" ,"config-manager" , "--disable" , "opennms-repo-stable-"])
subprocess.run(["sudo", "-u" ,"opennms" , "${OPENNMS_HOME}/bin/scvcli" , "set" , "postgres" , "opennms" , "password"])
subprocess.run(["sudo", "-u" ,"opennms" , "${OPENNMS_HOME}/bin/scvcli" , "set" , "postgres-admin" , "postgres" , "password"])
subprocess.run(["sudo", "sed", "-i", 's/password="${scv:postgres:password|opennms}"/password="123"/', "/opt/opennms/etc/opennms-datasources.xml"])
subprocess.run(["sudo", "sed", "-i", 's/password="${scv:postgres-admin:password|}"/password="YOUR-POSTGRES-PASSWORD"/', "/opt/opennms/etc/opennms-datasources.xml"])
subprocess.run(["sudo" , "/opt/opennms/bin/runjava", "-s"])
subprocess.run(["sudo" , "/opt/opennms/bin/install", "-dis"])
subprocess.run(["sudo" , "systemctl", "enable" , "--now" , "opennms"])
subprocess.run(["sudo" , "firewall-cmd", "--permanent" , "--add-port=8980/tcp"])
subprocess.run(["sudo" , "systemctl", "reload" , "firewalld"])
subprocess.run(["sudo" , "reboot"])



