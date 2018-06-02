#!/usr/bin/env python
import string
from pwn import *


ASCII = ''.join(chr(x) for x in range(128))
SEARCH_LIST = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
#string.printable

target = 'C1D7B5D06DD88D0F894E592B0A5FDB93C4F151C04BC2540D8626E5B0017D604E33ABC51334662B8ED8CCADE9B039AE4FB5F363EA9EDD32D551C32A892B058CDE8B0B'
context(terminal=['bash'])

encryptor = process(['./encryptor.ef241ed09dfc'])

def attempt(key):
    log.info(' ')

    encryptor.recvuntil('Please enter a key (ASCII text): ')
    encryptor.sendline(key)
    log.info('Attempt: {}'.format(key))

    encryptor.recvuntil('Message to encrypt: ')
    encryptor.sendline('TheCodeSamurai subscribed for 3 months! Thank you, TheCodeSamurai!')

    encryptor.recvuntil('Your coded message (in hexadecimal) is:')
    encryptor.recvline() # dummy read for previous line
    coded_hex = encryptor.recvline()
    log.info('Hex: {}'.format(coded_hex))

    if coded_hex.startswith(target[:(2 * len(key))]):
        log.info('Predict2: ' + key)
        return True

    return False

    


if __name__ == '__main__':
    prefix = ''
    for x in range(30):
        for i in SEARCH_LIST:
            if attempt(prefix + i) == True:
                prefix += i
                break

    encryptor.kill()



'''
def get_strcmp_result(payload):
    genesis = process(['gdb', './gen'])
    log.info(' ')

    #log.info('Set Breakpoint 1')
    genesis.recvuntil('(gdb)')
    genesis.sendline('break *0x80496bd')

    #log.info('Set Breakpoint 2')
    genesis.recvuntil('(gdb)')
    genesis.sendline('break *0x08049688')

    genesis.sendline('run')
    log.info('Running: ' + payload)

    genesis.recvuntil('hit Breakpoint 1, 0x080496bd')
    #log.info('At Breakpoint 1')
    genesis.recvuntil('(gdb)')
    genesis.sendline('call bonus()')

    genesis.recvuntil("LEVEL 99")
    #log.info('At LEVEL 99')
    genesis.sendline(payload)

    genesis.recvuntil("hit Breakpoint 2, 0x08049688")
    #log.info('At Breakpoint 2')
    genesis.recvuntil('(gdb)')
    genesis.sendline('p $eax')

    eax_info = genesis.recvline()
    strcmp_result = eax_info.split(' = ')[1]
    log.info('Result: ' + strcmp_result)

    genesis.kill()

    return int(strcmp_result) > 0
'''

#SEARCH_LIST = ASCII

'''
def find_letter(prefix=''):
    prev_result = None
    prev_letter = '0'
    for letter in SEARCH_LIST: 
        curr_result = get_strcmp_result(prefix + letter)
        if (prev_result != curr_result) and (prev_result is not None):
            print 'Found', prev_letter, letter
            return (prev_letter, letter)
            quit()
        prev_result = curr_result
        prev_letter = letter
    return None

def try_pair(prefix, a, b):
    result = find_letter(prefix + a)
    if result is not None:
        return (result, a)

    result = find_letter(prefix + b)
    return (result, b)

'''


        


"""

# Start a process
genesis = gdb.debug("./gen",  '''
# inside main()
break *0x80496bd

# after bonus() user-input
break *0x08049688
run
call bonus()
''')
"""



# process('./gen')

# Attach the debugger
#gdb.attach(genesis,)


#run
#call bonus()

#set logging on

# Interact with the process
#genesis.sendline('f')

#gdb.send('p $eax')

'''
f
f
set logging on
p $eax
'''