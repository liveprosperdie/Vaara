from flask import Flask, request

app = Flask(_name_)

@app.route("/")
def home():
    return "Vaara backend is running!"

if _name_ == "_main_":
    app.run(debug=True)
    