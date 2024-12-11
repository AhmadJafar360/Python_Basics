pesan = input("> ")
words = pesan.split(' ')
emoji = {
    ":)" : "😄",
    ":(" : "☹️"
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)

# Creating a Reusable Function
def emoji_converter(message):
    words = message.split("")
    emojis = {
        ":)" : "😄",
        ":(" : "☹️"
    }
    hasil = ""
    for word in words:
        hasil += emojis.get(word, word) + " "
    return hasil

message = input(">")
print(emoji_converter(message))