import pandas as pd
import functions as tools
import gpt_service as gpt

main_csv_path = r"C:\Users\havok\OneDrive\Python Projects\Data Science (general)\Datasets\the_bible\cleaned\verseID_map.csv"
cf_csv_path = r"C:\Users\havok\OneDrive\Python Projects\Data Science (general)\Datasets\the_bible\cleaned\cf_all_merged.csv"

bible_df = pd.read_csv(main_csv_path)
crossref_df = pd.read_csv(cf_csv_path)

# EXAMPLE return
# Enter a verse id in format book-chapter-verse (John 3:16 = 43 003 016)
# convert a verse ID into verse reference
reference = tools.id_to_reference(bible_df, 43003016)
print(reference)

# EXAMPLE find cross references
reference_id = tools.reference_to_id(crossref_df, "John", 3, 16)
cross_refs = tools.find_cross_references(crossref_df, reference_id)
result = cross_refs[['Book_Name', 'Chapter', 'Verse', 'origin_text']]
result.head()

# EXAMPLE find matching verses given word list
word_list = ["Jacob", "mercy", "love"]
results = tools.verse_search(bible_df, word_list)
print(results)

# EXAMPLE using ChatGPT
gpt = gpt.GPTService

prompt = f"What insights can you provide regarding the cross references to the main verse. What kind of themes and " \
         f"relationships are there?: {str(bible_results)}"

response = gpt.prompt(prompt)

print(response)
