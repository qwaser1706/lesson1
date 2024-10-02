def single_root_words(root_word, *other_wods):
    single_root_words = []
    for i in other_wods:
        if root_word.lower() in i.lower():
            single_root_words.append(i)
    for y in other_wods:
        if y.lower() in root_word.lower():
            single_root_words.append(y)
    return single_root_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words( 'Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
