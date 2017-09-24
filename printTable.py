# automatetheboringstuff.com/chapter6 printTable function
tableData = [
				['apples', 'oranges', 'cherries', 'banana'],
				['Alice', 'Bob', 'Carol', 'David'],
				['dogs', 'cats', 'moose', 'goose']
			]

def printTable(tableData):
	colWidths = [len(max(tableData[i], key=len)) for i in xrange(len(tableData))]
	output = []
	for j in xrange(len(tableData[0])):
		temp_list = []
		for i in xrange(len(tableData)):
			temp_list.append(tableData[i][j].rjust(colWidths[i]))
		output.append(" ".join(temp_list))
	return "\n".join(output)

print printTable(tableData)
