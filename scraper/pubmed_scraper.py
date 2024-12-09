#pubmed_scraper.py
import requests
from bs4 import BeautifulSoup

class PubMedScraper:
    def __init__(self):
        self.base_url = "https://pubmed.ncbi.nlm.nih.gov/"
        self.search_base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    def search_papers(self, query, max_results=10):
        """Search PubMed for papers using a keyword query and return PubMed IDs."""
        params = {
            'db': 'pubmed',
            'term': query,  # Search term (e.g., keyword or title)
            'retmax': max_results,  # Maximum number of results
            'retmode': 'xml'  # Return results in XML format
        }
        response = requests.get(self.search_base_url, params=params)
        
        if response.status_code == 200:
            ids = self.parse_ids_from_search(response.text)
            return ids
        else:
            print("Failed to search PubMed.")
            return []

    def parse_ids_from_search(self, xml_data):
        """Parse the PubMed search results to extract the PubMed IDs."""
        ids = []
        start = xml_data.find('<IdList>') + len('<IdList>')  # Locate the start of IdList
        end = xml_data.find('</IdList>')  # Locate the end of IdList
        ids_section = xml_data[start:end]
        ids = [id.strip() for id in ids_section.split('<Id>')[1:]]  # Extract individual IDs

        return ids

    def scrape_paper_data(self, pubmed_id):
        """Fetch paper data from PubMed using PubMed ID"""
        url = f"{self.base_url}{pubmed_id}/"
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = self.extract_title(soup)
            abstract = self.extract_abstract(soup)
            details = {
                "authors": self.extract_authors(soup),
                "journal": self.extract_journal(soup),
                "publication_date": self.extract_pub_date(soup)
            }
            
            return title, abstract, details
        else:
            print(f"Failed to fetch paper with PubMed ID {pubmed_id}")
            return None, None, None

    def extract_title(self, soup):
        """Extract the title of the paper."""
        title_section = soup.find('h1', class_='heading-title')
        return title_section.text.strip() if title_section else "No title available."

    def extract_abstract(self, soup):
        """Extract the abstract of the paper."""
        abstract_section = soup.find('div', class_='abstract-content')
        return abstract_section.text.strip() if abstract_section else "No abstract available."

    def extract_authors(self, soup):
        """Extract authors from the paper page."""
        authors_section = soup.find('div', class_='authors-list')
        authors = authors_section.text.strip() if authors_section else "No authors listed."
        return authors

    def extract_journal(self, soup):
        """Extract journal title from the paper page."""
        journal_section = soup.find('span', class_='journal-title')
        journal = journal_section.text.strip() if journal_section else "No journal available."
        return journal

    def extract_pub_date(self, soup):
        """Extract publication date from the paper page."""
        pub_date_section = soup.find('span', class_='cit')
        pub_date = pub_date_section.text.strip() if pub_date_section else "No publication date."
        return pub_date


# Test Scraper
if __name__ == "__main__":
    scraper = PubMedScraper()

    # Example query
    query = "covid"
    pubmed_ids = scraper.search_papers(query)

    if not pubmed_ids:
        print("No papers found.")
    else:
        for pubmed_id in pubmed_ids[:5]:  # Limit to first 5 papers for testing
            print(f"\nScraping PubMed ID: {pubmed_id}")
            title, abstract, details = scraper.scrape_paper_data(pubmed_id)
            if title:
                print(f"Title: {title}")
                print(f"Abstract: {abstract}")
                print(f"Authors: {details['authors']}")
                print(f"Journal: {details['journal']}")
                print(f"Publication Date: {details['publication_date']}")
