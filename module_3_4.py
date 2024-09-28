def single_root_words(root_word, *other_wods):
    single_root_words = []
    for w in other_wods:
        if root_word.lower() in w.lower():
            single_root_words.append(w)

    return single_root_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words( 'Able','Disablement', 'Mable', 'Disable', 'Bagel'))