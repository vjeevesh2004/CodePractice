class Number:
    def __init__(self, num):
        self.num = num
    
# here __add__, __mul__ are the dender methods to overload operators

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num
     # will print 300 if we write return 300

    def __mul__(self, num2):
        print("Lets Multiply")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2 
mul = n1 * n2
print(sum)
print(mul)