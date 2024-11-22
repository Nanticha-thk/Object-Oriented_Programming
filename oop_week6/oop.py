class cat:
    def __init__(self,ชื่อ,อายุ,สี,ความหิว):
        self.name = ชื่อ
        self.age = อายุ
        self.color = สี 
        self.hungry = ความหิว
    def eat(self,อาหาร):
        self.hungry+=อาหาร

cat1=cat(ชื่อ="ส้มจี๊ด",อายุ=10,สี="ส้ม",ความหิว=5)
cat2=cat("ขาวโพด",8,"ขาว",1)
print(cat1.color)
print(cat2.age)
print(cat1.hungry)