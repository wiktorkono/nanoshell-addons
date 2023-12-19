import hashlib

def get_hash(file_path, hashType):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()

            hashType = hashType.upper()

            if hashType == "MD5":
                md5_hash = hashlib.md5(data).hexdigest()
                print("MD5 Hash:", md5_hash)
            elif hashType == "SHA1":
                sha1_hash = hashlib.sha1(data).hexdigest()
                print("SHA1 Hash:", sha1_hash)
            elif hashType == "SHA256":
                sha256_hash = hashlib.sha256(data).hexdigest()
                print("SHA256 Hash:", sha256_hash)
            elif hashType == "SHA512":
                sha512_hash = hashlib.sha512(data).hexdigest()
                print("SHA512 Hash:", sha512_hash)
            elif hashType == "SHA224":
                sha224_hash = hashlib.sha224(data).hexdigest()
                print("SHA224 Hash:", sha224_hash)
            elif hashType == "SHA384":
                sha384_hash = hashlib.sha384(data).hexdigest()
                print("SHA384 Hash:", sha384_hash)
            elif hashType == "BLAKE2B":
                blake2b_hash = hashlib.blake2b(data).hexdigest()
                print("BLAKE2B Hash:", blake2b_hash)
            elif hashType == "BLAKE2S":
                blake2s_hash = hashlib.blake2s(data).hexdigest()
                print("BLAKE2B Hash:", blake2s_hash)
            elif hashType == "ALL":
                md5_hash = hashlib.md5(data).hexdigest()
                sha1_hash = hashlib.sha1(data).hexdigest()
                sha256_hash = hashlib.sha256(data).hexdigest()
                sha512_hash = hashlib.sha512(data).hexdigest()
                sha224_hash = hashlib.sha224(data).hexdigest()
                sha384_hash = hashlib.sha384(data).hexdigest()
                blake2b_hash = hashlib.blake2b(data).hexdigest()
                blake2s_hash = hashlib.blake2s(data).hexdigest()
                print("MD5 Hash:", md5_hash)
                print("\nSHA1 Hash:", sha1_hash)
                print("\nSHA256 Hash:", sha256_hash)
                print("\nSHA512 Hash:", sha512_hash)
                print("\nSHA224 Hash:", sha224_hash)
                print("\nSHA384 Hash:", sha384_hash)
                print("\nBLAKE2B Hash:", blake2b_hash)
                print("\nBLAKE2S Hash:", blake2s_hash)
            else:
                print("Invalid hash type")
    except FileNotFoundError:
        print("File not found")


def obtain_hash(args):
    if args.startswith("gethash "):
        split_args = args.split(" ", 3)
        if len(split_args) >= 3:
            hash_type = split_args[1]
            file_path = split_args[2]
            get_hash(file_path, hash_type)
        else:
            print("Missing argument(s): hash type and file path are required.")
            print("Command syntax: gethash <hash type> <file path>")
    else:
        pass
