import sys
import base64

def convert2png(fileName):
	print("function " + fileName)
	i = 0
	with open(fileName,"rb") as inf:
		for line in inf:
			if b'imagetype="PNG"' in line:
				pngData = base64.b64decode(inf.readline()[:-2])
				pngFilename = "%02d.png" % i
				pngFile = open(pngFilename,"wb")
				pngFile.write(pngData)
				pngFile.close()
				i += 1

if len(sys.argv) == 2:
	inputFile = sys.argv[1]
	print("Preparing to convert " + inputFile)
	convert2png(inputFile)
