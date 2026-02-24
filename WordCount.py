#WordCount.py
#Name: William Headlee
#Date: 2/24/26
#Assignment: Lab 6

def main():
  textFile = open("gettysberg.txt", 'r')

  lines = 0
  words = 0
  characters = 0
  
  for line in textFile:
    lines += 1
    w = line.split()
    c = list(line)
    for word in w:
      words += 1
    for char in c:
      characters += 1
      
  print("Lines: " + str(lines))
  print("Words: " + str(words))
  print("Characters: " + str(characters))
  

if __name__ == '__main__':
  main()
