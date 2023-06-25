with open("artifact.txt",'r') as f:
    text = f.read()
print(text)
with open("artifact.txt",'w') as f:
    text = f.write(text+" have added one more line")

print(text)
print("It is the end of stage 3")