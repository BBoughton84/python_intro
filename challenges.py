"""
write a func hat gets last char in a string
"""

# def get_last_char(arg):
#     return arg[-1]
#
# print(get_last_char('twister'))


"""
takes a tsting and an intersre adn retursn the stirng repated that many number o times
intput 3, "string"
output "stringstringstring"
"""

def repeat_string(num, item):
    i = 0
    x = ''
    while i<num:
        x += item
        i += 1
    return x

print(repeat_string(4, "Blah"))
