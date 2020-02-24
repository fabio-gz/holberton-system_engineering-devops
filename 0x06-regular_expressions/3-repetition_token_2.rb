#!/usr/bin/env ruby
# match repetition 'hbtn'
puts ARGV[0].scan(/hbt{1,4}n/).join
