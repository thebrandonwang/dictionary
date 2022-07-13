def read_file(filename, lists):
	with open(filename, 'r') as f:
		for line in f:
			lists.append(line.strip())
	return lists
def count(lists):
	wc = {} # word_count
	for line in lists:
		words = line.split()
		for word in words:
			if word not in wc:
				wc[word] = 1
			else:
				wc[word] += 1
	for w in wc:
		if wc[w] > 1000000:
			print(w, 'has appeared', wc[w], 'times')
	return wc

def search_word(wc):
	while True:
		word = input('please enter the word you are looking for: ')
		if word == 'q':
			break
		if word in wc:
			print(word, 'has appeared', wc[word], 'times')
		elif word not in wc:
			print('there is no such word in the reviews.')
def main():
	start_time = time.time()
	lists = []
	lists =  read_file('reviews.txt', lists)
	wc = count(lists)
	end_time = time.time()
	print('Total time spent: ', end_time - start_time, 'seconds')
	search_word(wc)


import time
main()