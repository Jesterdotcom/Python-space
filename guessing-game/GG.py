import random
#the database
mobs = [
    ["Zombie", "Undead", "Overworld", "Experience", "Walking"],
    ["Skeleton", "Undead", "Overworld", "Item", "Walking"],
    ["Creeper", "Beast", "Overworld", "Rare", "Walking"],
    ["Enderman", "Humanoid", "End", "Experience", "Teleporting"],
    ["Ghast", "Elemental", "Nether", "Item", "Flying"],
    ["Blaze", "Elemental", "Nether", "Special", "Flying"],
    ["Slime", "Beast", "Overworld", "Item", "Burrowing"],
    ["Drowned", "Undead", "Water", "Item", "Swimming"],
    ["Phantom", "Humanoid", "Overworld", "Experience", "Flying"],
    ["Magma Cube", "Elemental", "Nether", "Rare", "Burrowing"],
    ["Wither Skeleton", "Undead", "Nether", "Rare", "Walking"],
    ["Witch", "Humanoid", "Overworld", "Special", "Walking"],
    ["Guardian", "Beast", "Water", "Rare", "Swimming"],
    ["Elder Guardian", "Beast", "Water", "Special", "Swimming"],
    ["Shulker", "Humanoid", "End", "Item", "Flying"],
    ["Silverfish", "Beast", "Cave", "Experience", "Burrowing"],
    ["Vex", "Humanoid", "Overworld", "Rare", "Flying"],
    ["Ravager", "Beast", "Overworld", "Rare", "Walking"],
    ["Stray", "Undead", "Overworld", "Item", "Walking"],
    ["Piglin", "Humanoid", "Nether", "Item", "Walking"],
    ["Piglin Brute", "Humanoid", "Nether", "Rare", "Walking"],
    ["Hoglin", "Beast", "Nether", "Item", "Walking"],
    ["Warden", "Undead", "Cave", "Special", "Walking"],
    ["Evoker", "Humanoid", "Overworld", "Special", "Walking"],
    ["Vindicator", "Humanoid", "Overworld", "Item", "Walking"],
    ["Illusioner", "Humanoid", "Overworld", "None", "Teleporting"],
    ["Cave Spider", "Beast", "Cave", "Item", "Walking"],
    ["Spider", "Beast", "Overworld", "Experience", "Walking"],
    ["Husk", "Undead", "Overworld", "Item", "Walking"],
    ["Strider", "Beast", "Nether", "Item", "Walking"],
    ["Dune Spider", "Beast", "Desert", "Rare", "Walking"]
]
ff = [
    ["Alok", "Street", "Active", "Healing", "SMG"],
    ["K", "Mystic", "Active", "Healing", "AR"],
    ["Chrono", "Futuristic", "Active", "Defense", "Sniper"],
    ["Skyler", "Corporate", "Active", "Damage", "Shotgun"],
    ["Wukong", "Mythic", "Active", "Stealth", "SMG"],
    ["A124", "Futuristic", "Active", "Healing", "AR"],
    ["Dasha", "Rebel", "Passive", "Control", "AR"],
    ["Jota", "Street", "Passive", "Healing", "SMG"],
    ["Hayato", "Samurai", "Passive", "Damage", "AR"],
    ["Kelly", "Athlete", "Passive", "Speed", "Shotgun"],
    ["Moco", "Hacker", "Passive", "Detection", "SMG"],
    ["Laura", "Agent", "Passive", "Accuracy", "Sniper"],
    ["Rafael", "Assassin", "Passive", "Stealth", "Sniper"],
    ["Clu", "Detective", "Active", "Detection", "AR"],
    ["Kapella", "Singer", "Passive", "Healing", "SMG"],
    ["Maxim", "Streamer", "Passive", "Speed", "Shotgun"],
    ["Steffie", "Artist", "Active", "Defense", "AR"],
    ["Notora", "Biker", "Passive", "Healing", "SMG"],
    ["Luqueta", "Athlete", "Passive", "Defense", "AR"],
    ["Dimitri", "Medic", "Active", "Healing", "SMG"],
    ["Thiva", "Performer", "Passive", "Support", "Shotgun"],
    ["Homer", "Tech", "Active", "Damage", "SMG"],
    ["Kenta", "Bodyguard", "Active", "Defense", "Shotgun"],
    ["D-Bee", "Street", "Passive", "Speed", "SMG"],
    ["Iris", "Spy", "Active", "Detection", "AR"],
    ["Leon", "Athlete", "Passive", "Healing", "Shotgun"],
    ["Tatsuya", "Rebel", "Active", "Speed", "SMG"],
    ["Sonia", "Futuristic", "Active", "Defense", "AR"],
    ["Otho", "Psychic", "Passive", "Detection", "Sniper"],
    ["Clash", "Military", "Passive", "Accuracy", "AR"]
]
def start():
      global d,sent
      print("Welcome Users")
      print("1. Guess the mob"
      "\n2. Guess the character")
      c = int(input("Enter your choice :"))
      if c == 1:
            d = mobs
            sent = "Guess the MC mob :"
      elif c == 2:
            d = ff
            sent = "Guess the FF character :"
      else:
            print("Enter correct option")
            start()

def guessgame():
                  pick = d[random.randint(0,len(d) - 1)]   #guessed mob
                  while True:
                              w = "y"
                              guess = input(sent)
                              t = guess.lower()
                              print()
                              if t == pick[0].lower():
                                          print("Yay! You have guessed right")
                                          print(pick[0],"was the guess")
                                          break
                              elif guess == "kill":   #only for debugging
                                      break
                              elif guess == "esc":
                                      print(pick[0])
                              elif guess == "list":
                                      print(d)
                              for n in range(0,len(d)):
                                                if t == d[n][0].lower():  #check if guess is in database
                                                      w = "x"
                                                      gueset=d[n]
                                                      for i in range(1,5):       #Quality matching 
                                                            if pick[i]==gueset[i]:  
                                                                  print(gueset[i], "MATCHED")
                                                            elif pick[i]!=gueset[i]:
                                                                  print(gueset[i], "NOT MATCHED") 
                              if w == "y":
                                    print("INVALID CHARACTER")
                              print("Try Again")


start()
guessgame()

                                          

                                    
                                        

                              

