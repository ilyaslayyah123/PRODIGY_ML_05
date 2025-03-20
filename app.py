from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

model = tf.keras.models.load_model("food_model.h5")

food_classes = ["apple_pie", "baby_back_ribs", "baklava", "beef_carpaccio", "beef_tartare", "beet_salad", "beignets",
                "bibimbap", "bread_pudding", "breakfast_burrito", "bruschetta", "caesar_salad", "cannoli", "caprese_salad",
                "carrot_cake"]

calorie_dict = {
    "apple_pie": 265, "baby_back_ribs": 320, "baklava": 330, "beef_carpaccio": 150,
    "beef_tartare": 220, "beet_salad": 90, "beignets": 450, "bibimbap": 210,
    "bread_pudding": 290, "breakfast_burrito": 305, "bruschetta": 170,
    "caesar_salad": 160, "cannoli": 425, "caprese_salad": 140, "carrot_cake": 330
}

def preprocess_image(image_path):
    """Preprocess image for prediction."""
    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    calories = None

    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_path = "static/uploads/" + image_file.filename
            image_file.save(image_path)

            img = preprocess_image(image_path)
            predictions = model.predict(img)
            class_index = np.argmax(predictions)
            food_name = food_classes[class_index]

            estimated_calories = calorie_dict.get(food_name, "Unknown")

            return render_template("index.html", prediction=food_name, calories=estimated_calories, image_path=image_path)

    return render_template("index.html", prediction=prediction, calories=calories, image_path=None)

if __name__ == "__main__":
    os.makedirs("static/uploads", exist_ok=True)
    app.run(debug=True)
