# Configure HTTP response Header

# Updating OS
exec { 'update OS':
  command  => 'sudo apt-get -y update',
  path     => '/usr/bin',
  provider => shell,
}

# Installing NGINX
package { 'nginx':
  ensure => installed,
}

# Adding header and other configurations
exec { 'header X-Served-by':
  command  => 'sudo sed -i "/listen 80 default_server;/a\\       add_header X-Served-By $hostname;
  " /etc/nginx/sites-available/default',
  provider => shell,
  require  => Package['nginx'], # Ensure NGINX is installed before applying the configuration
}

# Ensure NGINX service is running and enable it at boot
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'], # Restart NGINX when configuration changes
}
