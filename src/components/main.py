'''
Submarine Escape
You are on a sub that was hit by a depth charge. You must fix the reactor so you can surface the sub. You must fix a coolant line, then restart the reactor.

Rooms:
Reactor
Mess Hall
Bridge
'''

class Player ():
  #properties (constructor)
  def __init__(self, loc, inven=[]):
    
    # the room object where the player currently is
    self.location = loc

    # list of items the player is carrying
    self.inventory = inven

  # this method triggers any time we try to 'print' this Player() object
  def __str__(self):
    return "I am the player."
  
  


  #method
  def cmd(self):
    command = input(">>> ")
    
    # command prompt
    if command == "move":
      print("Exits:", self.location.exits)
      room = input("Which room? >>>")
      if room in self.location.exits:
        print("________________________________________________")
        

        # convert the input string to the room object name
        if room == "Storage"  :
          self.location = storage
        
        elif room == "Main Hallway" :
          self.location = mainHallway

        elif room == "Crew Cabin" :
          self.location = crewCabin

        self.location.get_desc()

      else:
        print("I'm sorry, that is not an option.")
    
    elif command == "e" :
      #if the player has an item:
      if len(self.inventory) > 0 :
        print("you have:")
        for i in self.inventory:
          print(i.name)
      else:
        print("You have nothing lol")
    

    #drops the top item from your inventory
    elif command == "drop item" :
      #check if there is at least one item
      if len(self.inventory) > 0 :
        #report the item about to be dropped
        print("You got rid of:", self.inventory[0])
        #the item is popped out of the player's inventory into variable: droppedItem
        droppedItem = self.inventory.pop(0)
        #droppedItem is appended to the inventory of the player's current location
        print(self.location.inventory, "WACKA FLACKA FLAME1")
        print(crewCabin.inventory, "WACKA FLACKA FLAME2")
        print(mainHallway.inventory, "WACKA FLACKA FLAME3")
        self.location.inventory.append(5)
        print(self.location.inventory, "WACKA FLACKA FLAME4")
        print(crewCabin.inventory, "WACKA FLACKA FLAME5")
        print(mainHallway.inventory, "WACKA FLACKA FLAME6")
        print(self)

      #if the player's inventory is empty
      else : 
        print("You have nothing to drop")

    elif command == "pickup item" :
      if len(self.location.inventory) > 0:
        print("You pick up:", self.location.inventory[0])
        self.inventory.append(self.location.inventory.pop(0))
      else : 
        print("There is nothing to pick up here")

    

    elif command == "look":
      print("________________________________________________")
      self.look()


    elif command == "help" :
      print("list of commands")
      print("\nlook, move, e, drop item, pickup item")
      


  #movement
  def move(self, destination):
    print("You moved to...", destination)

  # look at your surroundings
  def look(self):
    self.location.get_desc()

  
  

#class Object ():

#class MoveableObj(Object) :

class Room () :
  # list of exits
  def __init__(self, exits = [], desc = "NULL", name = "NONAME", inven = []):
    self.exits = exits
    self.description = desc
    self.name = name
    self.inventory = inven

  def __str__(self):
    return "Room: " + self.name

    
    
  #description of room, including items if it has any
  def get_desc(self) :
    print("You're in the", self.name)
    print(self.description)
    print("You can go to:")

    #print out the exits from this room
    for e in self.exits:
      print(e)

    if len(self.inventory) > 0:
      print("In the room you find:")
      for i in self.inventory:
        print(i.name)




class Item() :
  def __init__(self, n = "NoName", itemDesc = "none", status = "none") :
    self.name = n
    self.itemDescription = itemDesc
    self.status = status

  def __str__(self):
    return self.name
  
  def useItem() :
    print("using item") 

#items

wrench = Item("Wrench")

flashlight = Item("flashlight")


#rooms

crewCabin = Room(["Storage", "Main Hallway"], "There are 10 sets of bunk beds that are cramed into this small room, a dim light in the center shows a door to the main hallways and another door to some storage.", "Crew Cabin")

mainHallway = Room(["Engine Room", "Crew Cabin", "Bridge", "Dining Area"], "A narrow hallway connected to many rooms of the ship.", "Main Hallway")

storage = Room(["Crew Cabin"], "Many boxes and storage bins are neatly stacked on racks.", "Storage", [wrench])

# player

p1 = Player(crewCabin, [flashlight])

print("Type 'help' for a list of commands.")

while True:
  p1.cmd()

#troubleshooting code
  print("\np1 inventory:", p1.inventory)
  print("p1 location:", p1.location)
  
  print("crewCabin inventory", crewCabin.inventory, "print obj id: ", id(crewCabin))
  
  print("mainHallway inventory", mainHallway.inventory, "print obj id: ", id(mainHallway))

  print("Storage inventory", storage.inventory, "\n")
