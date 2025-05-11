# 📧 AI-powered Mail Classifier

# 📊 Project Presentation

You can view the project presentation made by my friend and who we participated in Hackathon with here:  
[➡️ View on Google Drive](https://drive.google.com/drive/folders/1NEsrLmmiVfk5lY2MIW05IJMtqDfj-VLY?usp=drive_link)

---


## 📚 Overview

This project is designed to classify and process email data stored in JSON format. It uses HTML parsing, data transformation, and optional OpenAI-based classification to organize emails into a structured format. The project includes scripts for Gmail API integration, data loading, and content transformation.

## 🗂️ Project Structure

```
AI-powered_Mail_Classifier/
├── another.py         # 🔐 Gmail API authentication and token management
├── gettingJson.py     # 📥 Loads and parses raw email data from stuff.json
├── json_creator.py    # 🛠 Converts HTML content to plain text and saves as JSON
├── logics.py          # 🤖 Contains logic for processing emails, may include OpenAI
├── mails.json         # 📄 Sample input email data
├── newMails.json      # 🧪 Intermediate processed data
├── stuff.json         # 📦 Raw input data
└── .gitignore         # 🚫 Git ignored files
```

## ⚙️ Dependencies

- `google-auth`
- `google-auth-oauthlib`
- `google-api-python-client`
- `beautifulsoup4`
- `html2text`
- *(optional)* `openai`

Install them with:

```bash
pip install google-auth google-auth-oauthlib google-api-python-client beautifulsoup4 html2text openai
```

## 🚀 How to Use

1. Make sure your email data exists in `stuff.json` or `mails.json`.
2. Run the scripts in sequence:

```bash
python gettingJson.py     # Step 1: Load and clean JSON email data
python json_creator.py    # Step 2: Convert HTML to text and structure it
python logics.py          # Step 3: Process emails (logic or OpenAI)
```

3. Output will be saved in files like `newMails.json` or `stuff.json`.

## 🔐 Gmail Integration

The `another.py` script uses Google's OAuth2 flow:
- Requires a `credentials.json` file from Google Cloud Console.
- Generates `token.json` after first-time authentication.
- SCOPES used include Gmail read access.

## 📝 Notes

- File paths in scripts may need adjusting to your system.
- Gmail access requires manual API setup.
- OpenAI functionality in `logics.py` may be incomplete or require your API key.

## 👤 Author

Project contents derived directly from submitted source code. No external assumptions added.
