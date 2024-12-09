# scrap_and_summarize.py
from scraper.pubmed_scraper import PubMedScraper
from database.paper_database import PaperDatabase
from summarizer.paper_summarizer import PaperSummarizer

def search_and_summarize_papers(search_query):
    # Initialize components
    scraper = PubMedScraper()
    db = PaperDatabase()
    summarizer = PaperSummarizer()

    # Step 1: Search for papers in PubMed
    pubmed_ids = scraper.search_papers(search_query)
    if not pubmed_ids:
        return None, "No results found on PubMed."

    papers = []
    for pubmed_id in pubmed_ids:
        title, abstract, details = scraper.scrape_paper_data(pubmed_id)

        if db.paper_exists(title):
            print(f"Paper already exists in the database: {title}")
        else:
            embedding = summarizer.embed_paper(title, abstract, details)
            db.store_paper(title, abstract, details, embedding)

        papers.append((title, abstract, details))

    # Step 2: Combine abstracts and summarize
    combined_abstract = "\n\n".join([abstract for _, abstract, _ in papers if abstract != "Abstract Not Found"])
    combined_summary = ""
    if combined_abstract:
        combined_summary = summarizer.summarize_paper("Combined Papers", combined_abstract, {})

    return papers, combined_summary
