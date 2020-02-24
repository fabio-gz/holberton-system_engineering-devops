#!/usr/bin/env ruby
# regex logs
puts ARGV[0].scan(/\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/).join(',')
