from utils48 import BinRW
filename=input("binary here or type filename:")
if filename.replace("0","").replace("1","")=="":
    decode=filename
else:
    f=BinRW.fileRW(filename)
    decode=~f
def decodeTree(remainingBits):
    if remainingBits[0]=="1":
        return chr(int(remainingBits[1:9],2)),remainingBits[9:]
    elif remainingBits[0]=="0":
        zero,remainingBits=decodeTree(remainingBits[1:])
        one,remainingBits=decodeTree(remainingBits)
        return (zero,one),remainingBits
tree,binary=decodeTree(decode)
text=""
current=tree
print(current)
for i in binary:
    if type(current[int(i)])==tuple:
        current=current[int(i)]
    else:
        text+=current[int(i)]
        current=tree 
print(text)
file=input("filename to save to (no for dont save):")
if file != "no":
    with open(file,"w+") as f:
        f.write(text)
