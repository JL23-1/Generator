import random
while True:
    prompt1=input('Press enter to generate or type q to quit:\n').lower()

    if prompt1 == 'q':
       exit()
    else:
        modifier = ['ranged', 'zealous', 'spicy', 'godly', 'strange', 'silly', 'angry', 'deadly', 'miniature', 'awful', 'huge', 'nice', 'sighted', 'rapid', 'fast', 'speedy', 'tiny']
        prefix1 = ['blood', 'war', 'insanity', 'zombie', 'sadness', 'idiot', 'skeleton', 'explosion', 'bacon', 'spirit', 'ghost', 'giant', 'slime', 'midas']
        prefix2 = ['paladin', 'knight', 'soldier', 'god', 'mage', 'bard', 'druid', 'king', 'bomber']
        weapon = ['shotgun', 'butter knife', 'hatchet', 'shortbow', 'longsword', 'banana', 'rifle', 'chainsaw',
                  'ukulele', 'staff', 'shield', 'spear']
        suffix = ['smite', 'doom', 'might', 'music', 'range', 'pain', 'cool', 'the sun', 'bacon', 'ouchie', 'fire', 'explosions', 'ur mom']
    currentweapon = random.choice(weapon)
    if currentweapon == 'staff':
        print(
        random.choice(modifier) + ' ' + random.choice(prefix1) + '-' + random.choice(prefix2) + ' ' + random.choice(prefix1) + ' ' + currentweapon + ' of ' + random.choice(suffix) + '\n')
    else:
        print(
        random.choice(modifier) + ' ' + random.choice(prefix1) + '-' + random.choice(prefix2) + ' ' + currentweapon + ' of ' + random.choice(suffix) + '\n')
