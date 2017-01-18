#! python 3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

# Phone Regex
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?      		# area code
	(\s[-]\.)?						# separator
	(\d{3})							# first three digits
	(\s[-]\.)						# separator
	(\d{4})							# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))? 	# extension
	)''', re.VERBOSE)

# Email Regex
emailRegex = re.compile(r'''(
	# One or more characters that can be uppercase or lowercase
	# letters, numbers, a dot, an underscore, a percent sign
	# a plus sign, or a hyphen.  
	[a-zA-Z0-9._%+-]+				# username
	@								# @ symbol
	[a-zA-Z0-9.-]+					# domain name
	(\.[a-zA-Z]{2,4})				# dot-something
	)''', re.VERBOSE)

#Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')