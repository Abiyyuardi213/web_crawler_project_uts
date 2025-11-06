from flask import Flask, render_template, jsonify, send_from_directory
from crawler import crawl_single, crawl_multi
import os

app = Flask(__name__)

# === route halaman utama ===
@app.route("/")
def index():
    return render_template("index.html")

# === route untuk scraping ===
@app.route("/start", methods=["GET"])
def start_scraping():
    single_results, single_time = crawl_single()
    multi_results, multi_time = crawl_multi()

    # tambahkan nama file hasil scrape agar bisa ditampilkan
    for r in multi_results:
        filename = r["url"].replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
        r["file"] = filename

    return jsonify({
        "single_results": single_results,
        "multi_results": multi_results,
        "single_time": single_time,
        "multi_time": multi_time
    })

# === route untuk menampilkan hasil HTML langsung di browser ===
@app.route("/hasil/<path:filename>")
def serve_html(filename):
    return send_from_directory("hasil_html", filename)

if __name__ == "__main__":
    app.run(debug=True)
