# Arrange string characters such that lowercase letters should come first

txt = "PyNaTive"

arrange = ""
non_arrange = ""

for i in txt:
    if i == i.upper():
        arrange += i
    else:
        non_arrange += i
print("Arranged string is: " ,non_arrange + arrange)