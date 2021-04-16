import random


def get_jokes(const, jack=False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    words = []
    while const:
        if jack:
            words.append(f'{nouns.pop(nouns.index(random.choice(nouns)))}'
                         f' {adverbs.pop(adverbs.index(random.choice(adverbs)))}'
                         f' {adjectives.pop(adjectives.index(random.choice(adjectives)))}')
        else:
            words.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
        const -= 1
    return words


print(get_jokes(4, True))
