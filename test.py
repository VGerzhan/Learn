import time
# o = ['spam', 'eggs', 100, 1234, 10, 35, 48, 75, 66]
# t1 = time.time()
# for i in range(10**5):
#     o.append('xtra')
# t2 = time.time()
# print (t2 - t1)
#
# t1 = time.time()
# for i in range(10**5):
#     o.insert(1, 'xtra')
# t2 = time.time()
# print (t2 - t1)
# print ("Len o  = " + str(len(o)))
#
# t1 = time.time()
# while i < len(o):
#     o.remove(o[i])
# t2 = time.time()
# print (t2 - t1)

v = {'server': 'mpilgrim', 'uid': 'sa', 'database': 'master', 42: 'douglas', 'retrycount': 3}
# Add
t1 = time.time()
for i in range(10**5):
    v[i] = 'xtra'
t2 = time.time()
print (t2 - t1)
# Get
t1 = time.time()
for i in v:
    v.get(i)
t2 = time.time()
print (t2 - t1)
# Del
t1 = time.time()
vCopy = v.copy()
for key in vCopy.keys():
        del v[key]
t2 = time.time()
print (t2 - t1)

https://github.com/janusnic/21v-python/
