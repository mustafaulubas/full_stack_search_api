# -*- mode: ruby -*-
# vi: set ft=ruby :

unless Vagrant.has_plugin?("vagrant-docker-compose")
  system("vagrant plugin install vagrant-docker-compose")
  puts "Dependencies installed, please try the command again."
  exit
end

Vagrant.configure(2) do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  # If errors occur, try running "vagrant provision" manually
  # after "vagrant up"
  config.vm.provision :docker
  # To use docker_compose as a provisioning tool, install
  # vagrant-docker-compose plugin first. It should also solve the
  # "The '' provisioner could not be found." error:
  # $ vagrant plugin install vagrant-docker-compose
  config.vm.provision :docker_compose, rebuild: true, run: "always", yml: "/vagrant/docker-compose.yml", command_options: { up: ""}
end 


