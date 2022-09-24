# This is description how to create a static ip address on rasberry pi

* first one need to check the gateway
 ```bash
  sudo route -n  
 ```
* This will give you a list and you need to check the gateway from here
* One need to open /etc/dhcpcd.conf file with an editor. In may case I am using vim. So 
``` bash
sudo vi /etc/dhcpcd.conf
```
* Very first of the file you need to write 
	* interface wlan0 [I have used wlan0, because in my case it was wlan0, can be eth0, when using ethernet for internet connection]
	* static ip_address=192.168.xx.xx[xx should be replaced by your desired ip address]
	* static routers= 192.168.xx.xx[xx should be replaced by your gateway]
	* static domain_name_servers=8.8.8.8 8.8.4.4[you DNS server name is used for google DNS, can be used any DNS name]
* Now save it 
