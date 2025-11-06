from flask import Flask, render_template
from crawler import crawl_single, crawl_multi

app = Flask(__name__)

@app.route("/")
def index():
    single_results, single_time = crawl_single()
    multi_results, multi_time = crawl_multi()

    return render_template(
        "index.html",
        single_results=single_results,
        multi_results=multi_results,
        single_time=single_time,
        multi_time=multi_time
    )

if __name__ == "__main__":
    app.run(debug=True)
