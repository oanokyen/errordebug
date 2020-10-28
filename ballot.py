# A simple ballot without replacement
# Person A randomly a picks ball
pera = (input('Pick ball:  '))
pera=int(pera)
if pera == 1:
    print('Sucessful')
elif pera == 2:
    print('Sucessful')
elif pera == 3:
    print('Sucessful')    
elif pera == 4:
    print('Sucessful')
    
# Person B randomly picks another ball    

perb = int(input('Pick ball:  ')
if perb==pera:
    print('Error: Already chosen')
else:
    print('Sucessful')
 # Person C randomly picks another ball   
perc = int(input('Pick ball:  ')
if perc==pera:
    print('Error: Already chosen')
elif perc==perb:
    print('Error: Already chosen')
else:
    print('Sucessful')

# Person D randomly picks last ball    
perd = float(input('Pick ball:  ')
if perd==pera:
    print('Error: Already chosen')
elif perd==perb:
    print('Error: Already chosen')
elif perd==perc:
    print('Error: Already Chosen')
else:
    print('Sucessful')
