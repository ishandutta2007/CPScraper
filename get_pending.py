from pprint import pprint

a = open("cf_activereds").readlines()
b = open("cf_inactivereds").readlines()
alls = set(a).union(set(b))
# cf_userlist.txt
dones = open("cf_userlist.txt").readlines()
pendings = set(alls).difference(dones)
pendings = [p.replace("\n", "") for p in pendings]
pprint(list(pendings))
