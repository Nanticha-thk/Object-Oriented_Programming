class Bank:
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount

id1 = Bank(1,"ice",2500)
id1.deposit(1000)
print(f"คุณ {id1.name} มีเงิน = {id1.balance}")

# Abstraction การปกปิดข้อมูล