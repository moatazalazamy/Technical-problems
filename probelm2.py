def two_strings(str1, str2):
    str1 = set(str1.replace(' ',''))
    str2 = set(str2.replace(' ',''))
    s = str1.intersection(str2)
    if len(s)>0:
        return "Yes"
    else:
        return "No"

'''
#implement without intersection function
#call it by tmp(string1, string2)
char = {'a': 0, 'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}
def tmp(s1, s2):
    str1 = set(s1.replace(' ',''))
    str2 = set(s2.replace(' ',''))
    for i in s1:
        char[i] = 1
    for i in s2:
        if char[i] == 1:
            print("Yes")
            return 
    print("No")

'''

if __name__ =='__main__':
    st1 = input("Enter first string: ")
    st2 = input("Enter second string: ")
    print(two_strings(st1,st2))
