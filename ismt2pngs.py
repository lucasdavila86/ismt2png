import os
import sys
import base64

def convert2png(fileName, outputFolder):
	i = 0
	with open(fileName,"rb") as inf:
		for line in inf:
			if b'imagetype="PNG"' in line:
				pngData = base64.b64decode(inf.readline()[:-2])
				pngFilename = "%02d.png" % i
				destination = os.path.join(outputFolder, pngFilename)
				pngFile = open(destination,"wb")
				pngFile.write(pngData)
				pngFile.close()
				i += 1

if len(sys.argv) == 3:
	inputFile = sys.argv[1]
	outputFolder = sys.argv[2]
	print("Preparing to convert " + inputFile)
	print("Output folder " + outputFolder)
	if not os.path.exists(outputFolder):
		os.makedirs(outputFolder)
	convert2png(inputFile, outputFolder)
