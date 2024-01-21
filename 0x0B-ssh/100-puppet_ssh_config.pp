# edit the config file for puppet nodes
include stdlib
file_line { 'IdentityFile':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  replace => true,
}

file_line {'PasswordAuth':
  line    => '    PasswordAuthentication no',
  path    => '/etc/ssh/ssh_config',
  replace => true,
}
