Python={"John","Messi","Chris"}
Data_Science={"Harry","John","Henry"}
Python.add("Rooney")
print(Python)
Data_Science.remove("Henry")
print(Data_Science)
print(Python&Data_Science)
print(Python-Data_Science)
print(Python|Data_Science)
student_dict={
    "Python":len(Python),
    "Data_Science":len(Data_Science)
    }
for x in student_dict:
    print("Course:",x,",Students:",student_dict[x])
    
dict_compr={x:student_dict[x]*2 for x in student_dict}
print(dict_compr)