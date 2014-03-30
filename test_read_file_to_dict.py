import os

file_dir = os.getcwd() + '/serverfiles/'

def get_flights(filename):
	file_in = open(file_dir + filename)
	flights = {}
	flight_day = []
	flight_time = []
	flight_name = []
	for line in file_in:
		line = line.strip('\n')
		line_list = line.split(',')
		flight_name.append(line_list[0])
		flight_day.append(line_list[1])
		flight_time.append(line_list[2])
	for i in range(0, len(flight_name)):
		flights[flight_name[i]] = {}
	for i in range(0, len(flight_name)):
		flights[flight_name[i]][flight_day[i]] = flight_time[i]
	return flights

if __name__ == '__main__':
	filename = 'flights.csv'
	flights = get_flights(filename)
	print flights['UA005']['Mon']
