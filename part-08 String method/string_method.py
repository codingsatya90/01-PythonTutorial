text = "my name is satyanarayan kumar"

# new_text = text.upper() #upper method
# new_text = text.lower()    #lower method
# new_text = text.title()      #title method
# new_text = text.strip()      #strip method---using word space
# new_text = text.lstrip()    #lstrip methosd remove left side space
# new_text = text.rstrip()      #lstrip methosd remove left side space

# new_text = text.find("kum")      #find the letter number

new_text = text.replace("kumar", "chauhan")  # replace method
# new_text = text.replace("k", "c")              #replace method

print(new_text)

# new_text = "chauhan" in text  //output-- False   // check  currect words yes ya  no

new_text = "chauhan" not in text   #output-- True
print(new_text)
