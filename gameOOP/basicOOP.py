import argparse

# phone = {
#     "brand" : "Sumsang",
#     "memory" : 256,
#     'color': "blue"
# }

# print(phone)





class Laptop:
    def __init__(self, brand, release_year, color, RAM):
        self.laptop_brand= brand
        self.laptop_release_year = release_year
        self.laptop_color = color
        self.laptop_RAM = RAM
    # Tambahkan code di bawah ini
    def information(self):
        return f"{self.laptop_color} Laptop {self.laptop_brand} release in {self.laptop_release_year} with {self.laptop_RAM} RAM"
    # Tambahkan code di bawah ini di dalam class Laptop
    def coding(self):
        print("Laptop used for coding ....")
        print("RAM usage : 2GB")
        self.laptop_RAM -= 2;
        print("Reminder RAM : " + str(self.laptop_RAM) + " GB")
    
    def office(self):
        print("Laptop used for office ....")
        print("RAM usage : 1GB")
        self.laptop_RAM -= 1;
        print("Reminder RAM : " + str(self.laptop_RAM) + " GB")

class GamingLaptop(Laptop):
    def __init__(self, brand, release_year, color, RAM, VGA):
        super().__init__(brand, release_year, color, RAM)
        self.laptop_VGA = VGA
    
    def gaming(self):
        print("Laptop used for gaming .... ")
        print("Using " + self.laptop_VGA)
        print("RAM usage : 10GB")
        self.laptop_RAM -= 10;
        print("Reminder RAM : " + str(self.laptop_RAM) + " GB")

    
#indentasi sejajar dengan class
laptop_1 = Laptop("Dell", 2021, "Grey", 8)
laptop_2 = GamingLaptop("Asus", 2022, "Black", 16, "RTX 1650")
# Tambahkan code di bawah ini
laptop_2.office()
laptop_2.gaming()
# laptop_1.gaming()
#Tambahkan code di bawah ini
# print(Laptop)
# print(laptop_1)
# print(laptop_1.laptop_brand)
# print(laptop_1.information())
# Tambahkan code di bawah ini
# laptop_1.coding()
# laptop_1.office()