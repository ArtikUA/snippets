#CentOS


##### Remove wait when login
1. `sudo nano /etc/ssh/sshd_config`
2. change `#useDNS yes` to `useDNS no`

##### Create superuser artik
1. `useradd artik`
2. `passwd artik`
3. `sudo nano /etc/sudoers`
4. `artik ALL=(ALL)	ALL`
5. 

##### Activate eth0 and eth1
1. `ifup eth0`
2. `ifup eth1`

##### Network2
1. VirtualBOX - Network - Host-only Networks - add
2. VirtualBOX - CentOS - settings - Network - Adapter 2 - Host-only Adapter

##### On boot eth0 and eth1
1. `cd /etc/sysconfig/network-scripts`
2. `sudo nano ifcfg-eth0`
3. `ONBOOT=yes`
4. `sudo nano ifcfg-eth1`  
  DEVICE=eth1  
	BOOTPROTO=static  
	IPADDR=192.168.56.101  
	NETMAST=255.255.255.0  

##### Install SSH
1. `yum -y install openssh-server openssh-clients`
2. `chkconfig sshd on`
3. `service sshd start`

##### Install Screen and Nano
1. `yum -y install screen nano`


##### OFF firewall
1. `sudo chkconfig iptables off`
2. `sudo service iptables stop`


##### install python3.3 with pip3.3 from SCL
1. `sudo yum install -y centos-release-SCL`
2. `sudo yum install -y python33`
3. `sudo nano .bash_profile` > `. /opt/rh/python33/enable`
3. - `yum install scl-utils`
3. - `scl enable python33 bash`
4. - `export PATH="/opt/rh/python33/root/usr/bin:$PATH"`
5. `easy_install pip`

##### Install virtualenv
`sudo /usr/local/bin/pip3.4 install virtualenv`

##### Create mainenv with name `mainenv`
`virtualenv mainenv`

##### Activate virtualenv with name `mainenv`
`source /home/artik/mainenv/bin/activate`


##### Set remote interprer in PyCharm to virtualenv `mainenv`
`/home/artik/mainenv/bin/python3.4`


##### Set autoupload files in PyCharm

##### Install uwsgi
1. `sudo yum install -y gcc`
2. `pip3.3 install uwsgi`
3. `uwsgi --http :8001 --module woohoo.wsgi`


##### Install psycopg2
1. `sudo yum install -y postgresql-devel`
2. `sudo pip3.4 install psycopg2`


##### Install PostgreSQL from SCL
1. `sudo yum install -y centos-release-SCL`
2. `sudo yum install -y postgresql92`
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
1. `sudo yum install -y epel-release`
2. `sudo yum install -y nginx`
3. `sudo chkconfig nginx on`
4. `sudo service nginx start`
