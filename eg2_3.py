import eg2_1
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print (eg2_1).buildConnectionString(params)
print (eg2_1).buildConnectionString.__doc__