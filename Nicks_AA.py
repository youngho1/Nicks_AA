# This is my first text adventure game. It's gross,
# despicable, and poor-humored but it's my own.
# It's free to use and play as long as you promise
# me your first born or something of equal trade. Sorry,
# only cash, no credit.

#Import the exit function to end program
from sys import exit

# Initialize an item bag
item_bag = []

def start(item_bag):
	'''Start the game'''
	print "\nWelcome to Nick's Anal Adventure"
	print "If this is what you are into then you're in luck!"
	print "Enter 'Start' to begin or 'Exit' to end"
	print "\nOnce the game starts you can use mutiple commands"
	print "to interact with your environment. Some common"
	print "commands are 'look' to observe the room/enviroment"
	print "you are currently in, 'items' to bring up your item"
	print "bag and interact with it, and 'open' which probably"
	print "will close things. I'll try to dig up more info on"
	print "that last command for you. But for now, go forth and enjoy!"
	
	items_and_actions = ['start', 'exit']
	
	answer = raw_input('> ').lower()
	
	checkED_answer = check_answer(items_and_actions, answer)	

	if 'start' in checkED_answer:
		print "\nYou awake face down in a pool of blood as usual."
		print "The room smells of elderberry and horse semen."
		print "Make your move hotshot..."
		start_room(item_bag)
	elif 'exit' in checkED_answer:
		exit(0)
	else:
		print "\nI have no idea what the fuck you are saying..."
		answer = raw_input('> ').lower()

def start_room(item_bag):
	'''The room that you start in obviously'''
	
	# All the accepted answers used to evoke responses
	items_and_actions = ['look', 'closet', 'nightstand', 'door', 'items']
	
	# Ask for an answer
	answer = raw_input('> ').lower()
	
	# Check if user used a keyword in 'answer'
	checkED_answer = check_answer(items_and_actions, answer)
	
	if 'look' in checkED_answer:
		print "You see a dusty closet in the corner that you should probably "
		print "check out, your nightstand looks suspiciously uninteresting, and"
		print "there is obviously a door....duh."
		start_room(item_bag)
	elif 'closet' in checkED_answer:
		print "\nYou arrive at the closet. It may be locked"
		print "What ya going to do about it?"
		closet(item_bag)
	elif 'nightstand' in checkED_answer:
		print "\nYou crawl to the nightstand, it has an empty water glass"
		print "on top and a single drawer, half open."
		nightstand(item_bag)
	elif 'door' in checkED_answer:
		print "\nYou approach the door cautiously because anything could"
		print "be on the other side. Mostly likely it's another room."
		door(item_bag)
	elif 'items' in checkED_answer:
		item_bag_inspect(item_bag, start_room)
	else:
		print "Wrong!"
		
def closet(item_bag):
	'''The closet is locked and for good reason'''
	# All the accepted answer to evoke responses
	items_and_actions = ['look', 'handle', 'break', 'open', 'nightstand', 'door',
	'items']
	
	# Ask for an answer
	answer = raw_input('> ').lower()
	
	# Loop over until you get a keyword
	checkED_answer = check_answer(items_and_actions, answer)
	
	if 'look' in checkED_answer:
		print "\nYou start deeply at the majestic oaken door with utter "
		print "amazement. 'How can I possible get inside?', you think"
		print "to yourself. If only R. Kelly would come out..."
		closet(item_bag)
	elif ('open' in checkED_answer) and ('pet dolphin' in item_bag):
		print "\nYou have the fucking dolphin. Go Away. God you are"
		print "terrible at puzzle games."
		closet(item_bag)
	elif ('open' in checkED_answer) and ('key' in item_bag):
		print "\nYou cracked the code of the closed closet. A stuffed pet"
		print "dolphin falls out so you do the only logical thing you can."
		print "You shove it into your item bag without any questions."
		item_bag_add(item_bag, items_and_actions[6], closet)
	elif ('open' in checkED_answer) or ('handle' in checkED_answer):
		print "\nYou shake it once, you shake it twice, and now you"
		print "are just playing with it. It's locked by the way."
		closet(item_bag)
	elif 'nightstand' in checkED_answer:
		print "\nYou crawl to the nightstand, it has an empty water glass"
		print "on top and a single drawer, half open."
		nightstand(item_bag)
	elif 'break' in checkED_answer:
		print "\nIt's 300 lb oak door. Good luck with that."
		closet(item_bag)
	elif 'door' in checkED_answer:
		print "\nYou approach the door cautiously because anything could"
		print "be on the other side. Mostly likely it's another room."
		door(item_bag)
	elif 'items' in checkED_answer:
		item_bag_inspect(item_bag, closet)
	else:
		print "Wrong!"
	
	
	
