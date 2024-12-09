from flask import Flask, render_template, request
from service.scrap_and_summarize import search_and_summarize_papers

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    papers = None
    summary = None
    search_query = None

    if request.method == 'POST':
        search_query = request.form['search_query']
        papers, summary = search_and_summarize_papers(search_query)

    return render_template('index.html', papers=papers, summary=summary, search_query=search_query)

if __name__ == "__main__":
    app.run(debug=True)
