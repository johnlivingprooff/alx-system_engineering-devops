# configure HTTP response Header

# Ensure the configuration file exists
file { '/etc/nginx/sites-available/default':
  ensure => file,
  # Set proper ownership and permissions
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
}

  # Configure the HTTP response header
  exec { 'Configure Response header':
    path        => '/usr/bin:/usr/sbin:/bin',
    command     => 'sed -i "/location \/ {/a \\        \\tadd_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
    refreshonly => true,
    subscribe   => File[/etc/nginx/sites-available/default],
  }
