# Edit config file using puppet
exec {'edit config':
  command => 'sudo sed -i "s/PasswordAuthentication no/PasswordAuthentication yes" /etc/ssh/ssh_config; echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
