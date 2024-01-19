# kills a process named 'killmenow.'
exec { 'killmenow process':
    command => '/usr/bin/pkill -TERM killmenow',
}
