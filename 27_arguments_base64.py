#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import sys
import re

class ansi:
  RB = '\x1b[1;31m'
  GB = '\x1b[1;36m'
  BD = '\x1b[1m'
  RS = '\x1b[0m'

b64_var = 'd2l0aCBncmVhdCBwb3dlciwgY29tZXMgZ3JlYXQgcmVzcG9uc2liaWxpdHkK'

# check if argument is passed so len == 2 (arg0 == script, arg1 == second argument but first usable sys.argv[1])
#if len(sys.argv) == 2:
#  print('>>> sys.argv[0] is the name of the script, like in bash "${0}", script_name: ', ansi.GB, sys.argv[0], ansi.RS)
#  b64_arg = sys.argv[1]
#  print(f'>>> number of arguments: ', ansi.GB, len(sys.argv), ansi.RS, sep='', end='\n')
#  print(f'>>> current arguments: ', ansi.GB, sys.argv, ansi.RS, sep='', end='\n')
#  def decode_b64_arg(*args):
#    decarg_bytes = base64.b64decode(b64_arg)
#    return decarg_bytes.decode("utf-8")
#  print(f'>>> base64_argument.decoded: ' + ansi.GB + decode_b64_arg(sys.argv[1]) + ansi.RS, sep='', end='\n')
#else:
#  def decode_b64(n):
#    dec_b64_bytes = base64.b64decode(b64_var)
#    return dec_b64_bytes.decode("utf-8")
#  print('>>> sys.argv condition not matching, ' + ansi.RB + 'use hardcoded value!' + ansi.RS)
#  print(f'>>> base64_var.decoded: ', ansi.GB, decode_b64(b64_var), ansi.RS, sep='', end='\n')

# w/o comments
if len(sys.argv) == 2:
  if sys.argv[1] == "-h":
    # remove path from script path in sys.argv[0], expecting re works like sed -r 's,\(/\.*/\)//' 
    sys.argv[0] = re.sub(r'(/.*/)', '', sys.argv[0])
    print(sys.argv[0], ' expects base64 encoded string as argument')
  else:
    b64_arg = sys.argv[1]
    def decode_b64_arg(*args):
      b64_bytes = base64.b64decode(b64_arg)
      return b64_bytes.decode("utf-8")
    print(f"\n"'>>> base64_arg: ', ansi.GB, "\t", b64_arg, ansi.RS, "\n"'>>> base64_arg.decoded: ', ansi.GB, decode_b64_arg(sys.argv[1]), ansi.RS, sep='', end='\n')
else:
  def decode_b64(n):
    b64_bytes_dec = base64.b64decode(b64_var)
    return b64_bytes_dec.decode("utf-8")
  print(f"\n"'>>> base64_var: ', ansi.GB, "\t", b64_var, ansi.RS, "\n"'>>> base64_var.decoded: ', ansi.GB, decode_b64(b64_var), ansi.RS, sep='', end='\n')
