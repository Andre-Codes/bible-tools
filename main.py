import pandas as pd
import functions as tools
import gpt_service as gpt

csv_path = r"C:\Users\havok\OneDrive\Python Projects\Data Science (general)\Datasets\the_bible\cleaned\verseID_map.csv"

bible_df = pd.read_csv(csv_path)
bible_df.head()

# EXAMPLE return
# Enter a verse id in format book-chapter-verse (John 3:16 = 43 003 016)
# convert a verse ID into verse reference
reference = tools.id_to_reference(bible_df, 40003010)
print(reference)

# EXAMPLE find cross references
reference_id = tools.reference_to_id(bible_df, "Job", 6, 7)
cross_refs = tools.find_cross_references(bible_df, reference_id, format="clean")
bible_results = f"Main verse:\n{cross_refs[0]}\n\nCross references:\n{cross_refs[1]}"
print(bible_results)

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
