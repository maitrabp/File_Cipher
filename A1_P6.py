# Maitra Patel - Question 6 (Python)
def encode(encodedDictionary, inputF, outputF):
    # Iterating through the file line by line
    for line in inputF:
        for character in line:
            if encodedDictionary.__contains__(character):
                character = encodedDictionary[character]
            outputF.write(character)


def decode(decodedDictionary, inputF, outputF):
    # Iterating through the file line by line
    for line in inputF:
        for character in line:
            if decodedDictionary.__contains__(character):
                character = decodedDictionary[character]
            outputF.write(character)


# Read from Independence.txt file
inputF = open('Independence.txt', 'r')

# Write to Independence2.txt file
outputF1 = open('Independence2.txt', 'w')

# Write to Independence2.txt file
outputF2 = open('Independence3.txt', 'w')

plainText = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ciperText = 'DEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABC'

# This will split the string into a list of characters
plainTextList = []
plainTextList[:] = plainText
print(plainTextList)

ciperTextList = []
ciperTextList[:] = ciperText
print(ciperTextList)

# key-value pairing plain text with ciper text
encodedDictionary = dict(zip(plainTextList, ciperTextList))
decodedDictionary = dict(zip(ciperTextList, plainTextList))
print(decodedDictionary)

# ENCODE
encode(encodedDictionary, inputF, outputF1)
inputF.close()
outputF1.close()

# DECODE
outputF1 = open('Independence2.txt', 'r')
decode(decodedDictionary, outputF1, outputF2)
outputF1.close()
outputF2.close()
