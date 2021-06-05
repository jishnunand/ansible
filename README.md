# ansible
This repository shows ansible playbook with Vagrant and Django project deployment.

## Requirements

- Python
- Vagrant
- Virtualbox

## Setup

Clone the repository:<br/>
`https://github.com/jishnunand/ansible.git`

Change directory path to ansible:<br/>
`cd ansible`

update etc hosts for vm box to localhost communication <br/>
`sudo nano /etc/hosts`

Add below host details <br/>
`127.0.0.1 local.billing.com`

Start ansible with vagrant <br/>
`vagrant up`

This process take some time to get finish it up

Once the process completed try hitting <br/>
`http://local.billing.com:8686`
