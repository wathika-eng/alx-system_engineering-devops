# Install nginx via puppet

package { 'nginx':
	ensure => installed,
}
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "# Nginx configuration file
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    root /var/www/html;
    index index.html;

    location / {
        echo 'Hello World!';
    }

    location /redirect_me {
        return 301 http://$host/;
    }
}",
}

file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
