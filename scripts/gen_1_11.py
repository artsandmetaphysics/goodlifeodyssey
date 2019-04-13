stories = [
    35,  # creation 1
    20,  # creation 2
    25,  # sin
    16,
    26 - 16,
    32,
    22 + 24 + 22 + 17,
    10,
    32,
    9,
    22,
]

height = 550  # px

verses = sum(stories)

story_heights = [round(s/verses*height) for s in stories]

for h in story_heights:
    print(h)
