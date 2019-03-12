from math import ceil

'''
• RotR(A, n) denotes the circular right shift of n bits of the binary word A.
• ShR(A, n) denotes the right shift of n bits of the binary word A.
• AkB denotes the concatenation of the binary words A and B.

The algorithm uses the functions:
Ch(X, Y, Z) = (X ∧ Y ) ⊕ (X ∧ Z),
M aj(X, Y, Z) = (X ∧ Y ) ⊕ (X ∧ Z) ⊕ (Y ∧ Z),
Σ 0 (X) = RotR(X, 2) ⊕ RotR(X, 13) ⊕ RotR(X, 22),
Σ 1 (X) = RotR(X, 6) ⊕ RotR(X, 11) ⊕ RotR(X, 25),
σ 0 (X) = RotR(X, 7) ⊕ RotR(X, 18) ⊕ ShR(X, 3),
σ 1 (X) = RotR(X, 17) ⊕ RotR(X, 19) ⊕ ShR(X, 10),
and the 64 binary words K i given by the 32 first bits of the fractional parts of the cube roots of the first
64 prime numbers:'''


def circular_right_shift(n, a):

    pass


def right_shift(n, a):
    pass


def bin_concat(a,b):
    pass


def ch(x, y, z):
    return (x & y) ^ (x & z)


def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)


def sigma0(x):

    pass


def sigma1(x):
    pass


def omega0(x):
    pass


def omega1(x):
    pass


my_string = "Hello world! PADDING STARTS HERE " \
            "The message shall always be padded, even if the initial length is already a multiple of 512." \
            "To ensure that the message 1 has length multiple of 512 bits:" \
            "STEP 1: first, a bit 1 is appended," \
            "STEP 2: next, k bits 0 are appended, with k being the smallest positive integer such that l + 1 + k ≡ 448" \
            "mod 512, where l is the length in bits of the initial message," \
            "--> I assume here that k is at least 1, since it should be a positive integer. That means that I at least, " \
            "should be able to store 1 byte for a 1, 1 byte for a 0, and 64 bytes for the size of the original string. " \
            "That means 66 in total. That means that the last chunk can not be bigger than 512 - 66 = 446, " \
            "else an additional chunk is added." \
            "STEP 3 finally, the length l < 2 64 of the initial message is represented with exactly 64 bits, and these " \
            "bits are added at the end of the message."


bin_string = str()

#Convert the string into a string of concatenated binary numbers.
for letter in my_string:
    bin_letter = format(ord(letter), '08b')
    bin_string += bin_letter
    # print(letter,bin_letter, bin_string)

#Since the algortithm processes the string in chunks of 512 bytes, we might need to split up our string in chunks
# of that size. We will set these chunks up in a list.
chunks_list = []
chunk_size = 512

size_bin_sting = bin_string.__len__()
chunks = ceil(size_bin_sting/chunk_size)

for r in range(chunks):
    lower_range = r * chunk_size
    upper_range = (r + 1) * chunk_size
    chunks_list.append(bin_string[lower_range:upper_range])

'''PADDING STARTS HERE
The message shall always be padded, even if the initial length is already a multiple of 512.
To ensure that the message 1 has length multiple of 512 bits:
STEP 1: first, a bit 1 is appended,
STEP 2: next, k bits 0 are appended, with k being the smallest positive integer such that l + 1 + k ≡ 448
mod 512, where l is the length in bits of the initial message,

--> I assume here that k is at least 1, since it should be a positive integer. That means that I at least, should be
able to store 1 byte for a 1, 1 byte for a 0, and 64 bytes for the size of the original string. That means 66 in 
total. That means that the last chunk can not be bigger than 512 - 66 = 446, else an additional chunk is added.


STEP 3 finally, the length l < 2 64 of the initial message is represented with exactly 64 bits, and these bits
are added at the end of the message.

'''

if chunks_list[-1].__len__() < 512 and chunks_list[-1].__len__() > 446:
    chunks_list[-1] = chunks_list[-1] + "1" #STEP 1
    zeroes_to_add = 512 - chunks_list[-1].__len__()
    chunks_list[-1] = chunks_list[-1] + "0" * zeroes_to_add

if chunks_list[-1].__len__() == 512:
    chunks_list.append("")

else:
    chunks_list[-1] = chunks_list[-1] + "1" #STEP 1

zeroes_to_add = 448 - chunks_list[-1].__len__()
chunks_list[-1] = chunks_list[-1] + "0" * zeroes_to_add #STEP 2

bin_size_original_message = format(bin_string.__len__(), '064b')
chunks_list[-1] = chunks_list[-1] + bin_size_original_message #STEP 3

# for chunk in chunks_list:
#     print(chunk.__len__(),chunk)

'''Block decomposition
For each block M ∈ {0, 1} 512 , 64 words of 32 bits each are constructed as follows:
• the first 16 are obtained by splitting M in 32-bit blocks
M = W 1 kW 2 k · · · kW 15 kW 16
• the remaining 48 are obtained with the formula:
W i = σ 1 (W i−2 ) + W i−7 + σ 0 (W i−15 ) + W i−16 ,
17 ≤ i ≤ 64.'''

block = []

for chunks in chunks_list:
    for i in range(16):
        block.append(chunks_list[i*32:(i+1)*32])
    for i in range(17,65):
        part1 = int(block[i-2], 2)
        part2 = int(block[i-7], 2)
        part3 = int(block[i-15], 2)
        part4 = int(block[i-16], 2)

        block.append()





