#WordIndex.py
#Name: William Headlee
#Date: 2/24/26
#Assignment: Lab 6

def main():
    textFile = open("fish.txt", 'r')

    words = {} #create an empty dictionary

    lineNum = 1
    for line in textFile:
        w = line.split()
        for word in w:
            word = word.strip(".,!?").lower()
            if word in words:
                words[word].append(lineNum)
            else:
                words[word] = [lineNum]
        lineNum += 1

    for word in words:
        print(word, ":", words[word])

if __name__ == '__main__':
    main()
