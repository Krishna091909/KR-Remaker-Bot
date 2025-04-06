from flask import Flask, render_template, request
import os
from face_swap import swap_faces

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        face = request.files["face"]
        target = request.files["target"]
        face_path = os.path.join(UPLOAD_FOLDER, face.filename)
        target_path = os.path.join(UPLOAD_FOLDER, target.filename)
        face.save(face_path)
        target.save(target_path)

        result_path = swap_faces(face_path, target_path)
        return render_template("result.html", result_image=result_path)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
