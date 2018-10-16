freq = {}
freq[' '] = 700000000
freq['e'] = 390395169
freq['t'] = 282039486
freq['a'] = 248362256
freq['o'] = 235661502
freq['i'] = 214822972
freq['n'] = 214319386
freq['s'] = 196844692
freq['h'] = 193607737
freq['r'] = 184990759
freq['d'] = 134044565
freq['l'] = 125951672
freq['u'] = 88219598
freq['c'] = 79962026
freq['m'] = 79502870
freq['f'] = 72967175
freq['w'] = 69069021
freq['g'] = 61549736
freq['y'] = 59010696
freq['p'] = 55746578
freq['b'] = 47673928
freq['v'] = 30476191
freq['k'] = 22969448
freq['x'] = 5574077
freq['j'] = 4507165
freq['q'] = 3649838
freq['z'] = 2456495

def singleByteKeyXor(encodedString,key) :
	decodedString = ''
	for i in encodedString :
		decodedString += chr(ord(i) ^ ord(key))
	return decodedString

def scores(decodedString) :
	score = 0
	for i in decodedString :
		try :
			score += freq[i]
		except :
			continue
	return score

g = open('4-decoded.txt','a')
f = open('4.txt','r')
for lines in f.readlines() :
	encodedString = lines.rstrip().decode('hex')
	maxScore = 0
	actualString = ''
	for key in range(256) :
		decodedString = singleByteKeyXor(encodedString,chr(key))
		score = scores(decodedString)
		if score > maxScore :
			maxScore = score
			actualString = decodedString.encode('hex')
	g.write(actualString+'\n')
	
f.close()
g.close()

curMaxScore = 0
curBestStr = ''
f = open('4-decoded.txt','r')
for lines in f.readlines() :
	line = lines.rstrip()
	score = scores(line.decode('hex'))
	if score > curMaxScore :
		curMaxScore = scores
		curBestStr = line.decode('hex')

print curBestStr