'''
第10题（字符串）
翻转句子中单词的顺序。
题目：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。

句子中单词以空格符隔开。为简单起见，标点符号和普通字母一样处理。
例如输入“I am a student.”，则输出“student. a am I”。

'''
def ReverseWords(sentence_str):
	sentence_list = sentence_str.split(' ')
	words = sentence_list[::-1]
	words_str = '.'.join(words)
	return words_str
if __name__ == '__main__':
	sentence_str = 'I am a student.'
	print(ReverseWords(sentence_str))