import csv

def sort():

	cities = set(['ATL', 'LAX', 'ORD', 'DFW', 'JFK', 'DEN', 'SFO', 'CLT', 'LAS', 'PHX',
				  'MIA', 'IAH', 'SEA', 'MCO', 'EWR', 'MSP', 'BOS', 'DTW', 'PHL', 'LGA',
				   'FLL', 'BWI', 'DCA', 'MDW', 'SLC', 'IAD', 'SAN', 'HNL','TPA', 'PDX'])
	

	new = open('new.csv', 'w')
	with open('ontime.csv') as original:
		fieldnames = ["QUARTER","FL_DATE","UNIQUE_CARRIER","TAIL_NUM","ORIGIN","DEST","DEP_TIME","DEP_DELAY","ARR_TIME","ARR_DELAY","CANCELLED","ACTUAL_ELAPSED_TIME", ""]
		reader = csv.DictReader(original)
		writer = csv.DictWriter(new, fieldnames)
		writer.writeheader()
		for row in reader:
			if row['ORIGIN'] in cities and row['DEST'] in cities:
				writer.writerow(row)
def average():

	flights = {}

	new = open('averaged.csv', 'w')
	with open('new.csv') as filtered:
		fieldnames = ["QUARTER", "CARRIER", "ORIGIN", "DEST", "DEP_DELAY", "ARR_DELAY", "FLIGHT_TIME", "CANCELLED"]
		writer = csv.DictWriter(new, fieldnames)
		writer.writeheader()

		reader = csv.DictReader(filtered)

		for row in reader:

			if (row['CANCELLED'] != '1.00' and row["DEP_DELAY"] != "" and row["ARR_DELAY"] != "" and row["ACTUAL_ELAPSED_TIME"] != ""):
				flights.setdefault((row['ORIGIN'], row['DEST'], row["UNIQUE_CARRIER"], row["QUARTER"]), [])
				flights[(row['ORIGIN'], row['DEST'], row["UNIQUE_CARRIER"], row["QUARTER"])] += [row]

			elif row['CANCELLED'] == '1.00' :
				flights.setdefault((row['ORIGIN'], row['DEST'], row["UNIQUE_CARRIER"], row["QUARTER"]), [])
				flights[(row['ORIGIN'], row['DEST'], row["UNIQUE_CARRIER"], row["QUARTER"])] += [row]

	count = 0
	for name, data in flights.iteritems():
		avg_cancelled = 0
		avg_d_delay = 0
		avg_a_delay = 0
		avg_time = 0

		for d in data:
			if d['CANCELLED'] == '1.00':
				avg_cancelled += float(d["CANCELLED"])
			else:
				avg_d_delay += float(d["DEP_DELAY"])
				avg_a_delay += float(d["ARR_DELAY"])
				avg_time += float(d["ACTUAL_ELAPSED_TIME"])

		try:

			avg_d_delay /= (len(data) - avg_cancelled)
			avg_a_delay /= (len(data) - avg_cancelled)
			avg_time /= (len(data) - avg_cancelled)
			avg_cancelled /= len(data)

		except ZeroDivisionError:
			continue


		avg_d_delay = round(avg_d_delay, 3)
		avg_a_delay = round(avg_a_delay, 3)
		avg_time = round(avg_time, 3)
		avg_cancelled = round(avg_cancelled, 3)

		count += 1
		print("{}/{} Processed!". format(count, len(flights)))

		new_row = {"QUARTER": name[3], "CARRIER": name[2],
		 "ORIGIN": name[0] , "DEST": name[1],"DEP_DELAY": avg_d_delay , "ARR_DELAY": avg_a_delay,
		  "FLIGHT_TIME": avg_time, "CANCELLED": avg_cancelled}
		writer.writerow(new_row)


