import hashlib
import time


def StartPasswordCracking(file_name, hash_md5):
    start_time = time.time()
    try:
        with open(file_name, "r") as pass_file:      #open password file
            for password in pass_file:
                if hashlib.md5(str(password).strip()).hexdigest() == hash_md5:     
                    #remove end of line from password, calculate hash and compare with provided one
                    end_time = time.time()
                    print("Cracked password is: " + password)
                    print("Total time comsumed: %.4f sec" % (end_time - start_time))
                    exit()
    except Exception as ex:
        print("Exception occured: "+ str(ex))
        print("Program terminated unsuccessfully")


if __name__ == "__main__":
    print("Dictionary Attack")
    print("Please enter following attributes in '"'<parameter>'"' format")
    file_name = str(input("Enter Password File: ")) 
    hash_md5 = str(input("Enter MD5 hash of password you want to crack: ")) 
    StartPasswordCracking(file_name, hash_md5)
