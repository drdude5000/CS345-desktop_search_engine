# CS345-desktop_search_engine

Token Bugs<br><br>
1) Step2.txt should not include any reference to non-text files and directory<br>
			14 DIR 1 0<br>
			14 1 2 0	# These are garbage<br>
			14 TXTN 7 0<br>
			14 3 8 0	# More garbage<br><br>

2) No case-folding and no proper string checking<br>
			15 M9re 5 0 <br><br>

3) Offsets start with 1 and not 0 <br>
			(5,algorithms,1,0)
