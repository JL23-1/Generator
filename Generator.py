import random
print('Type help or ? for help or type q to quit\n')
while True:
    prompt=input('> ').lower()

    if prompt == '?':
        print(
        'Welcome to the help text\nThis is a list of commands\nweapon -- generates a random weapon name\nsandwich -- generates a random sandwich\nthreat -- generates a random threat\nhelp or ? -- prints this help text\nversion -- prints version\nq -- exits the generator'
        )
    elif prompt == 'help':
            print("Welcome to the help text\nThis is a list of commands\nweapon -- generates a random weapon name\nsandwich -- generates a random sandwich\nthreat -- generates a random threat\nq -- exits the generator")
    elif prompt == 'q':
       exit()
    elif prompt == 'weapon':
        modifier = ['ranged', 'zealous', 'spicy', 'godly', 'strange', 'silly', 'angry', 'deadly', 'miniature', 'awful', 'huge', 'nice', 'sighted', 'rapid', 'fast', 'speedy', 'tiny']
        prefix1 = ['blood', 'war', 'insanity', 'zombie', 'sadness', 'idiot', 'skeleton', 'explosion', 'bacon', 'spirit', 'ghost', 'giant', 'slime', 'midas']
        prefix2 = ['paladin', 'knight', 'soldier', 'god', 'mage', 'bard', 'druid', 'king', 'bomber']
        weapon = ['shotgun', 'butter knife', 'hatchet', 'shortbow', 'longsword', 'banana', 'rifle', 'chainsaw',
                  'ukulele', 'staff', 'shield', 'spear']
        suffix = ['smite', 'doom', 'might', 'music', 'range', 'pain', 'cool', 'the sun', 'bacon', 'ouchie', 'fire', 'explosions', 'ur mom']
        currentweapon = random.choice(weapon)
        if currentweapon == 'staff':
            print(
            '\n' + random.choice(modifier) + ' ' + random.choice(prefix1) + '-' + random.choice(prefix2) + ' ' + random.choice(prefix1) + ' ' + currentweapon + ' of ' + random.choice(suffix) + '\n')
        else:
            print(
            '\n' + random.choice(modifier) + ' ' + random.choice(prefix1) + '-' + random.choice(prefix2) + ' ' + currentweapon + ' of ' + random.choice(suffix) + '\n')
    elif prompt == 'sandwich':
        base = ['bagel', 'bread', 'bun', 'cookie', 'toast', 'egg']
        meat = ['ham', 'turkey', 'egg', 'tofu', 'hamburger', 'steak']
        topping = ['tomato', 'lettuce', 'cheese', 'egg', 'RAM', 'kale']
        sauce = ['ketchup', 'mayonnaise', 'mustard', 'egg', 'krytox 205g0', 'thermal paste', 'chocolate sauce', 'tomato sauce']
        
        bread = (random.choice(base))
        
        print('\nBread: '+bread + '\n' +'Meat: '+ random.choice(meat) + '\n' +'Topping: '+ random.choice(topping) + '\n' +'Topping: '+ random.choice(topping) + '\n' +'Sauce: '+ random.choice(sauce) + '\n' +'Bread: '+ bread + '\n')
    elif prompt == 'threat':
        part1 = ['snap', 'apply blunt force to', 'invert', 'fracture', 'boil', 'break', 'twist', 'bite', 'remove', 'delete', 'pull', 'drug', 'stab', 'explode', 'digest', 'combust', 'poach']
        part2 = ['skull', 'ribcage', 'arm', 'face', 'legs', 'ear', 'nose', 'fingers', 'hair', 'stomach', 'eyes', 'spine', 'teeth', 'heart']
        print('\nI will ' +random.choice(part1)+ ' your ' +random.choice(part2)+ '\n')
    elif prompt == 'version':
        print('version 1.0')
    elif prompt == 'armor':
        modifier = ['guarding', 'wise', 'titanic', 'pure', 'fierce', 'spiked']
        helmet = ['mask', 'helmet', 'mask', 'headgear']
        chestplate = ['scale mail', 'chestplate', 'shell', 'coat']
        leg = ['greaves', 'leggings']
        shoes = ['boots', 'slippers', 'shoes']
        material = ['iron', 'mythril', 'titanium', 'bone', 'cobalt', 'flesh', 'wooden', 'leather', 'chain', 'darkness', 'zombie', 'skeleton', 'slime']
        print(random.choice(modifier) + ' ' + random.choice(material) + ' ' + random.choice(helmet) + '\n' + random.choice(modifier) + ' ' + random.choice(material) + ' ' + random.choice(chestplate) + '\n' + random.choice(modifier) + ' ' + random.choice(material) + ' ' + random.choice(leg) + '\n' + random.choice(modifier) + ' ' + random.choice(material) + ' ' + random.choice(shoes))
    else:
        print('\nUnknown Command\nTry typing help or ?\n')
    
