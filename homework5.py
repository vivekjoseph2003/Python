Frontend={"John","Messi","Chris"}
Backend={"Harry","John","Henry"}
Backend.add("Puyol")
print(Backend)
Frontend.remove("Chris")
print(Frontend)
print(Frontend&Backend)
print(Backend-Frontend)
print(len(Frontend|Backend))
course_dict={
    "Frontend":len(Frontend),
    "Backend":len(Backend)
    }
for x in course_dict:
    print("Course:",x,",Students:",course_dict[x])

dict_compr={**course_dict, "Fullstack":course_dict["Frontend"]+course_dict["Backend"]}
print(dict_compr)
