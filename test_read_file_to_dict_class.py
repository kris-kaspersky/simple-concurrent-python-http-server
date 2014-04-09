import os

file_dir = os.getcwd() + '/serverfiles/'

class Flight():
	def __init__(self, flightID):
		self.flightID = flightID
		self.schedule_info = {}

	def add_scedule_info(self, date, time, ticket):
		self.info = [time, ticket]
		self.schedule_info[date] = self.info

	def add_reservation(self, date):
		if self.schedule_info[date][1] >= 1:
			self.schedule_info[date][1] -= 1
			return 'Reserve Success'
		else:
			return 'Not Enough Tickets'

def get_flights(filename):
	file_in = open(file_dir + filename)
	flights = {}
	for line in file_in:
		line = line.strip('\n')
		line_list = line.split(',')
		if not line_list[0] in flights:
			flights[line_list[0]] = Flight(line_list[0])
			flights[line_list[0]].add_scedule_info(line_list[1], line_list[2], 30)
		else:
			flights[line_list[0]].add_scedule_info(line_list[1], line_list[2], 30)
	return flights

if __name__ == '__main__':
	filename = 'flights.csv'
	flights = get_flights(filename)
	print flights['UA002'].add_reservation('Mon')
	print flights['UA002'].add_reservation('Mon')
	print flights['UA002'].schedule_info['Mon']
	for key in flights.keys():
		print key + " " + str(flights[key].schedule_info)