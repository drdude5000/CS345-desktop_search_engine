# CS345-desktop_search_engine

Token Bugs
1) Step2.txt should not include any reference to non-text files and directory
			14 DIR 1 0
			14 1 2 0	# These are garbage
			14 TXTN 7 0
			14 3 8 0	# More garbage

2) No case-folding and no proper string checking
			15 M9re 5 0 

3) Offsets start with 1 and not 0 
			(5,algorithms,1,0)
