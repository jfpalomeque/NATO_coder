nato_codes = {
    'A' : 'Alpha',
    'B' : 'Bravo',
    'C' : 'Charlie',
    'D' : 'Delta',
    'E' : 'Echo',
    'F' : 'Foxtrot',
    'G' : 'Golf',
    'H' : 'Hotel',
    'I' : 'India',
    'J' : 'Juliet',
    'K' : 'Kilo',
    'L' : 'Lima',
    'M' : 'Mike',
    'N' : 'November',
    'O' : 'Oscar',
    'P' : 'Papa',
    'Q' : 'Quebec',
    'R' : 'Romeo',
    'S' : 'Sierra',
    'T' : 'Tango',
    'U' : 'Uniform',
    'V' : 'Victor',
    'W' : 'Whisky',
    'X' : 'X-ray',
    'Y' : 'Yankee',
    'Z' : 'Zulu',
    ' ' : 'Space'
}

print('Welcome to  the NATO coder app. Please, enter the word or words to code in NATO phonetic alphabet. Then, press ENTER')
input = input()
print('....................................................................................................')

input = input.upper()

for ch in range(len(input)):
    key = input[ch]
    print(nato_codes[key])
    
    
