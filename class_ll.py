
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f'Ta restauracja nazywa się {self.restaurant_name.title()} i serwuje kuchnię {self.cuisine_type}.')

    def open_restaurant(self):
        print('Ta restauracja jest otwarta od poniedziałku do piątku, od godziny 10:00 do 22:00.')

    def set_number_served(self, served_customers):
        self.number_served = served_customers
    
    def increment_number_served(self):
        self.number_served = self.number_served + 1

culto = Restaurant('culto', 'fancy')
margerita = Restaurant('margerita', 'pizza')
kfc = Restaurant('kfc','fast food')

culto.increment_number_served()
culto.increment_number_served()
culto.increment_number_served()
print(f'{culto.number_served}')

culto.set_number_served(342)
print(f'{culto.number_served}')

# culto.describe_restaurant()
# margerita.describe_restaurant()
# kfc.describe_restaurant()
