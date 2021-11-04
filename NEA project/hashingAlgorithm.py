def hashing_algorithm(username, password):
    # to make sure all the hashes are unique the salt used will be their unique username
    us_list = [ord(ch) for ch in username]
    pw_list = [ord(ch) for ch in password]

    pw_weight = [pw_list[i] ** (2*(i+1)) for i in range(len(pw_list))]
    us_weight = [us_list[i] ** (2*(i+1)) for i in range(len(us_list))]
    hash_pw = sum(pw_weight) + sum(us_list)


    mod_hash = hash_pw % 2 ** 48

    return mod_hash

print(hashing_algorithm("Lcherriman", "Dank385,"))