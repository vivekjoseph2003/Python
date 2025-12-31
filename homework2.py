paragraph="""Python is a popular programming language.
Our course helps students learn Python basics.
Python is easy to learn."""
length=len(paragraph)
print("Length of paragraph:",length)
print("First character:",paragraph[0])
print("Last character:",paragraph[-1])
print("Preview:",paragraph[:50])
replaced_para=paragraph.replace("Python","PYTHON")
print("After replacement:\n",replaced_para)
lower_para=paragraph.lower()
print("Lowercase paragraph:\n",lower_para)
stripped_para=paragraph.strip()
print("After stripping whitespace:\n",stripped_para)
words=paragraph.split()
print("List of words:",words)
if "course" in paragraph.lower():
    print("The word 'course' is found in the paragraph.")
word_count=len(words)
final_message="The course description is {} characters long and has {} words.".format(length, word_count)
print(final_message)