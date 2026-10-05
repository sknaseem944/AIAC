import string


def is_anagram(str1, str2):
	"""Return True when two strings are anagrams, ignoring case and punctuation."""
	normalize = lambda value: sorted(
		char.casefold() for char in value if char not in string.whitespace and char not in string.punctuation
	)
	return normalize(str1) == normalize(str2)


# AI-generated test cases
assert is_anagram("listen", "silent") is True
assert is_anagram("hello", "world") is False
assert is_anagram("Dormitory", "Dirty Room") is True
assert is_anagram("", "") is True
assert is_anagram("A gentleman!", "Elegant man") is True

print("All anagram tests passed.")
