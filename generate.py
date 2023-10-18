import random
import string

import re

# Define the character classes
lowercase_letters = string.ascii_lowercase
digits = string.digits

# Combine the character classes
character_classes = lowercase_letters + digits

# letters numbers
rates = {}
rates["zero_ten"] = 0
rates["one_nine"] = 0
rates["two_eight"] = 0
rates["three_seven"] = 0
rates["four_six"] = 0
rates["five_five"] = 0
rates["six_four"] = 0
rates["seven_three"] = 0
rates["eight_two"] = 0
rates["nine_one"] = 0
rates["ten_zero"] = 0

anomalies = []

for x in range(0,10000):

    # Generate a 10-character string
    password = ''.join(random.choice(character_classes) for _ in range(10))

    print(password)

    # Check if the generated string matches the regex
    regex_pattern = r"^(?=(?:.*[a-z]){0})(?=(?:.*[0-9]){10})[a-z0-9]{10}$"
    if re.match(regex_pattern, password):
        rates["zero_ten"] = rates["zero_ten"] + 1
        anomalies.append(password)


    regex_pattern = r"^(?=(?:.*[a-z]){1})(?=(?:.*[0-9]){9})[a-z0-9]{10}$"
    if re.match(regex_pattern, password):
        rates["one_nine"] = rates["one_nine"] + 1
        anomalies.append(password)

    regex_pattern = r"^(?=(?:.*[a-z]){2})(?=(?:.*[0-9]){8})[a-z0-9]{10}$"
    if re.match(regex_pattern, password):
        rates["two_eight"] = rates["two_eight"] + 1

    regex_pattern = r"^(?=(?:.*[a-z]){3})(?=(?:.*[0-9]){7})[a-z0-9]{10}$"
    if re.match(regex_pattern, password):
        rates["three_seven"] = rates["three_seven"] + 1

    # Check if the generated string matches the regex
    regex_pattern = r"^(?=(?:.*[a-z]){4})(?=(?:.*[0-9]){6})[a-z0-9]{10}$"
    if re.match(regex_pattern, password):
        rates["four_six"] = rates["four_six"] + 1

    regex_pattern = r"^(?=(?:.*[a-z]){5})(?=(?:.*[0-9]){5})[a-z0-9]{10}$"
    if re.match(regex_pattern, password):
        rates["five_five"] = rates["five_five"] + 1

    regex_pattern = r"^(?=(?:.*[a-z]){6})(?=(?:.*[0-9]){4})[a-z0-9]{10}$"
    if re.match(regex_pattern, password):
        rates["six_four"] = rates["six_four"] + 1

    regex_pattern = r"^(?=(?:.*[a-z]){7})(?=(?:.*[0-9]){3})[a-z0-9]{10}$"
    if re.match(regex_pattern, password):
        rates["seven_three"] = rates["seven_three"] + 1
    
    # Check if the generated string matches the regex
    regex_pattern = r"^(?=(?:.*[a-z]){8})(?=(?:.*[0-9]){2})[a-z0-9]{10}$"
    if re.match(regex_pattern, password):
        rates["eight_two"] = rates["eight_two"] + 1

    regex_pattern = r"^(?=(?:.*[a-z]){9})(?=(?:.*[0-9]){1})[a-z0-9]{10}$"
    if re.match(regex_pattern, password):
        rates["nine_one"] = rates["nine_one"] + 1

    regex_pattern = r"^(?=(?:.*[a-z]){0})(?=(?:.*[0-9]){10})[a-z0-9]{10}$"
    if re.match(regex_pattern, password):
        rates["ten_zero"] = rates["ten_zero"] + 1
        anomalies.append(password)




print(str(rates["zero_ten"]/100)+ '% are rates["zero_ten"]')
print(str(rates["one_nine"]/100)+ '% are rates["one_nine"]')
print(str(rates["two_eight"]/100)+ '% are rates["two_eight"]')
print(str(rates["three_seven"]/100)+ '% are rates["three_seven"]')
print(str(rates["four_six"]/100)+ '% are rates["four_six"]')
print(str(rates["five_five"]/100)+ '% are rates["five_five"]')
print(str(rates["six_four"]/100)+ '% are rates["six_four"]')
print(str(rates["seven_three"]/100)+ '% are rates["seven_three"]')
print(str(rates["eight_two"]/100)+ '% are rates["eight_two"]')
print(str(rates["nine_one"]/100)+ '% are rates["nine_one"]')
print(str(rates["ten_zero"]/100)+ '% are rates["ten_zero"]')

print(anomalies)
