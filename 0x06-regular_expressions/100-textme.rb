#!/usr/bin/env ruby

# Define a regular expression to extract relevant information
puts ARGV[0].scan(/(?<=from:|to:|flags:)(\+?\w+|[-?[0-1]:?]+)/).join(',')
