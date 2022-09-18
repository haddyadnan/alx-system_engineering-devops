file {'edit config':
  ensure  => present,
  path    => '/tmp/school',
  content => 'Host *
    		   SendEnv LANG LC_*
    		   HashKnownHosts yes
    		   GSSAPIAuthentication yes
    		   PasswordAuthentication no
    		   IdentityFile ~/.ssh/school

		    '
}
