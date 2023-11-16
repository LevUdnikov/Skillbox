import os


def gen_python_files(directory='C:/'):
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith('.py'):
				file_path = os.path.join(root, file)
				with open(file_path, 'r') as f:
					lines = f.readlines()
					non_empty_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
					yield file_path, len(non_empty_lines)


# Пример использования, вместо Users мб любая другая директория
for file_path, num_lines in gen_python_files('C:/Users'):
	print(f'{file_path}: {num_lines} non-empty non-comment lines')
