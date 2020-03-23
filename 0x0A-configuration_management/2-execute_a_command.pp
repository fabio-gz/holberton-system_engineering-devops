# kills a process named killmenow.
exec { 'killp':
  command  => 'pkill killmenow',
  provider => 'shell'
}
