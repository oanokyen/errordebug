# A simple ballot without replacement
# Person A randomly a picks ball
pera = int(input('Pick ball:  '))
if pera <= 4:
    print('Selection Sucessful')
    
# Person B randomly picks another ball    
perb = int(input('Pick ball:  ')
while perb==pera:
    print('Error: Already chosen')
    perb = int(input('Pick ball:  ')       
else:
    print('Selection Sucessful')
               
 # Person C randomly picks another ball   
perc = int(input('Pick ball:  ')
while perc==pera or perc==perb:
    print('Error: Already chosen')
    perc = int(input('Pick ball:  ')       
else:
    print('Selection Sucessful')

# Person D randomly picks last ball    
perd = int(input('Pick ball:  ')
while perd==pera or perd==perb or perd==perc:
    print('Error: Already chosen')
    perd = int(input('Pick ball:  ')
else:
    print('Selection Sucessful')
