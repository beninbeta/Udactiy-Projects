import random
import words


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)
    noun = words
    silly_redux = []
    index = 0
    while index < len(template):
        if template[index : index + len("{{noun}}")] == "{{noun}}":
            silly_redux.append(random.choice(nouns))
            index += len("{{noun}}")
        elif template[index: index + len("{{verb}}")] == "{{verb}}":
            silly_redux.append(random.choice(verbs))
            index += len("{{verb}}")
        else:
            silly_redux.append(template[index])
            index += 1
    return "".join(silly_redux)
if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs,
        words.templates))