def nightstand(item_bag):
	'''The nightstand contains the key'''
	items_and_actions = ['look', 'open', 'water', 'glass', 'closet', 'door'
	, 'items']
	
	# Ask for an answer
	answer = raw_input('> ').lower()
	
	# Loop over until you get a keyword
	checkED_answer = check_answer(items_and_actions, answer)
	
	if 'look' in checkED_answer:
		print "\nIt's a nightstand, that's for sure. The drawer hangs half-open"
		print "almost begging you to slide it out. There is a pristine glass of cool"
		print "water sitting on the top as well."
		nightstand(item_bag)
	elif ('open' in checkED_answer) and ('key' in item_bag):
		print "\nThe drawer is empty because you already ransacked the key."
		print "Move along now, nothing to see here."
		nightstand(item_bag)
	elif 'open' in checkED_answer:
		print "\nThe draw slides open with such ease that it suprises you,"
		print "the entire drawer comes flying out, and a key falls on the ground."
		print "You pick it up because keys are shiny, and you are simple-minded."
		item_bag_add(item_bag, items_and_actions[6], nightstand)	
	elif 'closet' in checkED_answer:
		print "\nYou arrive at the closet. It may be locked"
		print "What ya going to do about it?"
		closet(item_bag)
	elif ('glass' in checkED_answer) or ('water' in checkED_answer):
		print "\nYou pick up the water, put it to your lips, and let a sip"
		print "gently roll down your throat. Ahhh, refrshing!"
		nightstand(item_bag)
	elif 'door' in checkED_answer:
		print "Door"
		door(item_bag)
	elif 'items' in checkED_answer:
		item_bag_inspect(item_bag, nightstand)
	else:
		print "Wrong!"

def door(item_bag):
	'''Exit out of the first room'''
	if ('key' in item_bag) and ('pet dolphin' in item_bag):
		print "\nYou made it out of my first room!"
		exit(0)
	else:
		print "\nGo back and complete the first room punk!"
		start_room(item_bag)
	
def check_answer(items_and_actions, answer):
	'''IMPORTANT : Checks the answers against acceptable answers'''
	# Turn the answer string into a list
	answer_to_list = answer.split()
	# Assign boolean True when answer list overlaps with acceptable list
	test = bool(set(answer_to_list) & set(items_and_actions))
	while not test:
		print "\nI have no idea what the fuck you are saying..."
		answer = raw_input('> ').lower()
		answer_to_list = answer.split()
		test = bool(set(answer_to_list) & set(items_and_actions))		
	# print answer - for tracing purposes
	return answer

def	look(*args):
	'''May be a useful function someday...'''
	room_items = []
	for arg in args:
		room_items.append(arg)
	return room_items
		
def item_bag_add(item_bag, item, room):
	'''This function can takes 3 arguments. The first is the item
	bag, the second is the item to be added, and the third is the room
	from which you came so you can return.'''
	item_bag.append(item)
	room(item_bag)

def item_bag_inspect(item_bag, room):
	'''This function prints out your item bag, and return to the room
	you were currently in'''
	print "Your item bag contains: "
	for item in item_bag:
		print ''
		print item
	room(item_bag)




	
start(item_bag)