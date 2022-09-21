# Puppet manifest to
# Install nginx and listening on port 80
# configure return page to return Hello World!
# 301 redirect permant

exec {'apt-update':
        command => '/usr/bin/apt-get -y update'
}

package {'install nginx':
  ensure   => 'latest',
  name     => 'nginx',

}

exec {'start nginx':
  command => 'sudo service nginx start',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}

service {'nginx':
        ensure => running,
}

exec {'configure page':
  command => 'echo "Hello World!" | sudo tee -a /usr/share/nginx/html/index.html > /dev/null',
   path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}


exec {'redirection':
   command => 'sed -i "rewrite ^/redirect_me http://intellisoftware.tech permanent;" /etc/nginx/sites-available/default',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}

exec {'restart':
  command => 'sudo service nginx restart',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
