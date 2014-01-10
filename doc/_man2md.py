#!/usr/bin/env python
import sys

f = open(sys.argv[1])

out = "---\nlayout: default\ntitle: Hexcap/Documentation\n---"

nl = True
for line in f:
  if(line.startswith('.')):
    if(line.startswith('.\\\"')):
      continue
    elif(line.startswith('.TH')):
      continue
    elif(line.startswith('.SH')):
      out += '## ' + ' '.join(line.split(' ')[1:])
    elif(line.startswith('.I')):
      nl = False
    elif(line.startswith('.TP')):
      out += '* '
  else:
    if(line.startswith('>')):
      line = '\\' + line

    if(nl):
      out += line + '\n'
    else:
      out = out[:-2] + line
      nl = True


f.close()

print out
