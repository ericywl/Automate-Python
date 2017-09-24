import string

def caesar(text):
	i = 0
	while i < 25:
		output = []
		for c in text:
			index = string.ascii_lowercase.index(c)
			output.append(string.ascii_lowercase[(index-i)%26])
		print "".join(output)
		i += 1

# startigrabbedeverythingicouldfindpleasereturnanyblueprintsforvaultandalarmdesignbasedonwhichbankyoudecideoniamsettingupsafehouseco
# zenameblackoutworriedthatourcipheristooweakonnextmessageswitchtovigenerecipherkeywordisthehiddensymbolofdeathinmyfavoriteholbeinend

def vigenere(text):
	key = "sskkuullll"
	key_list = [string.ascii_lowercase.index(i) for i in key]
	output = []
	count = 0
	for c in text:
		index = string.ascii_lowercase.index(c)
		key_index = index - key_list[count%len(key)]
		count += 1
		output.append(string.ascii_lowercase[key_index%26])
	print "".join(output)

# startwarningiheardreportofourbreakinonthenewsstillwaitingonalarmtestschedulesiwillreportbacktomorrowwithfinalplanforextrasecurityisuggestweburnourlettersafterreadingandswitchourletterstonumbersusingpolybiussquaredropmessageunderthebenchattrainstationend

def polybius_square(text):
	count = 0
	output = []
	polybius = ["afkpu","bglqv","chmrw","dinsx","ejoty"]
	for x in [text[i:i+2] for i in range(0, len(text), 2)]:
		output.append(polybius[int(x[0])-1][int(x[1])-1])
	print "".join(output)

# startalmostfinishedblackoutitisinshedonthirdaveworkingonastrongercipherforfuturemessagesitissurelyunbreakableitcombinesourpreviousmethodsrwktd