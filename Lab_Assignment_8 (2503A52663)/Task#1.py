def is_strong_password(password):
	"""Return True when password meets all strength requirements."""
	return (
		len(password) >= 8
		and " " not in password
		and any(character.isupper() for character in password)
		and any(character.islower() for character in password)
		and any(character.isdigit() for character in password)
		and any(not character.isalnum() for character in password)
	)
#test cases
print(is_strong_password("Password123!"))  # True
print(is_strong_password("password123!"))  # False
print(is_strong_password("Password123"))   # False
print(is_strong_password("Password!"))     # False