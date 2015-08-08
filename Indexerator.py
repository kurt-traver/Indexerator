from collections import defaultdict

def main():
	IndexEntries = defaultdict(list)

	#	Read in the source reverse index and parse it into IndexEntries
	fileName = raw_input("What file would you like to indexify?")
	try:
		with open(fileName,"r") as fileToIndex:
			parseFile(fileToIndex,IndexEntries)
	except IOError:
		print "Could not open file."

	#	Process IndexEntries and write it to a destination index file
	fileName = raw_input("What file would you like to write the index to?")
	try:
		with open(fileName,"w") as fileToWriteIndexTo:
			generateCSVForDict(IndexEntries,fileToWriteIndexTo)
	except IOError:
		print "Could not write file.\r"

def parseFile(fileToParse,indexDict):
	#	Iterate through each line of the file to process into the dict
	bookNumber = ''

	for line in fileToParse:
		#	Split each line on '  ' and make sure that it's conformant.
		#	Non-coforming lines are skipped
		splitLine = line.split('  ')
		if len(splitLine) != 2:
			continue
		page = splitLine[0]
		terms = splitLine[1]

		#	Check for if the line is the book index. 
		#	If it is, the book number will be prepended to each page.
		if page=="Book":
			bookNumber=terms.strip()
			bookNumber+='.'
			continue
		page = bookNumber + page

		#	Get all the terms out of the line and add them to the dict, if they aren't yet
		#	Then insert the terms at the key
		termList = terms.split(',')
		for term in termList:
			term = term.strip()
			term = term.lower()

			indexDict[term].append(page)

	print "Index dict was built\r"

def generateIndexForDict(dictToParse,fileToWriteIndexTo):
	for term,pages in sorted(dictToParse.items()):
		pageString = ", ".join(pages)
		stringToWrite = ""
		fileToWriteIndexTo.write("%-40s %40s\n" % (term,pageString))

def generateCSVForDict(dictToparse,fileToWriteIndexTo):
	for term,pages in sorted(dictToparse.items()):
		pageString = ", ".join(pages)
		stringToWrite = term + "|" + pageString + "\n"
		fileToWriteIndexTo.write(stringToWrite)

if __name__ == '__main__':
	main()