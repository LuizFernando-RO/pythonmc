def sentenceMaker(phrase):
    interrogatives = ('how','what','why')
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return '{}?'.format(capitalized)
    else:
        return '{}.'.format(capitalized)

results = []
while True:
    userInput = input("Say something: ")
    if userInput == '\end':
        break
    else:
        results.append(sentenceMaker(userInput))

print(" ".join(results))