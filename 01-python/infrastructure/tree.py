def draw_tree(size,shape='nora'):
	VALID = ['nora','lynn']
	if shape not in VALID:
		raise ValueError('shape is undefiend')
	
	if shape == 'nora':
    		for i in range(size):
		    print("n" * i)
		    print()
  		print("||")

    		return    
	

		 

	else:
	   for j in range(size):
		print("l" * j)
		print()
	   print("||")

 		return







