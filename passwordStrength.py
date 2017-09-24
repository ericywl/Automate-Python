#! python2

# automatetheboringstuff.com/chapter7 Strong Password Detection
# 8 digits long password with upper, lower characters and >0 digits
import re

def passwordStrength(password):
	passwordUpperRegex = re.compile(r"[A-Z]")
	passwordLowerRegex = re.compile(r"[a-z]")
	passwordDigitRegex = re.compile(r"[0-9]")
	passwordLengthRegex = re.compile(r".{8,}")

	condition = [
					passwordLengthRegex.search(password),
					passwordUpperRegex.search(password),
					passwordLowerRegex.search(password),
					passwordDigitRegex.search(password)
				]

	if None in condition:
		print "The password is not strong, please change it."
	else:
		print "The password is strong."

passwordStrength("Mk6mv90-")