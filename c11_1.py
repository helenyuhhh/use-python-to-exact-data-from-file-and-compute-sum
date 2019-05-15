#extracting numbers using regular expression from a file and
#compute the sum-----by H(QH).Y
import re
ofile = open('real.txt', 'r')
numbers = list()
sum = 0
for lines in ofile:
    lines.rstrip()
    number = re.findall('[0-9]+', lines) #number is a list of int
    if len(number) > 0:
        for num in number:
            numbers.append(num)
for numb in numbers:
    sum = sum + int(numb)
print(sum)
