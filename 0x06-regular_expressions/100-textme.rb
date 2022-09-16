#!/usr/bin/env ruby
puts ARGV[0].scan(/(from:\S*|to:\S*|flags:\S*)\b/).join(',').gsub(/(from:|to:|flags:)/,'')

# arg = ARGV[0].scan(/(from:\S*|to:\S*|flags:\S*)\b/).join(',')
# puts arg.gsub(/(from:|to:|flags:)/,'')
