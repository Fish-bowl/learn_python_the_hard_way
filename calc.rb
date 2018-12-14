require 'colorize'

def addition
  puts "give me a number.".colorize(:red)
  num = gets.strip.to_i
  puts 'how much would you like to add?'.colorize(:red)
  mod = gets.strip.to_i
  total = num + mod 
  puts "-".colorize(:blue) * 20
  puts "#{num} + #{mod} = #{total}".colorize(:green)
  puts "-".colorize(:blue) * 20
  start
end
def subtraction 
  puts "give me a number."
  num = gets.strip.to_i
  puts 'how much would you like to subtract?'
  mod = gets.strip.to_i
  total = num - mod 
  puts "-".colorize(:blue) * 20
  puts "#{num} - #{mod} = #{total}"
  puts "-".colorize(:blue) * 20
  start
end
def multiplication
  puts "give me a number."
  num = gets.strip.to_i
  puts 'how much would you like to multiply by?'
  mod = gets.strip.to_i
  total = num * mod 
  puts "-".colorize(:blue) * 20
  puts "#{num} * #{mod} = #{total}"
  puts "-".colorize(:blue) * 20
  start
end
def division
  puts "give me a number."
  num = gets.strip.to_i
  puts 'how much would you like to divide by?'
  mod = gets.strip.to_i
  total = num / mod 
  puts "-".colorize(:blue) * 20
  puts "#{num} / #{mod} = #{total}"
  puts "-".colorize(:blue) * 20
  start
end
def start 
  puts "What kind of math would you like to do?".colorize(:red)
  puts "+ ) \n- ) \n* ) \n/ )".colorize(:red)
  puts "-".colorize(:blue) * 20
  choice = gets.strip 
  case choice 
    when "+", "add", "addition"
      addition
    when "-", 'subtract', 'subtraction', 'sub'
      subtraction
    when "*", 'multiply', 'multiplication'
      multiplication
    when "/", 'divide', 'division'
      division
    when "exit", "q", 'quit'
      puts "bye bye!"
      exit(0)
    else 
      start
  end 
end 
start
