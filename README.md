#CentOS

##### Activate eth0 and eth1


##### Remove wait when login
1. `sudo nano /etc/ssh/sshd_config`
2. change `#useDNS yes` to `useDNS no`

##### Create superuser artik
1.
2. `sudo nano /etc/sudoers`

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
4. `sudo service postgresql-9.4 start`
5. `sudo chkconfig postgresql-9.4 on`

##### Install PostgreSQL from SCL
1. `sudo yum install centos-release-SCL`
2. `yum install postgresql92`
3. `sudo service postgresql-9.4 initdb`
4. `sudo service postgresql-9.4 start`
5. `sudo chkconfig postgresql-9.4 on`


##### Create superuser artik in PostgreSQL
1. `sudo -u postgres psql`
2. `CREATE USER artik WITH password '123456';`
3. `ALTER USER artik WITH SUPERUSER;`

##### Create database in PostgreSQL
1. `sudo -u postgres psql`
2. `CREATE DATABASE mydatabase;`
