# Edit config file using puppet
exec {'edit config':
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config; echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
  path    => ['/usr/bin', '/usr/sbin']
}
