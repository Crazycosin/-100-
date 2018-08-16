def sort_min(input_list,k):
	input_list.sort(reverse = False)
	return input_list[:k]
if __name__ == '__main__':
	input_list = [1,4,2,6]
	print(sort_min(input_list,2))