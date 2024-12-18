"""
File: validEmailAddress.py
Name: 
----------------------------
This file shows what a feature vector is
and what a weight vector is for valid email 
address classifier. You will use a given 
weight vector to classify what is the percentage
of correct classification.

Accuracy of this model: 65.384615384615387%
"""

WEIGHT = [                           # The weight vector selected by Jerry
	[0.4],                           # (see assignment handout for more details)
	[0.4],
	[0.2],
	[0.2],
	[0.9],
	[-0.65],
	[0.1],
	[0.1],
	[0.1],
	[-0.7]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	i = 0
	correct_classification_count = 0
	for maybe_email in maybe_email_list:
		feature_vector = feature_extractor(maybe_email)
		score = sum(WEIGHT[i][0] for i in range(len(feature_vector)) if feature_vector[i] == 1)
		print(f"Email: {maybe_email} | Score: {score:.2f} | Classified as: {'Valid' if score > 0 else 'Invalid'}")

		if (i < 13 and score < 0) or (i >= 13 and score > 0):
			correct_classification_count += 1
		i += 1

	accuracy = correct_classification_count / len(maybe_email_list) * 100
	print(f"Accuracy of this model: {accuracy:.15f}%")


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with 10 values of 0's or 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i] = 1 if '@' in maybe_email else 0
		elif i == 1:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' not in maybe_email.split('@')[0] else 0
		elif i == 2:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@')[0] != "" else 0
		elif i == 3:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@')[-1] != "" else 0
		elif i == 4:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' in maybe_email.split('@')[-1] else 0
		elif i == 5:
			feature_vector[i] = 1 if ' ' not in maybe_email else 0
		elif i == 6:
			feature_vector[i] = 1 if maybe_email.endswith('.com') else 0
		elif i == 7:
			feature_vector[i] = 1 if maybe_email.endswith('.tw') else 0
		elif i == 8:
			feature_vector[i] = 1 if maybe_email.endswith('.edu') else 0
		elif i == 9:
			feature_vector[i] = 1 if len(maybe_email) > 10 else 0
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that might be valid email addresses
	"""
	with open(DATA_FILE, 'r') as file:
		return [line.strip() for line in file]


if __name__ == '__main__':
	main()
