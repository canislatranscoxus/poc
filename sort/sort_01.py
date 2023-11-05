'''
links:
https://www.kite.com/python/answers/how-to-sort-a-list-with-a-lambda-expression-in-python

suppouse we have a list of tuples with

( Fruit, quantity, price )

let's sort by Fruit.

'''

data = [("Apples", 5, "20"), ("Pears", 1, "5"), ("Oranges", 6, "10")]

data.sort( key = lambda x: x[0] )

print(data)