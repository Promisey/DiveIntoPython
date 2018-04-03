params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
print(params.values())
print(params.items())
li = ["%s=%s" % (k, v) for k, v in params.items()]
print(li)
s = ";".join(li)
print(s)
print(s.split(";"))