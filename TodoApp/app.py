from flask import render_template, request, Flask, flash, redirect, url_for
from databases import DB

db = DB()

app = Flask(__name__, static_folder="static")
app.secret_key = b'_5#y2L27834828734872387_=(/77)"F4Q8z\n\xec]/'


@app.route("/")
def index():
    result = db.getTotalContent()
    return render_template("index.html", totalTask = result)

@app.route("/add", methods=["GET","POST"])
def addData():
    if request.method == "POST":
        __title = request.form.get("title")
        __content = request.form.get("content")
        db.addData(title=__title, content=__content)
        
        return redirect(url_for("index"))
    
    else:
        return redirect(url_for("index"))
    
    
@app.route("/delete/<int:id>")
def delete(id):
    db.delete(idTask=id)
    return redirect(url_for("index"))



@app.route("/details/<int:id>", methods=["GET","POST"])
def details(id):
       
    query = db.queryIdNumber(Id=id)
    if query:
        if query[0]:
            if id == query[0]:
                return render_template("details.html", query=query)
            
    else:        
        return redirect(url_for("index"))

    
@app.route('/update', methods=["GET","POST"])
def update():
    if request.method == "POST":
        title = request.form.get("titles")
        content = request.form.get("contents")
        ids = request.form.get("taskid")
        
        db.update(id=ids, title=title,content=content)
        return redirect(url_for("index"))
    
    
if __name__ == "__main__":
    app.run(debug=True)