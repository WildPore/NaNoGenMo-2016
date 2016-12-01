import markovify

def main():
    with open("prideandprejudice.txt") as f:
        text = f.read()
    text_model = markovify.Text(text)
    for i in range(10):
        print(text_model.make_sentence_with_start("Wedding"))

def first_word(file):
    first_words = []
    with open(file) as f:
        for line in f:
            first_words.append(line.rstrip().split(' ', 1)[0])

    return first_words

main()
