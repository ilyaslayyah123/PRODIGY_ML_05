# 🍔 Food Recognition & Calorie Estimation

## 🚀 Overview
This is a **Flask-based web application** that recognizes food items from images using a **deep learning model** and estimates their calorie content. The model is trained on the **Food-101 Tiny dataset** and provides an easy-to-use **modern UI** for users to track their dietary intake.

## ✨ Features
✅ **Upload an image** to identify food items  
✅ **Deep Learning Model** for food classification  
✅ **Calorie Estimation** for health tracking  
✅ **Modern UI** with Bootstrap and Glassmorphism effects  
✅ **Real-time Image Preview** before submitting  

## 🛠️ Technologies Used
- **Python** (Flask, TensorFlow, NumPy, PIL)
- **Deep Learning** (CNN Model)
- **Bootstrap 5** (Modern UI)
- **JavaScript** (Image Preview Feature)

## 📂 Dataset Used
We used the **[Food-101 Tiny Dataset](https://www.kaggle.com/datasets/msarmi9/food101tiny)** from Kaggle for training the model.

## 🏗️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/FoodRecognitionApp.git
cd FoodRecognitionApp
```

### 2️⃣ Install Dependencies
```bash
pip install flask tensorflow numpy pillow
```

### 3️⃣ Run the Flask App
```bash
python app.py
```

### 4️⃣ Open in Browser
Go to **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** and start using the app! 🎉

## 📸 Screenshots
### 🎨 Modern UI with Image Upload
![UI Screenshot](static/screenshots/ui.png)

### 🔥 Predictions with Calorie Estimation
![Prediction Screenshot](static/screenshots/prediction.png)

## 🤖 How It Works
1. User uploads a **food image**.
2. The trained **CNN model** predicts the food item.
3. The app fetches **calorie estimates** from a predefined database.
4. The results are **displayed in a user-friendly UI**.

## 📌 Folder Structure
```
FoodRecognitionApp/
│── static/
│   ├── uploads/        # Stores uploaded images
│   ├── screenshots/    # Screenshots for README
│── templates/
│   ├── index.html      # Frontend UI
│── app.py              # Flask Backend
│── food_model.h5       # Trained Deep Learning Model
│── README.md           # Project Documentation
```

## 🤝 Contributing
Contributions are welcome! Feel free to **fork** this repository and submit a **pull request**.

## 📜 License
This project is **open-source** under the **MIT License**.

---
### ⭐ If you like this project, don't forget to **star** the repository!
Happy Coding! 🚀

