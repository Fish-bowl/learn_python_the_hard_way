
def door1 
  puts "There's a giant bear here eating a cheese cake."
  puts "What do you do?"
  puts "1. Take the cake."
  puts "2. Scream at the bear."
  bear = gets.strip
  if bear == '1'
    puts 'The bear eats your face off. Good job!'
  elsif bear == '2'
    puts "The bear eats your legs off. Good job!"
  else 
    puts "Well, doing #{bear} is probably better"
  end 
end

def door2
  puts "You stare into the endless abyss at Cthulhu's retina."
  puts "1. Blueberries."
  puts "2. Yellow jacket clothespins."
  puts "3. Understanding revolvers yelling melodies."
  cthulu = gets.strip 
  if cthulu == '1' or cthulu == '2'
    puts "Your body survives powered by a mind of jello. Good job!"
  else 
    puts "The insanity rots your eyes into a pool of muck."
  end 
end

def game 
  puts "you enter a dark room with two doors. Do you go through door #1 or #2"
  door = gets.strip
  if door == '1'
    door1
  elsif door == '2'
    door2
  else 
    exit(0)
  end
end

game 
