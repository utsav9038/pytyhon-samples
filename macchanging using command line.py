import subprocess
import optparse

def macchangingar():
	parser=optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Enter the interface whose mac id to be changed")
	parser.add_option("-m", "--macid", dest="newmac", help="Enter the interface whose mac id to be changed")
	(options,argements)=parser.parse_args()
	if not options.interface:
		parser.error("enter the interface or choose for help")
	elif not options.newmac:
		parser.error("enter the mac or choose for help")
	return options

def macchangingfxn(interface,macid):
	subprocess.call(["sudo", "ifconfig", interface, "down"])
	subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", macid])
	subprocess.call(["sudo", "ifconfig", interface, "up"])

opt=macchangingar()
macchangingfxn(opt.interface,opt.newmac)