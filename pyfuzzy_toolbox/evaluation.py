def precision(TP, FP):
	return (TP / (TP + FP)) if (TP + FP) > 0 else 0


def recall(TP, FN):
	return (TP / (TP + FN)) if (TP + FN) > 0 else 0


def f1(TP, FP, TN, FN):
	return ((2 * (((TP / (TP + FP)) * (TP / (TP + FN))) / ((TP / (TP + FP)) + (TP / (TP + FN)))))) if (TP + FP) > 0 and (TP + FN) > 0 else 0


def accuracy(TP, FP, TN, FN):
	return ((TP + TN) / (TP + TN + FP + FN)) if (TP + TN + FP + FN) > 0 else 0

def tpr(TP, FN):
	return (TP / (TP + FN)) if (TP + FN) > 0 else 0

def tnr(TN, FP):
	return (TN / (TN + FP)) if (TN + FP) > 0 else 0	
