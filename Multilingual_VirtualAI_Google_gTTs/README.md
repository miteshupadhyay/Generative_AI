# Virtual Multilingual Assitant using Google Gemini Pro and gTTs

This is the simple Virtual Assistant System using Google Gemini Pro and Google Text to Speech API .
you need to pass GOOGLE_API_KEY inside .env file.

# 1. create the virtual enviroment

conda create -p mltlnglenv python=3.11 -y

# 2. Activate the virtual environment

conda activate mltlnglenv

# 3. Install requirements

pip install -r requirements.txt

# 4. Run Template.py
python template.py 

# 5. Please Replace the Google API Key in env file

# 6. Run the file
streamlit run app.py
