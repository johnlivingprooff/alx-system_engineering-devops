# kills a process named 'killmenow.'
exec { 'killmenow process':
  command     => 'pkill killmenow',
  refreshonly => true,
}

# notifies exec resource to ensure it runs
notify { 'killmenow':
  require => Exec[],
}
