import pandas as pd
import functions as tools
import gpt_service as gpt

main_csv_path = "/verseID_map.csv"
cf_csv_path = "/cf_all_merged.csv"

bible_df = pd.read_csv(main_csv_path)
crossref_df = pd.read_csv(cf_csv_path)

####################################
# EXAMPLE - convert a verse ID into verse reference

# Enter a verse id in format book-chapter-verse (John 3:16 = 43 003 016)
reference = tools.id_to_reference(bible_df, 43003016)  # Result: ('John', 3, 16, 'John 3:16')

# Convert standard verse reference to its ID
reference_id = tools.reference_to_id(crossref_df, "John", 3, 16)  # result: 43003016

####################################
# FEAT EXAMPLE - find cross-references
cross_refs = tools.find_cross_references(crossref_df, 43003016)
result = cross_refs[['Book_Name', 'Chapter', 'Verse', 'origin_text']]
result.head()

####################################
# FEAT EXAMPLE - find matching verses given word list
verse_search_df = bible_df.copy()  # Copy the unaltered df

# Remove all punctuation
verse_search_df['origin_text'] = verse_search_df['origin_text'].str.replace('[^\w\s]', '', regex=True)

# split verses into list of words
verse_search_df['origin_text'] = verse_search_df['origin_text'].str.split()

# Iterate through list of every row, converting words to lowercase
lower_if_string = lambda verse: [word.lower() if isinstance(word, str) else word for word in verse]
verse_search_df['origin_text'] = verse_search_df['origin_text'].apply(lower_if_string)

# Find verses that contain at least 50% of the words in the list
word_list = ["everlasting", "Israel", "covenant", "God", "seed", "children"]
word_list = list(map(str.lower, word_list))
results = tools.verse_search(verse_search_df, word_list, 50)
results.head()


####################################
###### EXAMPLE using ChatGPT ######
gpt = gpt.GPTService

prompt = f"What insights can you provide regarding the cross references to the main verse. What kind of themes and " \
         f"relationships are there?: {str(bible_results)}"

response = gpt.prompt(prompt)

print(response)
