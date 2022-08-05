from sys import argv
import geopandas

script, callback = argv
print(callback)
callback = input("do you want me to say something else to you?/n")
print(callback)