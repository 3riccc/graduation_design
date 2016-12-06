#encoding:utf
for ascii in range(0,126):
	if(ascii>31 and ascii<48 or ascii>57 and ascii<65 or ascii>90 and ascii < 95 or ascii>95 and ascii<97 or ascii>122):
		print chr(ascii)
		print ascii