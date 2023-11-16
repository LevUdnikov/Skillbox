from collections import Counter


def can_be_poly(s: str) -> bool:
	counts = Counter(s)
	odd_count = sum(1 for count in counts.values() if count % 2 != 0)
	return odd_count <= 1


print(can_be_poly('abcba'))  # True
print(can_be_poly('abbbc'))  # False
