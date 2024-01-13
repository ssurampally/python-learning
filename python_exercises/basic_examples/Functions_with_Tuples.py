# functions with loops on Tuples

customers = [('C100', 'Kevin', 'Canada', 2000), ('C200', 'Chris', 'USA', 3000), ('C300', 'Rich', 'USA', 1500)]

def topcustomer (customers):
    customername = ''
    revenue = 0

    for custno, name, country, rev  in customers:
        if rev > revenue:
            revenue = rev
            custname = name
       
    return revenue, custname

maxrev = topcustomer(customers)

print (maxrev)

