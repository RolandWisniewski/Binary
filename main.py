import os
import glob

text = "Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than     dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced."

text_list = text.split("\n")
for i, v in enumerate(text_list):
    text_list[i] = " ".join(v.split())

for i, lines in enumerate(text_list):
    with open(f"plik{i}.txt", mode="w") as f:
        for character in lines:
            if character == '\n':
                ascii_code = ord(character)
                bin_value = bin(ascii_code)[2:]
                f.write("000" + bin_value)
            elif character == ' ' or character == '.' or character == "'":
                ascii_code = ord(character)
                bin_value = bin(ascii_code)[2:]
                f.write("0" + bin_value)
            else:
                ascii_code = ord(character)
                bin_value = bin(ascii_code)[2:]
                f.write(bin_value)
        f.close()

my_decoded_text = ''
for i, plik in enumerate(text_list):
    with open(f"plik{i}.txt", mode="r") as f:
        for lines in f:
            lines.strip()
            for i in range(0, len(lines.strip()), 7):
                text_part = lines.strip()[i:i+7]
                int_from = int(text_part, 2)
                chr_from = chr(int_from)
                my_decoded_text += chr_from
            my_decoded_text += '\n'
    f.close()

print(my_decoded_text[:-1])

cwd = os.getcwd()
file_path = f'{cwd}/plik*.txt'
files = glob.glob(file_path)

for i in files:
    os.remove(i)
