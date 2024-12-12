import random

types = [1,2,3,4]
times = [10,11,12,13,14,15,16]

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
Letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','_','+','-','=','`','~','?','<','>']


go = 'yes'
while go == 'yes':
    code = []
    run = input('Enter to generate passcode')
    if run == '':
        time = random.choice(times)
        for i in range(time):
            character_type = random.choice(types)
            if character_type == 1:
                character = random.choice(letters)
                code.append(str(character))
            if character_type == 2:
                character = random.choice(numbers)
                code.append(str(character))
            if character_type == 3:
                character = random.choice(symbols)
                code.append(str(character))
            if character_type == 4:
                character = (random.choice(Letters))
                code.append(str(character))
        
        print('')
        print('Your code:')
        print(''.join(code))
        print('----------------------')

    if run.lower() == 'exit' or run.lower() == 'quit':
        quit()
    
