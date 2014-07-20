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
from noflib import noflib

run = noflib()

def usage():
    print 'Usage: sudo python redis_ha_installer.py [master|backup]'

def start_instace():
    run.execute_get_output('sudo', 'redis-server', '/etc/redis/redis.conf')
    run.execute_get_output('sudo', 'service', 'keepalived', 'start')

def install_keepalived():
    try:
        with open('/etc/sysctl.conf', 'a') as f:
            f.write('net.ipv4.ip_nonlocal_bind = 1')
    except IOError:
        print IOError.__doc__
    run.execute_get_output('sudo', 'sysctl', '-p')
    run.execute_get_output('sudo', 'apt-get', 'update')
    run.execute_get_output('sudo', 'apt-get', '-y', 'install', 'keepalived')

def install_redis():
    try:
        with open('/etc/sysctl.conf', 'a') as f:
            f.write('vm.overcommit_memory = 1')
    except IOError:
        print IOError.__doc__
    run.execute_get_output('sudo', 'sysctl', '-p')
    run.execute_get_output('sudo', 'apt-get', '-y', 'install', 'redis-server')

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
        install_keepalived()
        install_redis()
        copy_keepalived_master_conf()
        copy_redis_master_conf()
        copy_fail_over_script()
        start_instace()
    elif option == "backup":
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