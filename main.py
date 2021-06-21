import flask
from flask import Flask, render_template


app = Flask(__name__, static_folder="static", template_folder="src/templates/")



@app.route("/")
def emailSub():
    return render_template("index.html")

# GET - /resource?stock=TSLA&data=FULL
# POST - -d "stock={2010: 195}" -X POST /resource
@app.route("/success", methods=["POST"])
def emailSuccess():
    args = flask.request.form
    email = args.get("email")
    print(email)
    SQLDatabase("emails").write(email)
    return render_template("success.html")




if __name__ == '__main__':
    app.run()
