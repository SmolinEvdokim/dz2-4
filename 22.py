n = int(input("Vvvedite koli4estvo elementov pervogo mnojestva: "))
m = int(input("ВVvvedite koli4estvo elementov vtorogo mnojestva: "))

set1 = set()
for i in range(n):
    element = int(input("vvedite elementi pervogo mnojestva: "))
    set1.add(element)

set2 = set()
for i in range(m):
    element = int(input("vvedite elementi vtorogo mnojestva: "))
    set2.add(element)

intersection = sorted(list(set1 & set2))

print("obc4ie elementi:", intersection)
