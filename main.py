import math
from os import listdir
from os.path import isfile, join

class KNN():
	"this is to demonstrate the use of KNN"
	def __init__(self):
		print("""
___________________________________________

			KNN - CSC 323 
			Rapando C Samson
			Kirega Joseph
			Adrian Wanderi
___________________________________________

		""")
		
		self.data, self.sample, self.states = [],[], []
		self.no_samples, self.attributes, self.high_state, self.low_state =  0, 0, 0, 0


		self.folder = "files/"

		print("LIST OF FILES AVAILABLE\n")
		
		self.files = [f for f in listdir(self.folder) if isfile(join(self.folder, f))]
		x = 1
		for f in self.files:
			print(x, f)
			x += 1
		print()

		self.load_data()
		

	def load_data(self):
		chosen = int(input("Choose the data file to load : ", ))
		chosen_file = self.files[chosen - 1]
		print("You have chosen ", chosen_file, "...\n")

		#load the data to the self.data variable
		with open(self.folder + chosen_file, "r") as f:
			for line in f:
				sample = line.strip('\r\n').split(' ')
				one_sample = []
				for x in sample:
					try:
						one_sample.append(float(x))
					except:
						one_sample.append(x)
				self.data.append(one_sample)

		print("The data has been loaded...")

		if len(self.data[-1]) == 1:
			del self.data[-1]

		for sample in self.data:
			sample[-1] = int(sample[-1])
			self.states.append(sample[-1])

		self.no_samples = len(self.data)
		self.attributes = len(self.data[-1]) - 1
		self.high_state = max(self.states)
		self.low_state = min(self.states)

		print("The data has ",self.no_samples, "samples and has ", self.attributes, " attributes.")
		print("The Low State is ", self.low_state, " and the high state is ",self.high_state)

		print("___________________________________________")


	def validate_data(self):
		"Returns True if the number of columns is same in all rows and False otherwise"
		attributes = self.attributes
		data = self.data
		no_samples = self.no_samples

		valid_data = True
		for i in self.data:
			if len(i) != attributes + 1:
				valid_data = False
				break
		return valid_data
		

	def load_sample(self):

		for i in range(self.attributes):
			print("Enter Attribute ", i+1, ": ")
			x = input()
			self.sample.append(float(x))

		print()

	def get_differences(self):
		for item in self.data:
			total_differences = 0.0
			for i in range(self.attributes):
				total_differences += (item[i] - self.sample[i])**2
			item.append(total_differences)
			
		self.data.sort(key=lambda x:x[-1])

		print("The Differences have been calculated and the data sorted\n")

	def cluster(self):
		length = len(self.data)
		if length % 2 == 0:
			no = int(length / 2) + 1
		else:
			y = int(length / 2)
			if y % 2 == 0:
				no = y + 1
			else:
				no = y

		print("Using the first ", no, " elements to cluster")

		total = 0
		for i in range(no):
			total += self.data[i][-2]

		required_half = float (self.high_state * no) / float(2)
		print("the total is ", total, " and the required half is ", required_half)

		if total < required_half:
			print("The state of the sample is ", self.low_state)
		else:
			print("The state of the sample is ", self.high_state)
		




	
knn = KNN()
if knn.validate_data():
	print("\nThe data is valid. Continue\n")
	knn.load_sample()
	knn.get_differences()
	knn.cluster()

else:
	print("\nThe data has an error, exiting...\n")

print("___________________________________________")
