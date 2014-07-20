redis-ha
========

Redis with replication and failover (keepalived)

### Overview
This project help you to deploy redis With HA and automatic recovery. A basic cluster is a redis master and a redis slave, slave sync data from master. a redis master and some redis slaves if you needed.

### How to use?
* Clone this repo on all of the node:
```
git clone https://github.com/nofdev/redis-ha.git
```

* According to the need to edit the configuration file. The configuration files stored in the following location:
  * redis-ha\conf\keepalived.conf.master
    - This is the keepalived master configuration.
  * redis-ha\conf\keepalived.conf.backup
    - This is the keepalived backup configuration.
  * redis-ha\conf\redis.conf.master
    - This is the redis master configuration.
  * redis-ha\conf\redis.conf.slave
    - This is the redis slave configuration.

* To deploy the master node:
```
sudo python redis_ha_installer.py master
```

* To deploy the backup node(s):
```
sudo python redis_ha_installer.py backup
```

###Author
jiasir (Taio Jia) <jiasir@icloud.com>