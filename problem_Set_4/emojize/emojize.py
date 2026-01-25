from emojize_data import EmojiLibrary

emoji_lib = EmojiLibrary()
input_text = input("Input: ")

# Replace all :emoji_code: patterns with actual emojis
output = input_text
for emoji_name, emoji_char in emoji_lib.EMOJI_DICT.items():
    # Replace :emoji_name: with the actual emoji
    output = output.replace(f":{emoji_name}:", emoji_char)

print(output)