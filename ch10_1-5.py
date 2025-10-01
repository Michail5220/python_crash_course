from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

# lines = contents.splitlines()
lines_list = []

for line in contents.splitlines():
    lines_list.append(line.replace('Python', 'C'))


for line in lines_list:
    print(line)
