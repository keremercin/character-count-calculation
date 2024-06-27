import pandas as pd

# Function to read an Excel file and calculate the total character count
def calculate_total_characters(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Combine all texts in the 'text' column
    all_texts = ''.join(df['text'])

    # Find the total character count
    total_character_count = len(all_texts)

    return total_character_count

if __name__ == "__main__":
    file_path = "path/to/your/excel/file.xlsx"  # Change this to the path of your Excel file
    total_characters = calculate_total_characters(file_path)
    print("Total character count:", total_characters)
