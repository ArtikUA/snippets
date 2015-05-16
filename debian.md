##### Enable eth1
1. `sudo nano /etc/network/interfaces`
2. `auto eth1`

`iface eth1 inet static` 

`address 192.168.235.101` 

`netmask 255.255.255.0` 

3. `sudo service networking restart`
