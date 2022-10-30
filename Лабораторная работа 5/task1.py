# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

amount = 15

pprint([{"dec": i, "bin": bin(i), "oct": oct(i), "hex": hex(i)} for i in range(amount+1)])