# automatetheboringstuff.com/chapter7 Regex
import re

# {} specify the number of times to match
phoneNumRegex1 = re.compile(r"(\d{3})-(\d{3}-\d{4})")
phoneMO1 = phoneNumRegex1.search("My number is 415-555-2222.")
areaCode1, mainNum1 = phoneMO1.groups()
print "Phone number found: {}\nArea code: {}\nMain number: {}\n".format(phoneMO1.group(), areaCode1, mainNum1)

# \( \) escapes the brackets to make them matchable
phoneNumRegex2 = re.compile(r"(\(\d{3}\)) (\d{3}-\d{4})")
phoneMO2 = phoneNumRegex2.search("My number is (432) 437-2342.")
areaCode2, mainNum2 = phoneMO2.groups()
print "Phone number found: {}\nArea code: {}\nMain number: {}\n".format(phoneMO2.group(), areaCode2, mainNum2)

# Python's regex is by default greedy (ie. finds the longest)
greedyHaRegex = re.compile(r"(Ha){3,5}")
greedyHaMO = greedyHaRegex.search("HaHaHaHaHaHa")
print greedyHaMO.group()

# use ? to make it non-greedy
nongreedyHaRegex = re.compile(r"(Ha){3,5}?")
nongreedyHaMO = nongreedyHaRegex.search("HaHaHaHaHa")
print nongreedyHaMO.group()

# | matches any of the combination
heroRegex = re.compile(r"Batman|Superman")
heroMO1 = heroRegex.search("Batman and Superman.")
heroMO2 = heroRegex.search("Superman and Batman.")
print heroMO1.group()
print heroMO2.group()
print ""

batRegex1 = re.compile(r"Bat(man|mobile|woman|cave)")
batMO1 = batRegex1.search("Batmobile lost a wheel.")
print batMO1.group()
print batMO1.group(1)
print ""

# ? matches 0 or 1, optional matching
batRegex2 = re.compile(r"Bat(wo)?man")
batMO2_1 = batRegex2.search("The Adventures of Batman")
batMO2_2 = batRegex2.search("The Adventures of Batwoman")
print batMO2_1.group()
print batMO2_2.group()
print ""

# * matches 0 or more, + matches 1 or more
lolRegex1 = re.compile(r"(lo)*l")
lolRegex2 = re.compile(r"(lo)+l")
lolMO1_1 = lolRegex1.search("This is so funny, lololololololololol!")
lolMO1_2 = lolRegex1.search("I'm dying, l")
lolMO2_1 = lolRegex2.search("This is so funny, lololololololololol!")
lolMO2_2 = lolRegex2.search("I'm dying, l")
print lolMO1_1.group()
print lolMO1_2.group()
print lolMO2_1.group()
print lolMO2_2
print ""

# findall() method
phoneNumRegex3 = re.compile(r"\d{3}-\d{3}-\d{4}") # no groups
phoneNumRegex4 = re.compile(r"(\d{3})-(\d{3})-(\d{4})") # has groups
print phoneNumRegex3.findall("Cell: 415-555-9999 Work: 212-555-0000")
print phoneNumRegex4.findall("Cell: 415-555-9999 Work: 212-555-0000")

# Character class
'''
\d
Any numeric digit from 0 to 9.

\D
Any character that is not a numeric digit from 0 to 9.

\w
Any letter, numeric digit, or the underscore character. (Think of this as matching "word" characters.)

\W
Any character that is not a letter, numeric digit, or the underscore character.

\s
Any space, tab, or newline character. (Think of this as matching "space" characters.)

\S
Any character that is not a space, tab, or newline.

[0-5]
(0|1|2|3|4|5)
'''

# [^ ] makes a negative character class
vowelRegex1 = re.compile(r"[aeiouAEIOU]")
vowelRegex2 = re.compile(r"[^aeiouAEIOU]")
print vowelRegex1.findall("Robocop eats baby food. BABY FOOD.")
print vowelRegex2.findall("Robocop eats baby food. BABY FOOD.")
print ""

# ^ without the square brackets indicate start, $ indicate end of string
helloRegex = re.compile(r"^(h|H)ello")
endsWithNumberRegex = re.compile(r"\d$")
wholeStringNumRegex = re.compile(r"^\d+$")
print helloRegex.search("Hello it's me!").group()
print helloRegex.search("well, hello it's me!")
print endsWithNumberRegex.search("My score is 83").group()
print endsWithNumberRegex.search("I got 52 for that test.")
print wholeStringNumRegex.search("123822930").group()
print wholeStringNumRegex.search("123xso3940")
print ""

# . matches any character except newline, .* matches anything (greedy)
atRegex = re.compile(r".at")
nameRegex = re.compile(r"First name: (.*), Last name: (.*)")
print atRegex.findall("My cat sat on a flat hat.")
print nameRegex.search("First name: Eric, Last name: Yap").group(1)
print nameRegex.search("First name: Eric, Last name: Yap").group(2)
print ""

# non-greedy .* matching
greedyNameRegex = re.compile(r"<.*>")
nongreedyNameRegex = re.compile(r"<.*?>")
print greedyNameRegex.search("<Name is> Eric>").group()
print nongreedyNameRegex.search("<Name is> Eric>").group()
print ""

# re.DOTALL matches everything including newline
noNewlineRegex = re.compile(r".*")
newlineRegex = re.compile(r".*", re.DOTALL)
print [noNewlineRegex.search("Hi guys.\nPlease no Kappa\nXD").group()]
print [newlineRegex.search("Hi guys.\nPlease no Kappa\nXD").group()]
print ""

# re.I or re.IGNORECASE does case-insensitive matching
robocopRegex = re.compile("robocop", re.I)
print robocopRegex.search("Robocop is part man, part machine, all cop.").group()
print robocopRegex.search("ROBOCOP DESTROY!!!").group()
print robocopRegex.search("RoBoCoP 1337 lang.").group()

# re.VERBOSE ignores whitespace and comments
phoneVerboseRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)