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

# ex 10-4
# guest_name = input("Please enter your name: ")
# new_path = Path('guest.txt')
# new_path.write_text(guest_name)

# ex 10-5


new_path = Path('guestbook.txt')

guest_book =''

guest_name = ''

isFirstIncrement = True
#i need to catch first at last increments
while guest_name.lower() != 'end':
    
    guest_name = input("Please enter your name (or type 'end' to quit): ")
    
    if guest_name.lower() != 'end':
        if isFirstIncrement:
            guest_book = f"{guest_name.title()}"
            isFirstIncrement=False
        else:
            guest_book = f"{guest_book},\n{guest_name.title()}"
    else:
        guest_book = f"{guest_book}."

new_path.write_text(guest_book)

