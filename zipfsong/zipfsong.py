import sys

class PlayList:
	def __init__(self):
		self.list = []
		self.n = None
		self.m = None
		self.min = None
		self.min_idx = None
	
	def generate(self):
		line = sys.stdin.readline().strip().split()
		self.n = int(line[0])
		self.m = int(line[1])
		k = 1
		for line in sys.stdin:
			record = line.strip().split()
			plays = int(record[0])
			title = str(record[1])
			self.list.append((k,plays,title))
			k+=1
			
	def sortList(self):
		self.list.sort(key = lambda item: (item[0]*item[1], -item[0]),reverse=True)

	def write(self):
		for item in self.list[0:self.m]:
			print item[2]

def main():
	pl = PlayList()
	pl.generate()
	pl.sortList()
	pl.write()

if __name__ == '__main__':
	main()
	