# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/trusty64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false



  # If you want to connect to other ports (mysql?) you can hit this IP
  config.vm.network "private_network", ip: "192.168.33.134"
  # Otherwise, this is all that is necessary
  config.vm.network :forwarded_port, guest: 8000, host: 8034

  config.vm.provision :shell, :path => "vagrant/bootstrap.sh"

  config.ssh.forward_agent = true
  config.vm.provider :virtualbox do |vb|
    # The memory and CPUs will need to be tweaked non vPro cpus won't be able to do 2 cpus. Not sure if that includes Mac Air.
    vb.memory = 1536
    vb.cpus = 2
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

end
