import os
import sys

if len(sys.argv) == 2:
	os.system("VBoxManage snapshot '%s' take '%s' --pause" % (sys.argv[1], sys.argv[1]+"-base"))
	os.system("VBoxManage controlvm '%s' poweroff" % sys.argv[1])		
	os.system("VBoxManage snapshot '%s' restorecurrent" % sys.argv[1])