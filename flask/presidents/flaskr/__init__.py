from flask import Flask, render_template
from .modules import make_ordinal, convert_to_dict, presidency_president_pairs_list

app = Flask(__name__, template_folder="templates")
pres_list = convert_to_dict("../presidents/presidents.csv")

@app.route("/")
def index():
    return render_template("index.html", 
                           pairs=presidency_president_pairs_list(pres_list),
                           the_title="Presidents Index")

@app.route("/user/<name>")
def user(name):
    return render_template("hello.html", name=name)

@app.route("/president/<num>")
def detail(num):
    try:
        pres_dict = pres_list[int(num)-1]
    except:
        return f"<h1>Invalid value for presidency: {num}</h1>"
    ord_num = make_ordinal(int(num))
    return render_template("president.html", pres=pres_dict, 
                            ord=ord_num, the_title=pres_dict["President"])

if __name__ == "__main__":
    app.run(debug=True)