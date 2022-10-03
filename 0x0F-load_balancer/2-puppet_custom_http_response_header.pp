# Install nginx and Add http custom header with puppet
exec {'apt-update':
        command => '/usr/bin/apt-get -y update'
}

package {'install nginx':
  ensure   => 'latest',
  name     => 'nginx',

}

exec {'Add custom header':
  command => 'sudo sed -i "17i\        add_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}

exec {'restart nginx':
  command => 'sudo service nginx restart',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
