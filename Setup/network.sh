#!/bin/bash
sed -i 's/192.168.11.1/127.0.0.1/' /home/pi/.bashrc
sed -i 's/192.168.11.1/127.0.0.1/' /home/pi/catkin_ws/src/clever/clever/launch/mavros.launch
sed -i 's/192.168.11.1/127.0.0.1/' /home/pi/catkin_ws/src/clever/deploy/roscore.env

export ROS_IP=127.0.0.1

sudo systemctl restart roscore
sudo systemctl restart clever

read -p 'SSID: ' ssid
read -sp 'Password: ' pass

sudo systemctl stop dnsmasq
sudo systemctl disable dnsmasq

sudo sed -i 's/interface wlan0//' /etc/dhcpcd.conf
sudo sed -i 's/static ip_address=192.168.11.1\/24//' /etc/dhcpcd.conf

cat << EOF | sudo tee /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=GB

network={
    ssid="$ssid"
    psk="$pass"
}

EOF

sudo systemctl restart dhcpcd
