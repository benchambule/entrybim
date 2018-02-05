class MatrixProcessor:
	def __init__(self, matrix):
		self.matrix = matrix
		self.processedObjects = 0
		self.nrtwins = 0

	def process_1(self, matrix = None):
		if matrix:
			self.matrix = matrix

		array = self.matrix[:]
		self.processedObjects = 0

		for line, verticalArray in enumerate(array):
			for column, value in enumerate(verticalArray):
				if column + 2 < len(verticalArray):
					if value == verticalArray[column + 1] == verticalArray[column + 2] and value != 0:
						array[line][column] = array[line][column + 1] = array[line][column + 2] = 0
						self.processedObjects += 1

		self.processedMatrix = array[:]
		return array

	def process(self, matrix = None):
		if matrix:
			self.matrix = matrix

		array = self.matrix[:]
		self.processedObjects = 0
		self.nrtwins = 0

		for line, verticalArray in enumerate(array):
			x = self.process_vector(verticalArray)
			array[line] = x
			self.processedObjects += self.nrtwins
		
		return array

	def nr_twins(self, column, vector):
		nrtwins = 0
		for i in range(column+1, len(vector)):
			if vector[column] == vector[i] and vector[column] != 0:
				nrtwins += 1
			else:
				break

		return nrtwins

	def process_vector(self, vector):
		for column, value in enumerate(vector):
			x = self.nr_twins(column, vector)
			if x:
				vector[column:column + x + 1] = [0 for i in range(column, column + x + 1)]

			self.nrtwins += x

		return vector

	def getMatrix(self):
		return self.matrix

	def getProcessedMatrix(self):
		return self.processedMatrix

	def getNumOfProcessedObjects(self):
		return self.processedObjects

class MatrixViewer:
	def __init__(self, matrix):
		self.matrix = matrix
		self.linesViewed = 0

	def view(self, text="", matrix = None):
		if matrix:
			self.matrix = matrix

		if text != "":
			print text

		self.linesViewed = 0
		for x in self.matrix:
			self.linesViewed += 1
			print x

	def getLinesViewed(self):
		return self.linesViewed

class MatrixCleaner:
	def __init__(self, matrix):
		self.matrix = matrix
		self.cleanedObjects = 0

	def clean(self, matrix = None):
		if matrix:
			self.matrix = matrix

		array = matrix[:]
		self.cleanedObjects = 0

		for line, verticalArray in enumerate(array):
			for column, value in enumerate(verticalArray):
				if column + 1 < len(verticalArray) and array[line][column + 1] == 0 and value != 0:
					array[line][column + 1] = array[line][column]
					array[line][column] = 0
					self.cleanedObjects += 1

		self.cleanedMatrix = array[:]
		return array

	def getMatrix(self):
		return self.matrix

	def getCleanedMatrix(self):
		return self.cleanedMatrix

	def getNumOfCleanedObjects(self):
		return self.cleanedObjects



class MatrixTransposer:
	def __init__(self, matrix):
		self.matrix = matrix

	def transpose(self, matrix = None):
		if matrix:
			self.matrix = matrix

		self.transposedMatrix = [list(x) for x in zip(*self.matrix)]

		return self.transposedMatrix

	def getMatrix(self):
		return self.matrix

	def getTransposedMatrix(self):
		return self.transposedMatrix


def main():
	array = [
		[1, 2, 2, 1],
		[2, 2, 2, 1],
		[1, 4, 5, 7],
		[1, 2, 5, 7],
	]

	viewer = MatrixViewer(array)
	viewer.view("+++++++++++++++++++++++++++\n\tInitial Matrix\n+++++++++++++++++++++++++++\n")

	transposer = MatrixTransposer(array)
	processor = MatrixProcessor(array)
	cleaner = MatrixCleaner(array)

	iterations = 0
	while True:

		if processor.getNumOfProcessedObjects() == 0 and cleaner.getNumOfCleanedObjects() == 0 and iterations >= 1:
			break

		array = processor.process(array)
		array = transposer.transpose(array)
		#array = processor.process(array)
		array = cleaner.clean(array)
		array = processor.process(array)
		array = transposer.transpose(array)

		viewer.view("+ iteration " + str(iterations), array)

		iterations += 1

	viewer.view("+++++++++++++++++++++++++++\n\tResulting Matrix\n+++++++++++++++++++++++++++\n", array)

if __name__ == '__main__':
	main()
