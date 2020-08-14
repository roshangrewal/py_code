data = 'X-DSPAM-Confidence: 0.8475 ';

firstPos = data.find(':');

temp = data[firstPos+2:];

value = float(temp);

print(value);
