Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  config.vm.hostname = "billing"
  config.vm.network "forwarded_port", guest: 80, host: 8686
  config.vm.network "forwarded_port", guest: 5432, host: 5433

  config.vm.synced_folder "../billing", "/srv/billing/www/private/billing"
  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = 1024
    vb.cpus = 2
  end
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = 'ansible/site.yml'
    ansible.inventory_path = "ansible/inventory/localhost"
    ansible.verbose = '-v'
    ansible.limit = 'webservers'
  end
end
