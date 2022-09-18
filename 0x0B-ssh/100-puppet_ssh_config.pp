include stdlib
file_line {'edit cmd':
  ensure => present,
  path   => '/tmp/school',
  match  => '^IdentityFile',
  line   => 'IdentityFile ~/.ssh/school'
}
