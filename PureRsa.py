import random,time,math
from decimal import Decimal

class Rsa:
    def __init__(self,bits:int) -> None:
        self.p = None #prime number
        self.q = None #prime number
        self.n = None #modulus
        self.phi = None #Euler's totient
        self.e = 65537 #
        self.d = None
        self.bits = bits
        self._generateKey()

    def history(self)->None:
        h = 'RSA is a public-key cryptosystem that is widely used in the world today to provide a secure transmission system to millions of communications, is one of the oldest such systems in existence. The acronym RSA comes from the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman, who publicly described the algorithm in 1977. An equivalent system was developed secretly, in 1973 at GCHQ (the British signals intelligence agency), by the English mathematician Clifford Cocks. That system was declassified in 1997.'
        print(f'\n\n{h}\n')

    def _gcd(a:int, b:int)->int:
        '''
        Euclid's algorithm
        '''
        while b != 0:
            a, b = b, a % b
        return a

    def _millerRabin(self,n:int,k:int):
        d = n - 1
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, d, n)
            if x in [1, -1]:
                continue
            else:
                return False
        return True

    def _randomPrime(self,bits:int):
        while True:
            x = random.randrange(2 ** (bits - 1) + 1, 2 ** bits - 1, 2)
            if pow(2, x - 1, x) == 1:
                if self._millerRabin(x, 40):
                    return x
    
    def _egcd(self,e:int, n:int):
        if e == 0:
            return (n, 0, 1)
        else:
            g, y, x = self._egcd(n % e, e)
            return (g, x - (n // e) * y, y)

    def _modinv(self, a, m):
        g, x, y = self._egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def _generateKey(self):
        self.p = self._randomPrime(self.bits)
        while (prime := self._randomPrime(self.bits)) == self.p:
            pass
        self.q = prime
        self.n = self.p*self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.d = self._modinv(self.e, self.phi)
        if self.d < 0:
            self.d += self.phi
    def getPublicKey(self)->tuple:
        return self.n,self.e

    def encrypt(self,message:str)->tuple:
        array = []
        for char in message:
            encryptedText = pow(ord(char),self.e,self.n)
            array.append(encryptedText)
        return tuple(array)
    
    def decrypt(self,array)->str:
        decryptedText = ''
        for integer in array:
            decrypted = pow(integer,self.d,self.n)
            decryptedText += chr(decrypted)
        return decryptedText

class Hacks:
    def __init__(self,bits) -> None:
        self.p = None #prime number
        self.q = None #prime number
        self.n = None #modulus
        self.phi = None #Euler's totient
        self.e = 65537 #
        self.d = None
        
        self.bits = bits
        self.estimated = (2**bits)/1.154e+7

    def encrypt(self,message:str)->tuple:
        array = []
        for char in message:
            encryptedText = pow(ord(char),self.e,self.n)
            array.append(encryptedText)
        return tuple(array)
    
    def decrypt(self,array)->str:
        decryptedText = ''
        for integer in array:
            decrypted = pow(integer,self.d,self.n)
            decryptedText += chr(decrypted)
        return decryptedText
    
    def bruteForce(self,n:int):
        self.n = n
        self.p = self._factor()
        self.q = n//self.p
        self.phi = (self.p - 1) * (self.q - 1)
        self.d = self._modinv(self.e, self.phi)

    def _egcd(self,e:int, n:int):
        if e == 0:
            return (n, 0, 1)
        else:
            g, y, x = self._egcd(n % e, e)
            return (g, x - (n // e) * y, y)
    def _modinv(self, a, m):
        g, x, y = self._egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m        

    def _factor(self):
        for i in range(3,self.n):
            if self.n%i == 0:
                return i
import os
os.system('cls')
bits = 25
r = Rsa(bits)

encrypted = r.encrypt('h')

h = Hacks(bits)

n, e = r.getPublicKey()
s = time.perf_counter()
h.bruteForce(n)
e = time.perf_counter()-s
print(f'encrypted={encrypted}\ndecrypted={h.decrypt(encrypted)}\nestimated={h.estimated}\nseconds={e}')