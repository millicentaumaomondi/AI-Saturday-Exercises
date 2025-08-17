import pandas as pd

def read_dataset(file_path):
    try:
        # Load the dataset
        data = pd.read_csv(file_path)
        
        # Display the first few rows of the dataset
        print("First 5 rows of the dataset:")
        print(data.head())
        
        # Display basic information about the dataset
        print("\nBasic information about the dataset:")
        print(data.info())
        
        # Display summary statistics
        print("\nSummary statistics:")
        print(data.describe())
        
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: Error parsing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Specify the path to your dataset
    file_path = '/Users/millicentomondi/Documents/web_scarping_exercise/scraped_quotes.csv'  # Change this to your CSV file path
    read_dataset(file_path)