"""Convert hex to base64.
"""

import base64


HEX_STRING = ('49276d206b696c6c696e6720796f757220627261696e206c'
              '696b65206120706f69736f6e6f7573206d757368726f6f6d')

raw_bytes = bytearray.fromhex(HEX_STRING)

print(base64.b64encode(raw_bytes).decode() ==
      'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
