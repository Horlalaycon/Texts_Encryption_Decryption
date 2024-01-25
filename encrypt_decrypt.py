# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon
# This Program encrypt and decrypt texts by splitting, shifting the position in a circular order by shift_amount, rejoining and reversing the words.

def encrypt_decrypt(texts, shift_amount=2):
    split_texts = texts.split()
    shift_words = [split_texts[(i + shift_amount) % len(split_texts)] for i in range(len(split_texts))]
    join_words = " ".join(shift_words)
    reverse_words = join_words[::-1]
    result = reverse_words
    return result


text = input("Enter Text to encrypt or decrypt: ")

action = encrypt_decrypt(texts=text)

print(f"result: {action}")
