""" The code is to count how many time "the " appear in the american_novel.txt book"""
document = "american_novel.txt"
with open(document) as file_object:
    contents = file_object.read()
number_count = contents.lower().count("the ")
print(number_count)

# To count total number of words in american_novel.txt
number_words = contents.split()
print(len(number_words))
