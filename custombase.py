import base64
import argparse

from sys import exit
from hexdump import hexdump #not needed if you dont want to use hexdump flag
from string import maketrans

def decode_base(encoded,alphabet,standard_base,base32):
	encoded = encoded.translate(maketrans(alphabet, standard_base))
	if base32:
		decoded = base64.b32decode(encoded)
	else:
		decoded = base64.b64decode(encoded)
	return decoded

def encode_base(string_to_encode,alphabet,standard_base,base32):
	if base32:
		encoded = base64.b32encode(string_to_encode)
	else:
		encoded = base64.b64encode(string_to_encode)
	return encoded.translate(maketrans(standard_base, alphabet))


def main():
	parser = argparse.ArgumentParser(description='Decode or encode base64 or base32 with an optional custom alphabet')
	parser.add_argument('-in','--string_in',help='Input string that needs to be encoded/decoded',required=False)
	parser.add_argument('-f','--file_in',help='Input filename that needs to be encoded/decoded',required=False)
	parser.add_argument('-c','--customalphabet',help='Specify a custom alphabet',required=False)
	parser.add_argument('-32','--base32',help='Use base32 instead of base64',action='store_true',required=False)
	parser.add_argument('-hex','--hexdump',help='Output with hexdump()',action='store_true',required=False)
	parser.add_argument('-r','--replace',help='Replace padding (=/equal sign) with something',required=False)
	parser.add_argument('-e','--encode',help='Encode string',action='store_true',required=False)
	parser.add_argument('-d','--decode',help='Replace equal sign padding (=) with something',action='store_true',required=False)

	args = parser.parse_args()

	string_in = args.string_in
	file_in = args.file_in
	dohexdump = args.hexdump
	base32 = args.base32

	encode = args.encode
	decode = args.decode


	if not string_in and not file_in:
		print 'You should provide at least an input string or a filename...exiting'
		exit()
	if not encode and not decode:
		print 'Need to use encode or decode flag, exiting...'
		exit()
	elif encode and decode:
		print 'You should not try to decode and encode at the same time, exiting...'
		exit()
	elif string_in and file_in:
		print 'You should provide only a filename or an input string, not both, exiting...'
		exit()
  

	if base32:
		standard_base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567' #standard base32 alphabet
	else:
		standard_base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/' #standard base64 alphabet


	if args.customalphabet:
		alphabet = args.customalphabet
		if len(alphabet) != len(standard_base):
			print 'Custom alphabet must be same length as standard alphabet, exiting...'
			exit()
	else:
		alphabet = standard_base

	#replace provided character with = for padding
	if args.replace:
		replace_char = args.replace
		print 'replace char is: %s' % replace_char
	else:
		replace_char = None

	if file_in:
		with open(file_in, 'rb') as myfile:
			string_in=myfile.read()

	if decode:
		#replace padding char if needed
		if replace_char:
			string_in = string_in.replace(replace_char,'=')
		decoded = decode_base(string_in,alphabet,standard_base,base32)
		print 'Decoded output:'
		if dohexdump:
			hexdump(decoded)
		else:
			print decoded
	elif encode:
		encoded = encode_base(string_in,alphabet,standard_base,base32)
		if replace_char:
			encoded = encoded.replace('=',replace_char)
		print 'Encoded output:'
		if dohexdump:
			hexdump(encoded)
		else:
			print encoded


if __name__ == '__main__':
    main()
