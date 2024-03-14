# fixing to many open files

exec {'file_replace':
  provider => 'shell',
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace_file'],
}

exec {'replace_file':
  provider => 'shell',
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.d/90-nproc.conf',
}
