web_dev=["Lionel","Cristiano","Wayne"]
data_science=["Neymar","Suarez","Messi"]
ui_ux=["Rio","Evra","Vidic"]
all_participants=[web_dev,data_science,ui_ux]
web_dev.append("Marcus")
data_science.insert(1,"Scholes")
ui_ux.pop()
data_science_copy=data_science.copy()
data_science.clear()
print("First two Web Development participants:",web_dev[:2])
name_lengths=[len(name) for name in data_science_copy]
print("Lengths of Data Science participant names:",name_lengths)
asha_in_workshops="Asha" in web_dev or "Asha" in data_science_copy or "Asha" in ui_ux
print("Is 'Asha' in any workshop list?:",asha_in_workshops)
first_participants=(web_dev[0],data_science_copy[0],ui_ux[0]) 
print("First participant from each workshop:",first_participants)