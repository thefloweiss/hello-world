#Homework 2 - Create the E-Shop Experience
#Let the User choose an item from a specific list. Return the Price, Show categories & total price.

welcome = input("Hello! Welcome to your favorite E-shop, it's finally time to spend your money.")

menu = {
    'Laptops':['Lenovo':7499, 'HP':10949, 'Asus':8500],
    'Mobile Phones':['Samsung Note 10+':15000, 'Apple Iphone 10':85000, 'Motorola V3':2333],
    'Watches':['Samsung Watch':7499, 'Apple Watch':8900]
}
print('Today we have available discounts on: ')
for option in menu: 
    print(option)
chosen_product = input('For which products are you looking for? ')
chosen_product = chosen_product.lower() 

if chosen_product in menu.keys():
    print("The products available are: ")
    for product in menu[chosen_product]:
        print(product)
    chosen_product = input('Which product would you like? ')
    chosen_product = chosen_product.lower()
    chosen_product_price = menu[chosen_product][chosen_product]
    print(f"It will cost you {chosen_product_price} Czech Crowns")

else:
    print("We don't sell that here. Try again next time")

