Bug:
	Acessing the dictionary A is dont incorrectly: A['a']
	A['A'] should have been the correct way to access the data
	In such a case a blank file or simple computation such as
		"1+1" should print 2 but the sandbox fails to do so.
		Refer to the input file: a