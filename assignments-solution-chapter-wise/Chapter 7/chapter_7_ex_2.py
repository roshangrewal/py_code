fh = input('Enter the file name: ');
if len(fh) == 0:
    fh = 'mbox-short.txt';
file = open(fh);

count = 0;
total = 0.0;
average = 0.0;

for line in file:
    if not 'X-DSPAM-Confidence:' in line:
        continue;

    count += 1;

    # line = line.rstrip();
    position = line.find(':');
    # print(position);
    value = float(line[position+1:]);
    total += value;

average = total/count;
print('Average spam confidence: ', average);
