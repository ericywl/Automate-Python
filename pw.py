#! python2

# automatetheboringstuff.com/chapter6 pw batch file
# uses Windows Run command "pw [account]" to copy password
import sys, pyperclip

passwords = {
				"email": "@5>&Cc;5`4Aq_4=V",
				"blog": "eJ&h.A\"Z9+hNs}_c",
				"facebook": "`^yj[W=6G`ND4)kn"
			}

if len(sys.argv) < 2:
	print "Usage: python pw.py [account] - copy account password"
	sys.exit()

account = sys.argv[1]

if account in passwords:
	pyperclip.copy(passwords[account])
	print "Password for {} copied to clipboard.".format(account)
else:
	print "There is no account named {}.".format(account)