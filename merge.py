import pandas as pd

bible_text = pd.read_csv(r"C:\Users\havok\OneDrive\Python Projects\Bible\datatsets\cleaned\bible_asv.csv")

bible_cf = pd.read_csv(r"C:\Users\havok\OneDrive\Python Projects\Bible\datatsets\cleaned\cleaned_cross_reference.csv")

bible_text.head()
bible_cf.head()

bible_merged = pd.merge(bible_cf, bible_text, on='Verse_ID')

bible_merged = bible_merged.rename(columns={'Text': 'orign_text'})
bible_merged.to_csv('cf_with_text.csv')

