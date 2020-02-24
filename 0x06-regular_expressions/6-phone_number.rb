#!/usr/bin/env ruby
# match phone number
puts ARGV[0].scan(/^\d{10}$/).join
