def id_to_reference(df, verse_id):
    # Look up the verse ID in the dataframe
    reference = df[df['Verse_ID'] == verse_id]

    # Extract the book, chapter, and verse
    book = reference['Book_Name'].values[0]
    chapter = reference['Chapter'].values[0]
    verse = reference['Verse'].values[0]

    verse_formatted = f"{book} {chapter}:{verse}"

    # Return the book, chapter, and verse
    return book, chapter, verse, verse_formatted


def reference_to_id(df, book, chapter, verse):
    # Look up the book, chapter, and verse in the dataframe
    reference = df[(df['Book_Name'] == book) & (df['Chapter'] == chapter) & (df['Verse'] == verse)]

    # Extract the verse ID
    verse_id = reference['Verse_ID'].values[0]

    # Return the verse ID
    return verse_id


def find_cross_references(df, verse_id):
    # Find the rows where the verse ID is either the start or the end of a cross-reference
    cross_references = df[(df['cf_start'] == verse_id) | (df['cf_end'] == verse_id)]
    main_verse = get_verse(df, verse_id)

    # cross_references = format_verse(cross_references)
    # main_verse = format_verse(main_verse)

    return cross_references


def book_to_number(df, book):
    # Look up the book name in the dataframe
    reference = df[df['Book_Name'] == book]

    # Extract the book number
    book_number = reference['Book_Number'].values[0]

    # Return the book number
    return book_number


def number_to_book(df, number):
    # Look up the book number in the dataframe
    reference = df[df['Book_Number'] == number]

    # Extract the book name
    book_name = reference['Book_Name'].values[0]

    # Return the book name
    return book_name


def full_text(df):
    full_text = df.drop_duplicates(subset='Verse_ID')
    return full_text


def get_verse(df, verse_id):
    verse = full_text(df)
    verse = verse[verse['Verse_ID'] == verse_id]
    return verse


def format_verse(verse, format_=None):
    verse['Reference'] = verse['Book_Name'] + ' ' + verse['Chapter'].astype(str) + ':' + verse['Verse'].astype(str)
    formatted_verse = verse[['Reference', 'origin_text']]
    if format_ == 'str':
        return formatted_verse.to_string(index=False)
    else:
        return formatted_verse


def verse_search(df, word_list, min_match):
    # match_count_threshold = len(word_list) / 1
    df['match_ratio'] = df['origin_text'].apply(lambda verse: round(((sum(word in set(word_list) for word in set(verse)) / len(word_list)) * 100)), 0)
    filtered_df = df[df['match_ratio'] >= min_match]
    return filtered_df


# Explode the lists into separate rows
# new_df = new_df.explode('origin_text')

# cleaned_exploded = new_df['origin_text'].str.replace('[^\w\s]', '', regex=True)

# cleaned_exploded.to_csv("bible_text_exploded.csv", index=False)
