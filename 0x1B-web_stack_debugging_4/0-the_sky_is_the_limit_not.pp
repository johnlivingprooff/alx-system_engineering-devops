# fix high volume requests

exec { 'ulimit_replace':
  provider => 'shell',
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  unless   => 'sudo grep "ULIMIT=\"-n 4096\"" /etc/default/nginx',
  before   => Exec['ulimit_reload'],
}

exec { 'ulimit_reload':
  provider => 'shell',
  command  => 'sudo service nginx reload',
}
