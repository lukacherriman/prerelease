def hashing_algorithm(username, password):
    # to make sure all the hashes are unique the salt used will be their unique username
    us_list = [ord(ch) for ch in username]
    pw_list = [ord(ch) for ch in password]

    exponent = 2
    pw_weight = []
    for i in range(len(pw_list)):
        pw_weight.append(pw_list[i] ** exponent)
        if exponent == 8:
            exponent = 2
        else:
            exponent += 2

    hash_pw = sum(pw_weight) + sum(us_list)
    mod_hash = hash_pw % (2 ** 48)

    return mod_hash, hash_pw

print(hashing_algorithm("Lcherriman", "Dank385,"))
