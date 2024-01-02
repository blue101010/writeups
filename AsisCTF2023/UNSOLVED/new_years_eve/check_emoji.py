import emoji

text = "ASIS{🎈🍻💃🌃🎆🎇🍾🎉🎊🍷🍸🍹🍺🏙️🍆🗻🥃🥂🕺🌉🕛🥳👯}"

# Decode the emojis into text
decoded_text = emoji.demojize(text)

# Print the decoded text
print(decoded_text)

# Generate the summary string
summary = ''.join(word[0] for word in decoded_text.split(':')[1::2])

# Print the summary string
print("Summary:", summary)