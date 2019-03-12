

#/bin/sh shellcode strings
bin_sh_25 = "\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x31\xc0\x99\x31\xf6\x54\x5f\xb0\x3b\x0f\x05"

'''
0xff
|++++++++++++++|
|   \t         |
|   arg3       | <--- 0x00ff332200
|++++++++++++++| 
|   eip        | <--- 0x00ff332200+4
|++++++++++++++|
|   ebp        | <--- 0x00ff332200+4
|
0x00
'''


released = {
		"iphone" : 2007,
		"iphone 3G" : 2008,
		"iphone 3GS" : 2009,
		"iphone 4" : 2010,
		"iphone 4S" : 2011,
		"iphone 5" : 2012
	}
#test dictionary
testdict = {
        "arg3":"0x00ff332200",
        "EIP":"0x00ff332204",
        "ebp":"0x00ff332208",
        "trashend":"0x00ff33220B",
        "trashstart":"0x00ff332200",
        "int":"0x00ff332200"
    }

#YO WTF DICTIONARIES DONT OUTPUT IN CORRECT ORDER
def print_output(address_list):
    print("STACK")
    print("|" + "+"*27 + "|")
    for name,address in address_list.items():
        print("|" + " "*27 + "|")
        print("|\t" + name + " "*(20-len(name)) + "|" + "<---" + address)
        print("|" + " "*27 + "|")
        print("|" + "+"*27 + "|")

print_output(testdict)

        