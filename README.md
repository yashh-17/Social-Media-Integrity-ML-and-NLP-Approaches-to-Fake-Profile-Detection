# Social-Media-Integrity-ML-and-NLP-Approaches-to-Fake-Profile-Detection
This project is a Fake Account Detector developed using Flask, Keras, and machine learning. The system is designed to identify fake accounts on social media or websites by analyzing patterns and user behavior data. It uses a trained machine learning model (saved as a .keras file) to make predictions based on user input.


---

## **🚀 Step-by-Step Guide to Set Up & Run Your Project**

### **1️⃣ Navigate to Your Project Directory**  
Make sure you're in the right directory before running commands:  
```powershell
cd C:\github\Social-Media-Integrity-ML-and-NLP-Approaches-to-Fake-Profile-Detection
```

---

### **2️⃣ Create and Activate a Virtual Environment**  
If you haven’t set up a virtual environment yet, do it now:  
```powershell
python -m venv venv
venv\Scripts\activate  # On Windows
```

> ✅ **Make sure your virtual environment is activated** (you should see `(venv)` in the terminal).

---

### **3️⃣ Upgrade `pip` (to avoid outdated dependencies issues)**
```powershell
python -m pip install --upgrade pip
```

---

### **4️⃣ Manually Install Key Dependencies First**  
Installing these first helps prevent version conflicts:  
```powershell
pip install flask pandas numpy tensorflow scikit-learn gender-guesser
```

---

### **5️⃣ Fix `requirements.txt` (If Needed)**
- If `requirements.txt` contains **`astropy==7.0.0`**, replace it with:
  ```plaintext
  astropy==6.1.7
  ```
- Save the file before proceeding.

---

### **6️⃣ Install the Remaining Dependencies**  
Once core packages are installed, install the rest:  
```powershell
pip install -r requirements.txt
```

---

### **7️⃣ Verify Installation**  
Check if all required packages are installed:  
```powershell
pip list
```
✅ **Make sure the following are installed:**  
- `Flask`  
- `pandas`  
- `numpy`  
- `tensorflow`  
- `scikit-learn`  
- `gender-guesser`  

---

### **8️⃣ Run the Application**  
Now, navigate to the backend directory and start the app:  
```powershell
cd backend
python app.py
```

---

## **🔧 Troubleshooting Common Issues**
### **🚨 ModuleNotFoundError (If any package is missing)**
If you get an error like `ModuleNotFoundError: No module named 'X'`, install it manually:  
```powershell
pip install X  # Replace 'X' with the missing module name
```

### **🚨 TensorFlow Compatibility Issues**
If TensorFlow is causing problems, install a stable version:  
```powershell
pip install tensorflow==2.10.0
```

### **🚨 Clean Virtual Environment (If issues persist)**
If things are still broken, try starting fresh:  
```powershell
rmdir /s /q venv  # Deletes existing venv (Windows)
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install flask pandas numpy tensorflow scikit-learn gender-guesser
pip install -r requirements.txt
```

---

## **🎯 Final Notes**
- **Always activate the virtual environment before running `app.py`.**  
- **Keep `requirements.txt` updated** with the correct versions of dependencies.  
- **If facing issues, check the error logs and install missing dependencies manually.**  

---
