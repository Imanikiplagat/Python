# Q1 calculating discount
def calculate_discount (price , discount_percentage) :
    if discount_percentage >= 20:
        discount_amount = (discount_percentage /100) * price
        final_price =price - discount_amount
        return (final_price)
    else:
        return price
    
# Q2 user input
try :
    price = int(input("Enter your price: "))   
    discount_percent = int(input("enter your discount percentage: ")) 

    final_price = calculate_discount(price ,discount_percent)

    if discount_percent >= 20 :
        print("Final price is" , final_price)
    else:
        print("Oops!No discount for you ,final price is :" , final_price) 

except ValueError:
    print("Please enter a valid number.")           