import re

txt=input("Enter Pincode:  ")

regex_integer_in_range= '^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$'
regex_alternating_repetitive_digit_pair=r'(?=(\d)\d\1)'

result=(bool(re.match(regex_integer_in_range,txt)) and len(re.findall(regex_alternating_repetitive_digit_pair,txt))<2)

print(result)
