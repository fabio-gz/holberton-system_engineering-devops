# creating a custom HTTP header response
exec { 'XServed':
  command  => 'apt-get -y update; apt-get -y install nginx; sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-enabled/default; service nginx start',
  provider => shell
}
