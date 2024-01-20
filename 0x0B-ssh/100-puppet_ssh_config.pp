# Config w/Puppet

file { '/home/wathi/.ssh/config':
  ensure  => present,
  mode    => '0600',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "35.153.93.152
    HostName 35.153.93.152
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}

