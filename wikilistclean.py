import re
#Cleaning data
path = 'wikilist.txt'
fhand = open(path,encoding='cp1252').read()
lines = fhand.split('\n')
lst = list()
for line in lines:
    line = re.sub("\(.*", " ", line)
    line = re.sub("c\..*", " ", line)
    line = re.sub("of.*", " ", line)
    line = re.sub("[0-9].*", " ", line)
    line = re.sub("\,.*", " ", line)
    line = re.sub(".\sA\spupil", " ", line)
    line = re.sub("\.\sFollower", " ",line)
    line = re.sub("\.\sPythagorean.", " ",line)
    if 'philosopher' in line:
        line = " "
    if re.findall("\S", line):
        lst.append(line)

#Reduce down to most well-known name

final_list = []
for names in lst:
    words = names.split(' ')
    words = words[:-2]

    if 'the' in words:
        words = words[0]
    elif len(words) > 1 :
        words = words[len(words)-1]
    elif len(words) == 1:
        words = words[0]
    if words == [] or words == '' or words == 'de' or words == '\n':
        continue
    final_list.append(words)


#Send to text file
def write_to_file(list_name, file_name):
    fhand = file_name
    file = open(fhand, "w")
    for i in list_name:
        file.write(i)
        file.write("\n")
    file.close()

write_to_file(final_list, "clean_list.txt")
write_to_file(lst, "clean_list_backup.txt")
