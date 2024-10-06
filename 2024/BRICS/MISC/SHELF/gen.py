import base64


# The shell script
script = '#!/bin/sh\ncat /flag.txt\n'

# Encode to bytes
script_bytes = script.encode('utf-8')

# Base64 encode
b64_script = base64.b64encode(script_bytes).decode('utf-8')

print(b64_script)
