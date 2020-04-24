print("{}, World!!".format("Hello"))
"""print("{} World{}".format("Hello"))  This will give an error cause the no of 
placeholder is 2 and the value give is for only 1"""
#  Using multiple place holders
print("Hello my name is {} and im {} years old".format("Preet", 20))

#  Use of positional key arguments in format
print("{0} and {1}".format("Orange", "Apple"))
print("{1} and {0}".format("Orange", "Apple"))

#  Use of Keyword arguments
print("{o} and {a}".format(o='Orange', a='Apple'))
print("{a} and {o}".format(o="Orange", a="Apple"))

"""More parameters can be included within the curly braces of our syntax. Use the 
format code syntax {field_name:conversion}, where field_name specifies the index number of the 
argument to the str.format() method, and conversion refers to the conversion code of the data type."""
#  s --> strings
#  d --> decimal integer(base-10)
#  f --> floating point display
#  c --> character(turns integer value into character of the same ascii value)
#  b --> binary
#  o --> octal
#  x --> hexadecimal with lowercase letters after 9
#  X --> hexadecimal with uppercase letters after 9

print("{0:s} is string".format('hello'))
print("{0:c} is character".format(65))
print("{0:b} is binary of 12".format(12))
print("{0:o} is octal of 12".format(12))
print("{0:x} is hexadecimal of 12".format(12))
print("{0:X} is hexadecimal of 12".format(12))

"""By default strings are left-justified within the field, and numbers are right-justified. We can modify this 
by placing an alignment code just following the colon."""

#  <   :  left-align text in the field
#  >   :  right-align text in the field
#  ^   :  center text in the field

print("Hello {:<5} are you".format("How"))
print("Hello {:>5} are you".format("How"))
print("Hello {:^5} are you".format("How"))

#  You can show any symbol instead of space if u type that symbol just after ':'  .
print("Hello {:#<7} are you".format("How"))


print("{:d} {:d}".format(12, 13))
print("{:<4d} {:<4d}".format(12, 13))

numb = 1
for i in range(0,3):
    for j in range(0,3):
        print("{}".format(numb), end='')
        numb += 1
    print()
