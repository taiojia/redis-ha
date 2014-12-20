redis-ha
========

Redis with replication and failover (keepalived)

### Overview
This project help you to deploy redis With HA and automatic recovery. A basic cluster is a redis master and a redis slave, slave sync data from master. Only a redis master and a redis slave based on this arch. The project only for redis cache service not support transaction managemant. This program is for Ubuntu 14.04 or later, use `redis_ha_installer_el6.py` or `redis_ha_installer_el7.py` instead of CentOS 6/7 if you are using CentOS/RHEL.

### How to use?
* Clone this repo on all of the node:
```
git clone https://github.com/nofdev/redis-ha.git
```

* According to the need to edit the configuration file. The configuration files stored in the following location:
  * redis-ha/conf/keepalived.conf.master
    - This is the keepalived master configuration, you have to edit the VIP.
  * redis-ha/conf/keepalived.conf.backup
    - This is the keepalived backup configuration, you have to edit the VIP.
  * redis-ha/conf/redis.conf.master
    - This is the redis master configuration.
  * redis-ha/conf/redis.conf.slave
    - This is the redis slave configuration.
  * redis-ha/tools/redis.sh
    - This is the fail-over script invoked by keepalived, you have to edit the redis master ip.

* To deploy the master node:
```
sudo python redis_ha_installer.py master
```

* To deploy the backup node(s):
```
sudo python redis_ha_installer.py backup
```

### Note
* Please use the stable version.

###About the redis.sh script
* On the master node, set the `REDIS_MASTER_IP` as slave IP.
* On the slave node, set the `REDIS_MASTER_IP` as master IP.

### Using docker
* Please deploy docker daemon on your server.
* Choose your correct Docker file and rename it to `Dockerfile`.
* Using `docker build -t user/repo:tag` to build your image.

### Author
jiasir (Taio Jia) <jiasir@icloud.com>


### Change log
2014.12.20 - Add support for the docker.
2014.10.28 - Change the redis configuration settings, compatible with the version 2.8.17 and resoled the soft and hard limits.
