import random


def generateRandomDNASequence(length):
    nucleotides = 'ACGT'
    sequence = ''
    for _ in range(length):
        sequence += random.choice(nucleotides)
    return sequence


def findQueryMatches(query, text):
    matches = []
    queryLength = len(query)
    for i in range(len(text) - queryLength + 1):
        if text[i:i+queryLength] == query:
            matches.append(i)
    return matches


# m = 100
# text = generateRandomDNASequence(m)
# print(f'Text : {text}')

# query = 'AGT'
# print(f'Query : {query}')

# matches = findQueryMatches(query, text)

# if len(matches) == 0:
#     print('No matches found')
# else:
#     print(f'Found {len(matches)} matches at positions: {matches}')
