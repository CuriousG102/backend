import csv
import re

def main():
    inFileName = raw_input("What is the path to the file to be converted?: ")
    outFileName = raw_input("What is the path to the file to be output?: ")
    inFile = open(inFileName)
    outFile = open(outFileName, "w")
    convertToCSV(inFile, outFile)
    inFile.close()
    outFile.close()

def convertToCSV(inFile, outFile):
    header = inFile.readline()
    
    blankSpaces = [(m.start(0), m.end(0)) for m in re.finditer(r'\s{2,}', header)]

    # follows this format: [(columnName, startInclusive, endExclusive)]
    columnReferences = [(header[0:blankSpaces[0][0]], 0, blankSpaces[0][1])]
    for i in xrange(0, len(blankSpaces) - 2):
        startInclusive = blankSpaces[i][1]
        endExclusive = blankSpaces[i+1][1]
        columnName = header[startInclusive:blankSpaces[i+1][0]]
        columnReference = (columnName, startInclusive, endExclusive)
        columnReferences.append(columnReference)
    # last column is edge case because the # showing the end of the header row
    # is not necessarily as far out as the # at the end of other rows.
    # This necessitates just getting the starting index of the last column and
    # then finding the # that denotes its end on various lines
    # follows format: (lastColumnName, startInclusive)
    startInclusive = blankSpaces[-2][1]
    lastColumn = (header[startInclusive:blankSpaces[-1][0]], startInclusive)
    print columnReferences
    print lastColumn


    sheetWriter = csv.writer(outFile)
    columnNames = [reference[0] for reference in columnReferences]
    columnNames.append(lastColumn[0])
    sheetWriter.writerow(columnNames)

    for lineNo, row in enumerate(inFile, start=2):
        rowToWrite = []
        for columnReference in columnReferences:
            try:
                rowToWrite.append(row[columnReference[1]:columnReference[2]].strip())
            except:
                print lineNo
                print row
                print columnReference
                raise
        try:
            rowToWrite.append(row[lastColumn[1]:row.find('#')])
            sheetWriter.writerow(rowToWrite)
        except:
            print lineNo
            print row
            raise

if __name__ == '__main__': main()