#!/usr/bin/env python
import sys

f = open(sys.argv[1])

out = "---\nlayout: default\ntitle: Hexcap/Documentation\n---"

I = False
TP = False
for line in f:
  if(line.startswith('.')):
    if(line.startswith('.\\\"')):
      continue
    elif(line.startswith('.TH')):
      continue
    elif(line.startswith('.SH')):
      out += '## ' + ' '.join(line.split(' ')[1:])
    elif(line.startswith('.I')):
      I = True
    elif(line.startswith('.TP')):
      TP = True
  else:
    if(line.startswith('>')):
      line = '\\' + line

    if(I):
      out = out[:-2] + line
      I = False
    elif(TP):
      out += "**" + line.strip() + "** "
      TP = False
    else:
      out += line + '\n'

f.close()
print out
