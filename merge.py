import os
def merge():
	with open('ontime.csv', 'w') as f:
		f.write("""
			"QUARTER","FL_DATE","UNIQUE_CARRIER","TAIL_NUM","ORIGIN","DEST","DEP_TIME","DEP_DELAY","ARR_TIME","ARR_DELAY","CANCELLED","ACTUAL_ELAPSED_TIME",
			""")
		for name in os.listdir('ontime/'):
			with open('ontime/' + name) as file:
				for line in file:
					if not ("QUARTER" in line):
						f.write(line);