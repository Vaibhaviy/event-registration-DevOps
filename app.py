from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        event = request.form["event"]

        return f"""
        <h2>Registration Successful!</h2>
        <p>Name: {name}</p>
        <p>Email: {email}</p>
        <p>Event: {event}</p>
        """

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)