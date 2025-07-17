import sys

count = 0
with open(sys.argv[1], 'r') as file:
    for line in file:
        if line[0] != "#" and line[0] != " ":
            line = line.strip()
            alist = line.split()
            for i in range(1, len(alist), 2):
                count += int(alist[i])
    print(f"{count:_}")

if __name__ == '__main__':
    file = __file__

'''
https://github.com/RichardGoodrich/addz.git

Python Tutorial: File Objects - Reading and Writing to Files
https://youtu.be/Uh2ebFW8OYM?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

'''
