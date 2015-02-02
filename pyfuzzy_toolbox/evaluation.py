def precision(TP, FP):
	return TP / (TP + FP)


def recall(TP, FN):
	return TP / (TP + FN)


def f1(TP, FP, TN, FN):
	return (2 * (((TP / (TP + FP)) * (TP / (TP + FN))) / ((TP / (TP + FP)) + (TP / (TP + FN)))))


def accuracy(TP, FP, TN, FN):
	return (TP + TN) / (TP + TN + FP + FN)
