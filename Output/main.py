names = []
name = ''
with open ("/home/carlos/Bureau/100 days of python/Day 24/Input/Names/Invited_names.txt", 'r') as f:
    contents = f.read()
    for i in contents:
        if i != '\n':
            name += i
        else:
            names.append(name)
            name = ''
    print(names)
            
for name in names:
    with open(f"/home/carlos/Bureau/100 days of python/Day 24/Output/ReadyToSend/letter_to_{name}.docx", 'w') as file:
        file.write(f"Dear {name},\n\nYou are invited to my birthday this Saturday.\n\nHope you can make it!\n\nCarlos")