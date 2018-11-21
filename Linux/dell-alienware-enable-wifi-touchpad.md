# Enable Dell Alienware Wifi and touchpad on ubuntu 18.04

1. Enable touchpad
  
   ```sh
   sudo su
   echo 'blacklist i2c_hid' >> /etc/modprobe.d/blacklist.conf
   depmod -a
   update-initramfs -u
   ```

2. Enable Wifi
   ```sh
   sudo apt-get install git
   git clone https://git.kernel.org/pub/scm/linux/kernel/git/iwlwifi/backport-iwlwifi.git
   cd backport-iwlwifi
   make defconfig-iwlwifi-public
   sed -i 's/CPTCFG_IWLMVM_VENDOR_CMDS=y/#       CPTCFG_IWLMVM_VENDOR_CMDS is not set/'       .config
   make -j4
   sudo make install
   ```

3. Install Proprietary Nvidia GPU Drivers
   
   ```sh
   sudo add-apt-repository ppa:graphics-drivers/ppa
   sudo apt update
   sudo apt install nvidia-387
   ```

## References

[Alienware 13 touchpad not working](https://askubuntu.com/questions/647505/alienware-13-touchpad-not-working-under-any-distro-dll068b00-06cb76e9-hid-r)

[Alienware 17 R4 Ubuntu 16.04 WiFi driver](https://askubuntu.com/questions/1016903/alienware-17-r4-ubuntu-16-04-wifi-driver)

[Install Proprietary Nvidia GPU Drivers on Ubuntu 16.04 / 17.10 / 18.04](https://websiteforstudents.com/install-proprietary-nvidia-gpu-drivers-on-ubuntu-16-04-17-10-18-04/)