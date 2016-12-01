import markovify

def main():
    with open("prideandprejudice.txt") as f:
        text = f.read()
    text_model = markovify.Text(text)

    novel = ''
    words = 0

    while(words < 50000):
        line = text_model.make_sentence_with_start("Mr. Darcy")
        line = line.split()
        words += len(line)

        for word in line:
            novel += ''.join(word) + ' '
        novel += '\n'

    with open("mrdarcyandmrdarcy.txt", "w") as f:
        f.write(novel)

main()
