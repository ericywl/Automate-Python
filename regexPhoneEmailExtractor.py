#! python2

# automatetheboringstuff.com/chapter7 PhoneAndEmail
# Extracts phone numbers and email addresses from clipboard
import re
import pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-=]+				# username
	@								# @ symbol
	[a-zA-Z0-9.-]+					# domain name
	(\.[a-zA-Z]{2,4})				# dot-something
	)''', re.VERBOSE)

text = pyperclip.paste().encode('utf-8')
phoneNumList = []
for matches in phoneRegex.findall(text):
	phoneNum = "-".join([matches[1], matches[3], matches[5]])
	if matches[8] != "":
		phoneNum += " x" + matches[8]
	phoneNumList.append(phoneNum)

emailList = []
for matches in emailRegex.findall(text):
	emailList.append(matches[0])

if len(phoneNumList) == 0 and len(emailList) == 0:
	print "No phone numbers or email addresses found."
elif len(phoneNumList) == 0:
	print "No phone numbers found."
	pyperclip.copy("\n".join(emailList))
	print "Email address copied to clipboard:"
	print "\n".join(emailList)
elif len(emailList) == 0:
	print "No email addresses found."
	pyperclip.copy("\n".join(phoneNumList))
	print "Phone numbers copied to clipboard:"
	print "\n".join(phoneNumList)
else:
	phoneNumMatches = "Phone numbers:\n" + "\n".join(phoneNumList)
	emailMatches = "Email addresses:\n" + "\n".join(emailList)
	pyperclip.copy("\n".join([phoneNumMatches, emailMatches]))
	print "Matches copied to clipboard:"
	print "\n".join([phoneNumMatches, emailMatches])