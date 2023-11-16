def count_unique_characters(message: str) -> int:
	unique_chars = set(message.lower())
	unique_chars.discard(' ')
	print(unique_chars)
	return len(unique_chars)


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
