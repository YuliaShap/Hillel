
class Jets:
    model = None
    country = 0

    def __init__(self, name, country, quantity):
        self.name = name
        self.country = country
        self.quantity = quantity



first_item=Jets("F14","USA",87)
second_item=Jets("Mirage2000","France",35)

total = first_item.quantity+second_item.quantity
print(total)