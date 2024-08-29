given_str="hello Akhil! how you doing akhil"

search_word="Akhil"

sub_string=search_word.lower()
str=given_str.lower()
# result=str.count(sub_string)

# print("Number of times word {} is {}".format(search_word,result))


#def find_occurrences(string, search_string):
occurrences = []
for i in range(len(str) - len(sub_string) + 1):
        if str[i:i+len(sub_string)] == sub_string:
            occurrences.append(i)
result = len(occurrences)

    # Example usage
print(f"Occurrences of '{search_word}' in the given string: {result}")
