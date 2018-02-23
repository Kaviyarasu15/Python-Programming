while True:
aa = input("Enter any character: ")
if aa == '0':
	break
else:
if((aa>='a' and aa<='z') or (aa>='A' and aa<='Z')):
	print(aa, "is an alphabet.\n")
else:
	print(aa, "is not an alphabet.\n")
