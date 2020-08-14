fh = input('Enter the file name: ');

if(fh == 'mbox.txt' or 'mbox-short.txt'):
    file = open(fh,'r');
    count = 0;
    for line in file:
        if not 'Subject:' in line:
            continue;
        count+=1;
    print('There were '+ str(count) + ' subject lines in ' + fh);

elif(fh == 'na na boo boo'):
    print(fh.upper() + ' - You have been punk"d!')

else:
    print('File cannot be opened: '+ fh)
