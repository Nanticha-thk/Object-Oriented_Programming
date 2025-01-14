class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.__price = price
        self.__stock = stock
    
    def add(self, amount):  # เพิ่มจำนวน
        self.__stock += amount
        print(f"- เพิ่มสินค้า {self.name} จำนวน {amount} ชิ้นสำเร็จ ยอดคงเหลือในสต๊อก: {self.__stock} ชิ้น")
    
    def remove(self, amount):  # ลดจำนวน
        if amount <= self.__stock:
            self.__stock -= amount
        else:
            print('จำนวนสินค้าในสต็อกไม่เพียงพอ')
    
    def update(self, new_price):  # แก้ไขราคา
        if new_price > 0:
            self.__price = new_price
            print(f"- ปรับราคา {self.name} เป็น {self.__price} บาทสำเร็จ")
        else:
            print("ราคาต้องมากกว่า 0 บาท")

    def showstock(self):  # ตรวจสอบ
        print(self.__stock)
        return self.__stock
    
    def show_product_info(self):  # แสดงข้อมูลสินค้า
        print(f"Product ID: {self.id}")
        print(f"Product Name: {self.name}")
        print(f"Price: {self.__price} บาท")
        print(f"Stock: {self.__stock} units")


product1 = Product(1,"ตู้เย็น", 40000, 14)

product1.add(14)  # เพิ่ม
product1.remove(14)  # ลด
product1.update(35000)  # แก้ไข
product1.show_product_info()  # ตรวจสอบข้อมูลสินค้า


    