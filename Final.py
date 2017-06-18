import re #Imports the "Regular Expressions (regex)" library to this file.

#This script converts verilog files into benchmarks for the SAT Solver software.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Setup~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

V_file = open("c880.v", "r") # Add the name of the ".v" file, which has to be converted.
line = ''.join(V_file)
x = re.sub('module (.*?);','',line) # regex to remove the "module" part from the .v file.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Key~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

pattern = re.compile('# key=(.*?)[0-9]+',re.S) # regex to search for the
n = pattern.search(x)						   # "key" in the .v file.

if n is None:
	None
else:
	print(n[0])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Input~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

pattern = re.compile('(input|Input)(.*?);',re.S) # regex to search for the
n = pattern.search(x)							 # "Input" part in the .v file.

l = n[2]
p = n[0]

if "keyinput" in l:
	pattern = re.compile('[0-9]+',re.S) # regex to search for the input
	m = pattern.findall(l)				# gates in the .v file.
	
	key = re.compile('keyinput[0-9]+',re.S) # regex to search for the term
	j = key.findall(l)						# "keyinput" in the .v file.
	v = len(j)
	m = m[:-v]
		
	for h in m:
		d = ("INPUT" + "(" + "G" + h + ")")
		print (d) # Prints the "INPUT" lines in the benchmark.
	
else:
	l = n[2]

	pattern = re.compile('[0-9]+',re.S) # regex to search for the input
	m = pattern.findall(l)				# gates in the .v file.

	for h in m:
		d = ("INPUT" + "(" + "G" + h + ")")
		print (d) # Prints the "INPUT" lines in the benchmark.


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~keyinput~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	

pattern = re.compile('(keyinput|Keyinput)(.*?);',re.S) # regex to search for the
n = pattern.search(x)								   # "keyinput" part in the .v file.

if n is None:
	None
else:
	l = n[2]
	pattern = re.compile('[0-9]+',re.S) # regex to search for the input
	m = pattern.findall(l)				# gates in the .v file.
		
	for h in m:
		d = ("INPUT" + "(" + "keyinput" + h + ")")
		print (d) # Prints the "INPUT" lines in the benchmark.

print("\n")
	

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Output~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


pattern = re.compile('(output|Output)(.*?);',re.S) # regex to search for the
n = pattern.search(x)							   # "Output" part in the .v file.

l = n[2]

pattern = re.compile('[0-9]+',re.S) # regex to search for the output
m = pattern.findall(l)				# gates in the .v file.

for h in m:
	d = ("OUTPUT" + "(" + "G" + h + ")")
	print (d) # Prints the "OUTPUT" lines in the benchmark.


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Gates~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	

pattern = re.compile(' (.*)\((.*)\);') # regex to search for the inputs
j = pattern.findall(x)				   # & outputs of each gate in the design.

#print(j)

print ("\n")

i = 0
for a in j: # Loop manipulates the above regex output list to print the gate in\out's in the bench file.
	sub = j[i]
	k = sub[0]
	sub_n = k.lower()

	if "not" in sub_n:
		sub_name = "not"
	if "or" in sub_n:
		sub_name = "or"
	if "and" in sub_n:
		sub_name = "and"
	if "nor" in sub_n:
		sub_name = "nor"
	if "nand" in sub_n:
		sub_name = "nand"
	if "xor" in sub_n:
		sub_name = "xor"
	if "xnor" in sub_n:
		sub_name = "xnor"
	if "buf" in sub_n:
		sub_name = "buf"
	if "mux" in sub_n:
		sub_name = "mux"
	
	sub_gate = sub[1]

	pat = re.compile('(.*?),(.*)',re.S)
	w = pat.findall(sub_gate)
	x = list(w)
	e = w[0][0]
	d = w[0][1]
	s = (e, "=", sub_name + "(" + d + ")")
	print (s[0],s[1],s[2])	
	
	i += 1


#	if 'keyinput' in sub_gate:
#		pat = re.compile('(.*?),(.*)',re.S)
#		w = pat.findall(sub_gate)
#		x = list(w)
#		e = w[0][0]
#		d = w[0][1]
#		c = (e, "=", sub_name + "(" + d + ")")
#		print (c[0],c[1],c[2])


#	if 'E' in sub_gate:

		

#	else:
#		pat = re.compile('(.*?),(.*)',re.S)
#		w = pat.findall(sub_gate)
#		x = list(w)
#		e = w[0][0]
#		d = w[0][1]
#		c = (e, "=", sub_name + "(" + d + ")")
#		print (c[0],c[1],c[2])

	
