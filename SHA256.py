from math import ceil


def add_mod(*args):
    result = int()
    for arg in args:
        result += int(arg, 2)
    result = result % (2**32)
    return format(result, "032b")


def RotR(A, n):
    first_part = A[-n:]
    last_part = A[:-n]
    return first_part + last_part


def ShR(A, n):
    A = int(A, 2)
    result = A >> n
    return format(result, "032b")


def AkB(*args):
    result = ""
    for arg in args:
        result += arg
    return result


def ch(X, Y, Z):
    X = int(X, 2)
    Y = int(Y, 2)
    Z = int(Z, 2)
    result = (X & Y) ^ ((~X) & Z)
    return format(result, "032b")


def maj(X, Y, Z):
    X = int(X, 2)
    Y = int(Y, 2)
    Z = int(Z, 2)
    result = (X & Y) ^ (X & Z) ^ (Y & Z)
    return format(result, "032b")


def sigma0(X):
    first_part = int(RotR(X, 2), 2)
    second_part = int(RotR(X, 13), 2)
    third_part = int(RotR(X, 22), 2)
    result = first_part ^ second_part ^ third_part
    return format(result, "032b")


def sigma1(X):
    first_part = int(RotR(X, 6), 2)
    second_part = int(RotR(X, 11), 2)
    third_part = int(RotR(X, 25), 2)
    result = first_part ^ second_part ^ third_part
    return format(result, "032b")


def omega0(X):
    first_part = int(RotR(X, 7), 2)
    second_part = int(RotR(X, 18), 2)
    third_part = int(ShR(X, 3), 2)
    result = first_part ^ second_part ^ third_part
    return format(result, "032b")


def omega1(x):
    first_part = int(RotR(x, 17), 2)
    second_part = int(RotR(x, 19), 2)
    third_part = int(ShR(x, 10), 2)
    result = first_part ^ second_part ^ third_part
    return format(result, "032b")


def T1_f(h, e, f, g, k_num, w_block):
    result = add_mod(h, sigma1(e), ch(e,f,g), k_num, w_block)
    return result


def T2_f(a, b, c):
    return add_mod(sigma0(a), maj(a, b, c))




my_string = "Hello world!"


bin_string = str()

#Convert the string into a string of concatenated binary numbers.
for letter in my_string:
    bin_letter = format(ord(letter), '08b')
    bin_string += bin_letter
    # print(letter,bin_letter, bin_string)

#Since the algortithm processes the string in chunks of 512 bytes, we might need to split up our string in chunks
# of that size. We will set these chunks up in a list.
M_blocks = []
chunk_size = 512

size_bin_sting = bin_string.__len__()
chunks = ceil(size_bin_sting/chunk_size)
if chunks == 0:
    chunks = 1

for r in range(chunks):
    lower_range = r * chunk_size
    upper_range = (r + 1) * chunk_size
    M_blocks.append(bin_string[lower_range:upper_range])


if M_blocks[-1].__len__() < chunk_size and M_blocks[-1].__len__() > 446:
    M_blocks[-1] = M_blocks[-1] + "1" #STEP 1
    zeroes_to_add = 512 - M_blocks[-1].__len__()
    M_blocks[-1] = M_blocks[-1] + "0" * zeroes_to_add

if M_blocks[-1].__len__() == chunk_size:
    M_blocks.append("")

else:
    M_blocks[-1] = M_blocks[-1] + "1" #STEP 1

zeroes_to_add = 448 - M_blocks[-1].__len__()
M_blocks[-1] = M_blocks[-1] + "0" * zeroes_to_add #STEP 2

bin_size_original_message = format(bin_string.__len__(), '064b')
M_blocks[-1] = M_blocks[-1] + bin_size_original_message #STEP 3
chunks = M_blocks.__len__()



for index, chunks in enumerate(M_blocks):
    W_blocks = []
    for t in range(16):
        W_blocks.append(chunks[t * 32:(t + 1) * 32])
    for t in range(17, 65):
        part1 = omega1(W_blocks[t - 1 - 2])
        part2 = W_blocks[t - 1 - 7]
        part3 = omega0(W_blocks[t - 1 - 15])
        part4 = W_blocks[t - 1 - 16]
        result = add_mod(part1, part2, part3, part4)
        W_blocks.append(result)
    M_blocks[index] = W_blocks

K_nr = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

for index, k in enumerate(K_nr):
    K_nr[index] = format(k, "032b")

H1 = format(0x6a09e667, "032b")
H2 = format(0xbb67ae85, "032b")
H3 = format(0x3c6ef372, "032b")
H4 = format(0xa54ff53a, "032b")
H5 = format(0x510e527f, "032b")
H6 = format(0x9b05688c, "032b")
H7 = format(0x1f83d9ab, "032b")
H8 = format(0x5be0cd19, "032b")


for index_M, M_block in enumerate(M_blocks):

    a = H1
    b = H2
    c = H3
    d = H4
    e = H5
    f = H6
    g = H7
    h = H8

    for i in range(64):
        T1 = T1_f(h, e, f, g, K_nr[i], M_block[i])
        T2 = T2_f(a, b, c)
        h = g
        g = f
        f = e
        e = add_mod(d, T1)
        d = c
        c = b
        b = a
        a = add_mod(T1, T2)

    H1 = add_mod(H1, a)
    H2 = add_mod(H2, b)
    H3 = add_mod(H3, c)
    H4 = add_mod(H4, d)
    H5 = add_mod(H5, e)
    H6 = add_mod(H6, f)
    H7 = add_mod(H7, g)
    H8 = add_mod(H8, h)

H = AkB(H1, H2, H3, H4, H5, H6, H7, H8)

print(hex(int(H, 2)))
