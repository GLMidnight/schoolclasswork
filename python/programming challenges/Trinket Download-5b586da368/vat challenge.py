def get_price():
    price = float(raw_input("How much does the item cost?"))
    return price

def VAT(price):
    VAT = round(.2 * price,2)
    return VAT

def final_price(price,VAT):
    final_price = price - VAT
    return final_price

def display(price, VAT):
    print "You paid £","%.2f" % price
    print "The VAT you paid came to £","%.2f" % VAT
    print "Your final payment after VAT is £","%.2f" % final_price

price = get_price()
VAT = VAT(price)
final_price = final_price(price,VAT)
display(price,VAT)