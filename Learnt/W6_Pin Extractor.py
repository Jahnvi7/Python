def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        print(len(words[line_index]))


poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)