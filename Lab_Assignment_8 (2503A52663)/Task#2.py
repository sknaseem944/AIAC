def classify_number(n):
	"""Classify a numeric value as Positive, Negative, or Zero."""
	if not isinstance(n, (int, float)) or isinstance(n, bool):
		raise TypeError("n must be a number")

	if n > 0:
		return "Positive"
	if n < 0:
		return "Negative"
	return "Zero"


# Boundary and representative test cases generated for the classification logic.
test_cases = [
	(10, "Positive"),
	(-5, "Negative"),
	(0, "Zero"),
	(1, "Positive"),
	(-1, "Negative"),
]

for number, expected in test_cases:
	assert classify_number(number) == expected

for invalid_value in ("10", None):
	try:
		classify_number(invalid_value)
	except TypeError:
		pass
	else:
		raise AssertionError("Invalid input should raise TypeError")

print("All classification tests passed.")