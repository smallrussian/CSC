
b1="001"
b18=b1.zfill(8)
#print(b1)
def write_file(filename, content):
    f=open(filename, "w")
    for item in content:
        f.writelines(item+"\n")
    f.close()
def read_file(filename):
    try: 
        f=open(filename, "r")
    except FileNotFoundError:
        print("File Does Not Exist, please create file")
    else:
        ciphertext=f.readlines()
        f.close
        return ciphertext
def twos(char):
    a = bin(char)
    b = bin(char)[2:]
    c = b. zfill(8)
    translation={"0":"1","1":"0"}
    compliment=''
    #print(c)
    for i in c:
        compliment+=translation[i]
    #print(compliment)
    twos=compliment
    decimaltwos=int(twos,2)+int(b18,2)
    bintwos=bin(decimaltwos)[2:]
    return bintwos
def reverse_twos_comp(val, bits): #found this function at https://stackoverflow.com/questions/1604464/twos-complement-in-python
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is

def decryption():
    ciphertext=(read_file("encrypted.txt"))
    #print(ciphertext)
    list=[]
    for item in ciphertext:
        list.append(item)
    new_list=[x[:-1] for x in list]
    #print(new_list)
    ascii_list=[]
    for element in new_list:
        reverse=reverse_twos_comp(int(element, 2), len(element))
        reverse=(~reverse+1)
        ascii_list.append(reverse)
    #print(ascii_list)
    #for lines 50-52 credit to https://www.geeksforgeeks.org/python-ways-to-convert-list-of-ascii-value-to-string/
    final_str=""
    for value in ascii_list:
        final_str+=chr(value)
    return final_str
def encryption():
    plaintext=str(input("Please enter a string\n"))
    ascii=[]
    for a in plaintext:
        ascii.append(ord(a))
    #print(ascii)
    twoslist=[]
    for num in ascii:
        twoslist.append(twos(num))
    write_file("encrypted.txt", twoslist)
    print(twoslist)
    

#mainloop
usr_input=int(input("Please enter 1 for encryption and 2 for decryption\n"))
while(True):
    if usr_input==1:
        encryption()
        input2=int(input("Would you like to decrypt? Press 1 for yes, 2 for no\n"))
        while(True):
            if input2==1:
                print(decryption())
                break
            elif input2==2:
                print("have a nice day!\n")
                break
            else:
                print("Please enter a valid selection\n")
        break
        
    elif usr_input==2:
        print(decryption())
        break
    else:
        print("Please enter a valid selection")

