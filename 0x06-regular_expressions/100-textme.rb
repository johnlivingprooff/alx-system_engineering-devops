#!/usr/bin/env ruby

# Define a regular expression to extract relevant information
puts ARGV[0].scan(/from:(?<sender>[\w\s]+)\s\[to:(?<receiver>\+\d+)\]\s\[flags:(?<flags>[-\d:]+)\]\s\[msg:(?<msg_id>\d+):(?<message>[^\]]+)\]/).join
