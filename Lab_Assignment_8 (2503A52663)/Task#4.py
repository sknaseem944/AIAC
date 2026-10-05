class Inventory:
	"""Manage stock quantities by item name."""

	def __init__(self):
		self._stock = {}

	def add_item(self, name, quantity):
		if quantity < 0:
			raise ValueError("Quantity cannot be negative")
		self._stock[name] = self._stock.get(name, 0) + quantity

	def remove_item(self, name, quantity):
		if quantity < 0:
			raise ValueError("Quantity cannot be negative")
		if quantity > self.get_stock(name):
			raise ValueError("Insufficient stock")
		self._stock[name] = self.get_stock(name) - quantity

	def get_stock(self, name):
		return self._stock.get(name, 0)


# Assert-based tests
inv = Inventory()
inv.add_item("Pen", 10)
assert inv.get_stock("Pen") == 10

inv.remove_item("Pen", 5)
assert inv.get_stock("Pen") == 5

inv.add_item("Book", 3)
assert inv.get_stock("Book") == 3


#test cases for error handling
try:
    inv.add_item("Pencil", -1)
except ValueError:
    pass
else:
    raise AssertionError("Adding negative quantity should raise ValueError")

try:
    inv.remove_item("Pen", -1)
except ValueError:
    pass
else:
    raise AssertionError("Removing negative quantity should raise ValueError")

try:
    inv.remove_item("Pen", 15)
except ValueError:
    pass
else:
    raise AssertionError("Removing more than available stock should raise ValueError")

print("All inventory tests passed.")