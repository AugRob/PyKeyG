import random
import hashlib
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("key_len")
	args = parser.parse_args()

	
    numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    specChars = ['!', '"', "'", '@', '#', '$', '%', '&', '(', ')', '*', '+', '=', '`', '-', '.', '/', ':', ';', '<', '>', ',', '?', '[', ']', '{', "}", '\\', '_', '|', '~']

    charList = numList + alphabet + specChars

    randList = []
    
    keyLength = int(raw_input("Desired key length: "))
    
    
    while len(randList) < keyLength:
        randList.append(charList[random.randint(0, len(charList) - 1)])

    key = ""
    hsh = ""
    numRnd = 0

    for i in range(0, keyLength):
		
		for i in range(0, len(hsh)):
			if hsh[i] not in alphabet:
				numRnd += int(hsh[i])
				
		hashNum = int(numRnd)		
		while hashNum > len(randList):
			hashNum = hashNum / (random.randint(2,4))
		
		print hashNum
		
		for	i in range(0, hashNum):
			random.shuffle(randList)
		
		key += str(randList[random.randint(0, len(randList) - 1)])
		hsh += str(hashlib.sha224(key).hexdigest())

    print "KEY: ", str(key)
 

if __name__ == '__main__':
    main()
