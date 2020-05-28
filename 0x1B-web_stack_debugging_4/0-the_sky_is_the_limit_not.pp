#fail requests
exec { 'nginx fix':
    command  => 'sudo sed -i "s/15/2001/g" /etc/default/nginx; sudo service nginx restart',
    provider => 'shell'
}
