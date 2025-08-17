import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes(url):
    quotes = []  # List to store quotes
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all quote containers
        quote_elements = soup.find_all('div', class_='quote')
        
        for quote in quote_elements:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
            quotes.append({'text': text, 'author': author, 'tags': tags})  # Append to list
            
            # Print the quote details
            print(f"Quote: {text}\nAuthor: {author}\nTags: {', '.join(tags)}\n")
        
        # Save quotes to CSV
        save_to_csv(quotes, 'scraped_quotes.csv')
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def save_to_csv(quotes, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote', 'Author', 'Tags'])  # Header
        for quote in quotes:
            writer.writerow([quote['text'], quote['author'], ', '.join(quote['tags'])])

def main():
    url = "https://quotes.toscrape.com/"
    scrape_quotes(url)

if __name__ == "__main__":
    main()