def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    appleLocs = []
    orangeLocs = []
    numa = 0
    numo = 0
    print("Apple locations")
    for i in apples:
        appleLocs.append(a+i)
        print(a+i)
    print("Orange Locations")
    for j in oranges:
        print(b+j)
        orangeLocs.append(b+j)
    for apple in appleLocs:
        if(apple>=s and apple<=t):
            numa += 1
    for orange in orangeLocs:
        if(orange>=s and orange<=t):
            numo += 1
    print("Apples")
    print(numa)
    print("Oranges")
    print(numo)

countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])