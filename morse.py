import playsound

morse_map = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
    '.':'.-.-.-',
    ',':'--..--',
    '?':'..--..',
    '\'':'.----.',
    '!':'-.-.--',
    '/':'-..-.',
    '(':'-.--.',
    ')':'-.--.-',
    '&':'-.---',
    ':':'---...',
    ';':'-.-.-.',
    '=':'-...-',
    '+':'.-.-.',
    '-':'-....-',
    '"':'.-..-.',
    '$':'...-..-',
    '@':'.--.-.',
    'END':'...-.-',
    'OVER':'-.-',
    'ROGER':'...-.',
    'STARTING':'-.-.-',
    'ERROR':'........',
    ' ':' '}

sound_map = {
    '.':'dot',
    '-':'dash',
    ' ':'space'}

def convert_input():
    userinput = input('What would you like converted to morse code?\n')
    specials=['END','OVER','ROGER','STARTING','ERROR']
    for x in specials:
        if x in userinput:
            print('Special signifiers END OVER ROGER STARTING ERROR currently still parsed normally by letter, WIP')
    morse = list(map(lambda m: morse_map[str.upper(m)], userinput))
    return(morse)

def broadcast_morse(code):
    morse_sound = []
    for word in code:
        word_sound = list(map(lambda a:sound_map[a], word))
        morse_sound.append(word_sound)
    return morse_sound

def morse_audio(sentence):
    for word in sentence:
        if word != ' ':
            print('word = ')
            print(word)
            for letter in word:
                    i = 0
                    while i < len(letter)-1:
                        print('i = '+str(i))
                        print('len(letter)-1 = '+str(len(letter)-1))
                        print('i < len(letter) - 1 (not at last d of letter)')
                        for d in letter:
                            if d == '.':
                                print('play dot')
                                playsound.playsound('dot.mp3')
                            elif d == '-':
                                print('play dash')
                                playsound.playsound('dash.mp3')
                            else:
                                print('morse audio parse error')
                            print('play silentdot')
                            playsound.playsound('silentdot.mp3')
                            i+=1
                    while i == len(letter)-1:
                        print('i = '+str(i))
                        print('len(letter)-1 = '+str(len(letter)-1))
                        print('i == len(letter) - 1 (at last d of letter)')
                        for d in letter:
                            if d == '.':
                                print('play dot')
                                playsound.playsound('dot.mp3')
                            elif d == '-':
                                print('play dash')
                                playsound.playsound('dash.mp3')
                            else:
                                print('morse audio parse error')
                            print('play silentdash\n')
                            playsound.playsound('silentdash.mp3')
                            i+=1
        elif word == ' ':
                print('hitting space between words\n')
                playsound.playsound('space.mp3')

if __name__ == "__main__":
    mcode = convert_input()
    print('\nmorse code conversion:\n')
    print(mcode)
    msound = broadcast_morse(mcode)
    print('\nmorse code audio as text:\n')
    print(msound)
    print('\nmorse code actual audio playing now:\n')
    morse_audio(mcode)
