# replace phpp with php in all the wp-files
exec { 'replace phpp':
  provider => shell,
  command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
