#! python2

# automatetheboringstuff.com/chapter6 bulletPointAdder
# Adds bullet points to the start of each line on the clipboard
import pyperclip

text = pyperclip.paste()
lines = text.split("\n")

for i in range(len(lines)):
	lines[i] = "* " + lines[i]

text = "\n".join(lines)
pyperclip.copy(text)