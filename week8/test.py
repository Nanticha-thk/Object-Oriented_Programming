class Cat :
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.fish = 0
    def cry(self):
        print(f"{self.name} ร้องเหมี้ยว")
    def eat(self,fish):
        self.fish += fish
        self.cry()
        
        return self.fish

cat1 = Cat('ศรีทอง',"ส้ม")
cat2 = Cat('ศรีเงิน',"ขาว")

print(cat1.eat(5)+5)