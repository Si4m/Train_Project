
** How to Run This Project (First Time Setup)**

Follow these steps to run the project for the first time:

 1.Install Python

Make sure Python is installed on your computer.

Check version:

python --version

If not installed, download from:
https://www.python.org/


---

2. Create a Virtual Environment (Recommended)

python -m venv venv

Activate the virtual environment:

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate


---

3. Install Required Libraries

Run this command to install dependencies:

pip install tensorflow numpy


---

4. Prepare Your Files

Make sure these files are in the same folder:

test_model.py
train_detection_model.keras
test_image.jpg

Your folder should look like this:

Train_Project/
├── test_model.py
├── train_detection_model.keras
└── test_image.jpg


---

5. Run the Code

Now run the script using:

python test_model.py


---
* Expected Output*


This is NOT a train :
<img width="1575" height="863" alt="Screenshot 2025-12-02 235137" src="https://github.com/user-attachments/assets/2d2c3a97-6238-47b3-ad37-bdd215580790" />


This is a TRAIN :
<img width="1569" height="1039" alt="Screenshot 2025-12-02 234927" src="https://github.com/user-attachments/assets/924ef3cd-3a66-4df8-98a3-b6a65b8f9fa3" />
