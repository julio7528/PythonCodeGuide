#Set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
contentA = set(['5','7','3','4'])
contentA.add('10')
contentA.remove('3')
contentA.pop()
contentA.update(['19','20'])
contentA.difference_update(['1','2','3'])
contentA.discard('4')
#content.clear()
print(contentA)

contentB = set(['4','5','6','7'])
print(contentB)

union = contentA.union(contentB)
print(union)

intersect = contentA.intersection(contentB)
print(intersect)

#The issubset() method returns True if another set contains this set, otherwise it returns False.
issubset = contentA.issubset(contentB)
print(issubset)

#The difference is the difference between two sets as a new set. The difference of A and B is the set of elements that are in A but not in B.
difference = contentA.difference(contentB)
print(difference)
difference = contentB.difference(contentA)
print(difference)

#The symmetric difference of two sets is the set of elements which are in either of the sets and not in their intersection.
symmetric_difference = contentA.symmetric_difference(contentB)
print(symmetric_difference)

#issuperset() method returns True if another set contains this set, otherwise it returns False.
issuperset = contentA.issuperset(contentB)
print(issuperset)

#Update the set with the union of this set and others.
update = contentA.update(contentB)
print(update)

#Convert the set into a list.
contentA = list(contentA)
print(contentA)

#To search a specifc valuen in the set, use the in keyword.
if '5' in contentA:
    print('Yes, 5 is in the set')
#Using For
for x in contentA:
    if '5' in contentA:
        print('Yes, 5 is in the set')
        if '5' == x:
            print(x)
            break

content1 = {1,2,3}
content2 = {3,4,5}
#Another Union examples
union2 = content1 | content2
print(union2)

#Another Intersection examples
intersect2 = content1 & content2
print(intersect2)

