def main 
  puts "how old are you"
  age = gets.strip
  puts 'how tall are you'
  height = gets.strip
  puts 'how much do you weigh'
  weigh = gets.strip
  puts '*' * 20
  puts "so you're #{age} old, #{height} tall, and #{weigh} heavy"
end
main
