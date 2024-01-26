import os
os.system('cls')
width = os.get_terminal_size()[0]+1
with open('t.txt','r',encoding="utf-8") as f:
    l = ''
    for line in f.readlines():
        try:
            char = chr(int(f'0x{line[0:5]}',16))
            if len(l) == width:
                print(l,end='')
                l = ''
            else:
                l += char
        except ValueError:
            pass
