aclNum = int(input("ACL Number? "))
if aclNum >= 1 and aclNum <= 99:
    print("Standard")
elif aclNum >= 100 and aclNum <= 199:
    print("Extended")
else:
    print("Not Standard or Extended")