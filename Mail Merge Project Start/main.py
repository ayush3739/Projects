#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


file=open("Input\Letters\starting_letter.txt",mode='r')
letter=file.read()
file.close()
with open("C:/Users/ayush/Documents/Day 24 - Files, Directories and Paths/Mail Merge Project Start/Input/Names/invited_names.txt",mode='r') as new:
    names=new.readlines()
    print(names)

for name in names:
    stripped_name = name.strip()
    output_path = f"C:/Users/ayush/Documents/Day 24 - Files, Directories and Paths/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt"
    with open(output_path, mode='w') as final:
        final.write(letter.replace('[name]', stripped_name))
    

