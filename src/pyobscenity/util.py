def compare_intervals(lower_bound_0: int, upper_bound_0: int, lower_bound_1: int, upper_bound_1: int) -> int:
	if lower_bound_0 < lower_bound_1:
		return -1
	if lower_bound_1 < lower_bound_0:
		return 1
	if upper_bound_0 < upper_bound_1:
		return -1
	if upper_bound_1 < upper_bound_0:
		return 1
	return 0

reg_exp_special_chars = list(map(lambda c: c.encode('utf-8'), ['[', '.', '*', '+', '?', '^', '$', '{', '}', '(', ')', '|', '[', '\\', ']']))