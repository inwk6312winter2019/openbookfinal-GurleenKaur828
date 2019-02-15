file=open("access.log")
file1=open("get.log","a+")
file2=open("post.log","a+")
file3=open("put.log","a+")
file4=open("delete.log","a+")
def log_file(file):
	for line in file:
		line=line.split()
		if 'get' in line:
			file1.append(line)
		elif 'post' in line:
                       file2.append(line)
		elif 'put' in line:
                        file3.append(line)
		elif 'delete' in line:
                        file4.append(line)
print(log_file(file))
