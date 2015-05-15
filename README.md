#CentOS


##### Remove wait when login
1. `sudo nano /etc/ssh/sshd_config`
2. change `#useDNS yes` to `useDNS no`

##### Create superuser artik
1. `useradd -ou 0 -g 0 artik`
2. `passwd artik`

##### Activate eth0 and eth1
1. `ifup eth0`
2. `ifup eth1`

##### Network2
1. VirtualBOX - settings - Network - Adapter 2 - Host-only Adapter
2. 

##### On boot eth0 and eth1
1. `cd /etc/sysconfig/network-scripts`
2. `sudo nano ifcfg-eth0`
3. `ONBOOT=yes`
4. `sudo nano ifcfg-eth1`
5. `DEVICE=eth1`

`BOOTPROTO=static`

`IPADDR=192.168.56.101`

`NETMAST=255.255.255.0`


##### Install python3.4 with pip3.4 from sources
1. `sudo yum install gcc openssl-devel pcre-devel zlib-devel`
2. `wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz`
3. `tar xzf Python-3.4.3.tgz` 
4. `cd Python-3.4.3`
5. `./configure`
6. `make`
7. `sudo make install`

##### install python3.3 with pip3.3 from SCL
1. `sudo yum install centos-release-SCL`
2. `sudo yum install python33`

##### Install virtualenv
`sudo /usr/local/bin/pip3.4 install virtualenv`

##### Create mainenv with name `mainenv`
`virtualenv mainenv`

##### Activate virtualenv with name `mainenv`
`source /home/artik/mainenv/bin/activate`


##### Set remote interprer in PyCharm to virtualenv `mainenv`
`/home/artik/mainenv/bin/python3.4`


##### Set autoupload files in PyCharm


##### Install psycopg2
1. `sudo yum install postgresql-devel`
2. `sudo pip3.4 install psycopg2`


##### Install PostgreSQL
1. `yum localinstall http://yum.postgresql.org/9.4/redhat/rhel-6-x86_64/pgdg-centos94-9.4-1.noarch.rpm`
2. `yum install postgresql94-server`
3. `sudo service postgresql-9.4 initdb`
4. `sudo chkconfig postgresql-9.4 on`
5. `sudo service postgresql-9.4 start`

##### Install PostgreSQL from SCL
1. `sudo yum install centos-release-SCL`
2. `yum install postgresql92`
3. `sudo service postgresql-9.4 initdb`
4. `sudo chkconfig postgresql-9.4 on`
5. `sudo service postgresql-9.4 start`


##### Create superuser artik in PostgreSQL
1. `sudo -u postgres psql`
2. `CREATE USER artik WITH password '123456';`
3. `ALTER USER artik WITH SUPERUSER;`

##### Create database in PostgreSQL
1. `sudo -u postgres psql`
2. `CREATE DATABASE mydatabase;`

##### Install nginx
1. `sudo yum install epel-release`
2. `sudo yum install nginx`
3. `sudo chkconfig nginx on`
4. `sudo service nginx start`
