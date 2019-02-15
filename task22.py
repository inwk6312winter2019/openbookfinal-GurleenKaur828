file=open("access.log")
file1=open("get.log","a+")
file2=open("post.log","a+")
file3=open("put.log","a+")
file4=open("delete.log","a+")

def log_file(file):
	count1=0
	count2=0
	for line in file:
		line=line.split()
		if 'get' in line:
			if 'ip address' in line:
				count=count+1
				print(count1)
		if 'get' in line:
                        if 'ip address' in line:
                                count=count+1
                                print(count2)
print(log_file(file))


