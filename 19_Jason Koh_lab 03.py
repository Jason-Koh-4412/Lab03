a = 10
print(a)
print(type(a))

b = 5 + 6j
print(b)
print(type(b))

c = 10.5
print(c)
print(type(c))

e = 'Testing String'
print(e)
print(type(e))

f = [1, 2, 3]
print(f)
print(type(f))

g = (4, 5, 6)
print(g)
print(type(g))

h = {'Student': 'Aaron'}
print(h)
print(type(h))

i = {7, 8, 9}
print(i)
print(type(i))

j = [1, 2, 3]
k = f + j
print(k)
print(type(k))
print(1 in k)

l = (10, 11, 12)
m = l + g
print(m)
print(type(m))

k[0] = 11
print(k)

n = {'Lecturer': 'Judy'}
h.update(n)
print(h)
print(type(h))

o = {9, 10, 11}
print(o.union(i))
print(type(o))

o = {9, 10, 11}
print(o.intersection(i))
print(type(o))

# DIY Challenges
diy_countries = {'AU' : 'Australia', 'BE' : 'Belgium', 'CN': 'China', 'DK' : 'Denmark'}
diy_new_key_list = list(diy_countries.keys())
diy_new_values = list(diy_countries.values())

diy_new_countries = diy_new_values.index('Australia')
print("Get a key by value:",diy_new_key_list[diy_new_countries])

Names = ['Thomas', 'Lind', 'Cath', 'Benny']
Names.sort()
print(Names)

Names.pop()
Names.pop()
Names.pop()
Names.pop()

print(Names)