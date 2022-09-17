
print("enter any text with three words")
three_words=input()
last_index_of_firstword=three_words.find("") -1
last_index_of_secondword=three_words.rfind("") -1
last_index_of_lastword=len(three_words) -1

print(last_index_of_firstword+last_index_of_secondword+last_index_of_lastword)



