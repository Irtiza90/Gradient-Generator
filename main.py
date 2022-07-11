from os.path import join as os_join

from colorthief import ColorThief
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template


app = Flask(__name__)
app.secret_key = "ka2365d4aa8sd7au*oqa4d2e2e54"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/palettes", methods=("GET", "POST"))
def palletes_route():
    f_path = "static/images"

    img_file = request.files['file']
    img_file.save(os_join(f_path, secure_filename(img_file.filename)))
    img_path = f"{f_path}/{img_file.filename}"

    colors = ColorThief(img_path)
    color_palette = colors.get_palette()

    return render_template("palettes.html", img_path=img_path, palette=color_palette)


if __name__ == "__main__":
    app.run(debug=True)
