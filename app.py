from flask import Flask, render_template
import json

app = Flask(__name__)


with open("data.json") as file:
    data = json.load(file)


def write_data():
    with open("data.json", "w") as file:
        json.dump(data, file)


@app.route("/", methods=["GET"])
def get_list():
    return render_template("main.jinja", items=data)


@app.route("/delete/<num>", methods=["GET"])
def delete_item(num):
    num = int(num)
    item = data[num]
    del data[num]

    write_data()

    return render_template("main.jinja", items=data)


@app.route("/create/<name>")
def create_item(name):
    data.append(name)

    write_data()

    return render_template("main.jinja", items=data)


if __name__ == "__main__":
    app.run(debug=True)