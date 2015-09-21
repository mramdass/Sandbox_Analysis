Bug:
	Syntax error was found when checking the type of file passed in.
	Refer to the following lines of code:

try:
	if !sys.argv[1].endswith(".py"):
		print "Sandbox only supports .py files"
		exit(1)

"!" is incorrectly used.