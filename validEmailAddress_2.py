"""
File: validEmailAddress_2.py
Name: 
----------------------------
Please construct your own feature vectors
and try to surpass the accuracy achieved by
Jerry's feature vector in validEmailAddress.py.
feature1: There is '@' in the string
feature2: There is '.' in the string
feature3: Some strings before '@'
feature4: Some strings after '@'
feature5: No invalid combinations ('..', '.@', '@.', '-@', '@-', ' ')
feature6: No invalid chars (()<>[]:;,\)
feature7: Do not start with '.' or '-'
feature8: Do not end with '.' or '-'
feature9: Only one '@'
feature10: Strings' length before '@' <= 64
feature11: Strings' length after '@' <= 253
feature28: Quoted strings before '@' (if any) properly enclosed


Accuracy of your model: 88.461538461538453%
"""

import numpy as np

WEIGHT = np.array([
					[1], 		# The weight vector selected by you
					[1], 		# (Please fill in your own weights)
					[1],
					[1],
					[1],
					[1],
					[1],
					[1],
					[1],
					[1],
					[1],
					[1],
])

DATA_FILE = 'is_valid_email2.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	i = 0
	correct_classification_count = 0
	for maybe_email in maybe_email_list:
		feature_vector = feature_extractor(maybe_email)
		score = WEIGHT.T.dot(feature_vector)[0]
		print(f"Email: {maybe_email} | Score: {score:.2f} | Classified as: {'Valid' if score == 12 else 'Invalid'}")

		if (i < 13 and score != 12) or (i >= 13 and score == 12):
			correct_classification_count += 1
		i += 1

	accuracy = correct_classification_count / len(maybe_email_list) * 100
	print(f"Accuracy of this model: {accuracy:.15f}%")


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with value 0's and 1's
	"""
	feature_vector = np.zeros(len(WEIGHT))

	feature_vector[0] = 1 if '@' in maybe_email else 0
	feature_vector[1] = 1 if '.' in maybe_email else 0
	if feature_vector[0]:
		feature_vector[2] = 1 if maybe_email.split('@')[0] != "" else 0
	if feature_vector[0]:
		feature_vector[3] = 1 if maybe_email.split('@')[-1] != "" else 0
	feature_vector[4] = 1 if not contains_invalid_combination(maybe_email) else 0
	feature_vector[5] = 1 if not contains_invalid_chars(maybe_email) else 0
	feature_vector[6] = 1 if not (maybe_email.startswith('.') or maybe_email.startswith('-')) else 0
	feature_vector[7] = 1 if not (maybe_email.endswith('.') or maybe_email.endswith('-')) else 0
	feature_vector[8] = 1 if maybe_email.count('@') == 1 else 0
	if feature_vector[0]:
		feature_vector[9] = 1 if len(maybe_email.split('@')[0]) <= 64 else 0
	if feature_vector[0]:
		feature_vector[10] = 1 if len(maybe_email.split('@')[-1]) <= 253 else 0
	feature_vector[11] = 1 if '"' not in maybe_email.split('@')[0] \
		or (maybe_email.split('@')[0].startswith('"') and maybe_email.split('@')[0].endswith('"')) else 0

	return feature_vector


def contains_invalid_combination(string):
	"""
	Checks if the input string contains any invalid combinations
	that are not allowed in an email address.
	"""
	invalid_combination = ['..', '.@', '@.', '-@', '@-', ' ']
	for combination in invalid_combination:
		if combination in string:
			return True
	return False


def contains_invalid_chars(string):
	"""
	Checks if the input string contains any invalid chars
	that are not allowed in an email address.
	"""
	invalid_chars = '()<>[]:;,\\'
	for char in invalid_chars:
		if char in string:
			return True
	return False


def read_in_data():
	"""
	:return: list, containing strings that might be valid email addresses
	"""
	with open(DATA_FILE, 'r') as file:
		return [line.strip() for line in file]


if __name__ == '__main__':
	main()
