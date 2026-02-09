class Rational:
    def __init__(self,
                 n: int,
                 d: int
                 ):
        self.n = n
        self.d = d
        return
    
    def __repr__(self) -> str:
        return f"{self.n}/{self.d}"
    
    def __add__(self, other) -> 'Rational':
        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return Rational(n,d)
    
    def __sub__(self, other) -> 'Rational':
        n = self.n * other.d - self.d * other.n
        d = self.d * other.d
        return Rational(n,d)
    
    def __mul__(self, other) -> 'Rational':
        n = self.n * other.n
        d = self.d * other.d
        return Rational(n,d)
   
    def __truediv__(x:int, y:int):
        if y==0:
            return x
        else:
            Rational.gcd(y,x%y)

    def reduce(self):
        g = Rational.gcd(self.n, self.d)
        self.n //= g
        self.d //= g
        return self
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        if b == 0:
            return a
        return Rational.gcd(b, a % b)
    
    
    
    
    