#!/usr/bin/env python
# Install redis server
# Usage: sudo python redis_ha_installer.py [master|backup]
# Author: jiasir (Taio Jia)
# E-Mail: jiasir@icloud.com
# License: The MIT License

import os
import sys
import shutil
import logging
from command import Command

run = Command()

def usage():
    print 'Usage: sudo python redis_ha_installer_el6.py <master|backup>'

def install_epel():
    run.execute_get_output('rpm', '-ivh', 'http://mirrors.yun-idc.com/epel/6/i386/epel-release-6-8.noarch.rpm')

def start_instace():
    run.execute_get_output('sudo', 'service', 'redis', 'start')
    run.execute_get_output('sudo', 'service', 'keepalived', 'start')

def install_keepalived():
    try:
        with open('/etc/sysctl.conf', 'a') as f:
            f.write('net.ipv4.ip_nonlocal_bind = 1')
    except IOError:
        print IOError.__doc__

    try:
        with open('/etc/rc.local', 'a') as f:
            f.write('ulimit -SHn 65535')
    except IOError:
        print IOError.__doc__

    run.execute_get_output('sudo', 'sysctl', '-p')
    run.execute_get_output('sudo', 'ulimit', '-SHn', '65535')
    run.execute_get_output('sudo', 'yum', '-y', 'install', 'keepalived')

def install_redis():
    try:
        with open('/etc/sysctl.conf', 'a') as f:
            f.write('vm.overcommit_memory = 1')
    except IOError:
        print IOError.__doc__
    run.execute_get_output('sudo', 'sysctl', '-p')
    run.execute_get_output('sudo', 'yum', '-y', 'install', 'redis')

def copy_keepalived_master_conf():
    shutil.copy('conf/keepalived.conf.master', '/etc/keepalived/keepalived.conf')
    print '[OK] Create keepalived config file: /etc/keepalived/keepalived.conf'

def copy_keepalived_backup_conf():
    shutil.copy('conf/keepalived.conf.backup', '/etc/keepalived/keepalived.conf')
    print '[OK] Create keepalived config file: /etc/keepalived/keepalived.conf'

def copy_redis_master_conf():
    shutil.copy('conf/redis.conf.master', '/etc/redis/redis.conf')
    print '[OK] Create redis config file: /etc/redis/redis.conf'

def copy_redis_slave_conf():
    shutil.copy('conf/redis.conf.slave', '/etc/redis/redis.conf')
    print '[OK] Create redis config file: /etc/redis/redis.conf'

def copy_fail_over_script():
    shutil.copy('tools/redis.sh', '/var/lib/redis/redis.sh')
    print '[OK] Create fail-over script: /var/lib/redis/redis.sh'

def main():
    if len(sys.argv) > 1:
        option = sys.argv[1]
    if option == "master":
        install_epel()
        install_keepalived()
        install_redis()
        copy_keepalived_master_conf()
        copy_redis_master_conf()
        copy_fail_over_script()
        start_instace()
    elif option == "backup":
        install_epel()
        install_keepalived()
        install_redis()
        copy_keepalived_backup_conf()
        copy_redis_slave_conf()
        copy_fail_over_script()
        start_instace()
    else:
        usage()
  
if __name__ == '__main__':
    if os.getuid() == 0:
        main()
    else:
        print 'You do not have permission'
        usage()
        exit()