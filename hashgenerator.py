import hashlib

a = True
while a:

    hashtxt = input("Enter The String You Want To Hash")

    hashalgo = input("Enter The Required Hashing Algorithm\nmd5\nsha1\nsha256\nsha384\nsha512")

    print("\n")

    if hashalgo == "md5":

        hashme  = hashlib.md5(hashtxt.encode())

        print("result =",hashme.hexdigest())

    if hashalgo == "sha1":

        hashme  = hashlib.sha1(hashtxt.encode())

        print("result =",hashme.hexdigest())

    if hashalgo == "sha256":

        hashme  = hashlib.sha256(hashtxt.encode())

        print("result =",hashme.hexdigest())


    if hashalgo == "sha384":

        hashme  = hashlib.sha384(hashtxt.encode())

        print("result =",hashme.hexdigest())

    if hashalgo == "sha512":

        hashme  = hashlib.sha512(hashtxt.encode())

        print("result =",hashme.hexdigest())


    if hashalgo == "":

        print("Enter a Valid Algorithm")