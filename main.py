import pandas as pd
import bible
import gpt_service as gpt

csv_path = r"C:\Users\havok\OneDrive\Python Projects\Bible\datatsets\cleaned\cf_all_merged.csv"

bible_df = pd.read_csv(csv_path)

# Enter a verse id in format book-chapter-verse (John 3:16 = 43 003 016)
bible.find_cross_references(bible_df, 40003010)

reference = bible.id_to_reference(bible_df, 39001001)
print(reference)

reference_id = bible.reference_to_id(bible_df, "Job", 6, 7)
cross_refs = bible.find_cross_references(bible_df, reference_id, format="clean")
bible_results = f"Main verse:\n{cross_refs[0]}\n\nCross references:\n{cross_refs[1]}"

print(bible_results)

gpt = gpt.GPTService

prompt = f"What insights can you provide regarding the cross references to the main verse. What kind of themes and relationships are there?: {str(bible_results)}"

response = gpt.prompt(prompt)

print(response)
