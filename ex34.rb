def dead
  puts "You died. Good Job"
  exit(0) 
end

def gold_room 
  puts "this is a room full of gold. How much do you take?"
  choice = $stdin.gets.strip
  if choice > 50
    dead
  else
    puts "you wanted #{choice} gold coins."
    puts "Nice, you're not greedy, you win!"
    exit(0)
  end 
end

def bear_room 
  puts "There is a bear in here."
  puts "The bear has a bunch of honey."
  puts "The fat bear is in front of another door."
  puts "How are you going to move the bear?"
  bear_moved = false 

  choice = $stdin.gets.strip 
  if choice === 'Take honey'
     dead
  elsif choice === 'taunt bear' && bear_moved === false 
    puts "The bear has moved from the door."
    puts "You can go through it now."
    bear_moved = true
  elsif choice === 'taunt bear' &&  bear_moved === true 
    dead
  elsif choice === "open door" && bear_moved === true 
    gold_room
  elsif choice === "open door" && bear_moved === false
    dead
  else 
    puts "I don't understand"
    bear_room
  end
end

def cthulu_room 
  puts "Here you see the great evil Cthulu.\nHe, it, whatever stares at you and you go insane.\nDo you flee for your life or eat your head?"
  puts "flee?"
  puts "eat head"
  choice = $stdin.gets.strip 
  if choice === 'flee'
    game
  elsif choice === 'eat head'
    dead
  else 
    cthulu_room
  end 
end

def game
  puts "You are in a dark room."
  puts "There is a door to your right and left."
  puts "Which do you take?"
  choice = $stdin.gets.strip
  if choice === 'left'
    bear_room
  elsif choice === 'right'
    cthulu_room
  else
    puts 'you stumble around in the dark and fall on a knife'
  end
end

game
