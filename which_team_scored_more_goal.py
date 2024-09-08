# from given string print which team scored moer goal

s = "teamA teamB teamB teamB teamA teamA teamB"
a = list(s.split(" "))
count_A = 0
count_B = 0
for el in a:
    if el == "teamA":
        count_A +=1
    else:
        count_B +=1
if count_B > count_A:
    print("Team B")
else:
    print("Team A")
