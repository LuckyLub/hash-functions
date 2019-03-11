
my_string = "Hello world!"
bin_string = str()

for letter in my_string:
    bin_string += format(ord(letter), 'b')
    print(format(ord(letter), 'b'))

bin_string += "1"
size_original_message = bin_string.__len__()
zeroes_to_add = 448 - size_original_message

a = bin(size_original_message)

bin_string = bin_string + "0" * zeroes_to_add


print(bin_string)
