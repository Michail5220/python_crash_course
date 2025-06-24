name = "Eric johnson"
message = "Hi " + name.title() + ", would you like to learn some Python today?"
message1 = "Hi " + name.lower() + ", would you like to learn some Python today?"
message2 = "Hi " + name.upper() + ", would you like to learn some Python today?"
print(message)
print(message1)
print(message2)
author = 'somebody   '
message = '  once said: "the only way is through"   '
quote = f"{author.rstrip().title()}\n {message.lstrip()}"
print(quote)
fileName = "python_notes.txt"
print(fileName.removesuffix(".txt"))