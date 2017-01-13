#Catches a phone number with hyphens
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#Catches a phone number  wrapping the area code and the number in two groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#Catches a phone number INCLUDING parentheses, also two groups
phoneNumRegex = re.compile(r'(\(\d\d\d\))(\d\d\d-\d\d\d\d)')
#The string 'Batman' or the string 'Tina Fey' 
heroRegex = re.compile(r'Batman|Tina Fey')
#'Bat' followed by either man, mobile, copter or bat
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
#'Bat' then zero or one times 'wo' then man
#Catches 'Batman' and 'Batwoman'
batRegex = re.compile(r'Bat(wo)?man')
#Phone number with or without area code
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
#'Bat' followed by zero or MORE 'wo' then 'man'
batRegex = re.compile(r'Bat(wo)*man')