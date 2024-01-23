# installs nginx package
package { 'nginx':
  ensure => present,
}

# define server config
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
  server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.htm index.html index.nginx-debian.html;

        server_name _;

        location /redirect_me {
                return 301 https://google.com/;
        }
}',
  notify  => Service['nginx'],
}

# add the index file
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# restart the service
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
}
