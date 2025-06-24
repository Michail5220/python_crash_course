message = "hi"

# print(message)

message_2 = message + ",\thow are you?"

print(message_2.title())
print(message_2.upper())
print(message_2.lower())

message_3= "what's up?\n"

new_var = f"{'   '+message_3.title() + message_2.upper()+'   '}"
print(new_var.lstrip())
print(new_var.rstrip())
print(new_var.strip())

new_url = "https://www.somesite.com"

print(new_url.removeprefix("https://"))