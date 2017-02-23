Purpose: Encode or decode base64 or base32 using a custom alphabet:

usage: custombase.py [-h] -in STRING_IN [-c CUSTOMALPHABET] [-32] [-hex]
                     [-r REPLACE] [-e] [-d]

Decode or encode base64 or base32 with an optional custom alphabet

optional arguments:
  -h, --help            show this help message and exit
  -in STRING_IN, --string_in STRING_IN
                        Encoded base64 string
  -c CUSTOMALPHABET, --customalphabet CUSTOMALPHABET
                        Specify a custom alphabet
  -32, --base32         Use base32 instead of base64
  -hex, --hexdump       Output with hexdump()
  -r REPLACE, --replace REPLACE
                        Replace padding (=/equal sign) with something
  -e, --encode          Encode string
  -d, --decode          Replace equal sign padding (=) with something

Example 1:
Pirpi custom base32:
python custombase.py -i '[extracted encoded html content here]' -c 'V1234567890oKabcdefgABCDEFGwxyzW' -32 -d -hex

Decoded Output:
[varies]

Example 2
Hwdoor custom base64 discussed by Talos (ref: hxxp://blog[.]talosintelligence[.]com/2017/02/korean-maldoc.html):

python custombase.py -i 'BKBcEcnxUKToBIBxAcToQn7IVVEQNQEFKVHVVPVJA0MfZyVchIESUgzYJQ3PK0hKYGE3w4DgiKBbYGhcZ4MmwGLkXYugA4uP' -c 'THISPROGAMCNBEUFLDJKQVWYZXviwhatrudongqyempsljkfxzbc(0546312879)' -d

Decoded output:
13379090#0#0#0#ROBUST-COMPUTER#Robust#C:\WINDOWS\system32\wscript.exe#xD