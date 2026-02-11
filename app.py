from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        return redirect(url_for("success", name=name))
    return render_template("contact.html")


@app.route("/success")
def success():
    name = request.args.get("name")
    return render_template("success.html", name=name)


if __name__ == "__main__":
    app.run(debug=True, port=5006)
