# 📄 AI Resume Scanner

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://resume-scanner-ai-cmh538cgwso83kyvw5k2uq.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-green)

A smart, AI-powered tool designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). This application analyzes resumes against job-specific keywords to identify missing skills and improve approval chances.

**🔴 [Live Demo](https://resume-scanner-ai-cmh538cgwso83kyvw5k2uq.streamlit.app)**

---

## 🚀 Features

* **Universal Role Support:** Pre-configured skill databases for **Data Analysts, Software Engineers, Web Developers (Frontend/Backend), Digital Marketers, Mechanical Engineers**, and more.
* **PDF Support:** Directly upload your resume in PDF format.
* **Smart Parsing:** Uses `pypdf` to extract text and analyze content.
* **Instant Feedback:**
    * **Match Score:** A percentage score indicating how well your resume fits the role.
    * **Missing Keywords:** Identifies exactly which hard skills (e.g., SQL, React, Tableau) are missing.
    * **Profile Summary:** Detects and lists the skills you successfully included.
* **Privacy First:** All processing happens in-memory; no resumes are stored.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (for the web interface)
* **Backend:** Python
* **Libraries:**
    * `streamlit` - UI Framework
    * `pypdf` - PDF Parsing
    * `pandas` (Optional for future data handling)

---

## ⚙️ Installation & Local Setup

Want to run this on your own machine? Follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/rohitkr2005/resume-scanner-ai.git](https://github.com/rohitkr2005/resume-scanner-ai.git)
cd resume-scanner-ai

```

**2. Create a Virtual Environment (Optional but Recommended)**

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

```

**3. Install Dependencies**

```bash
pip install -r requirements.txt

```

**4. Run the App**

```bash
streamlit run app.py

```

The app will launch in your browser at `http://localhost:8501`.

---

## 📂 Project Structure

```
resume-scanner-ai/
├── app.py                # Main application logic
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
└── .gitignore           # Files to ignore in Git

```

---

## 🤝 Contributing

Contributions are welcome! If you want to add more job roles or improve the keyword matching algorithm:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/NewRole`).
3. Add your changes (e.g., update `ROLE_DB` in `app.py`).
4. Commit your changes (`git commit -m 'Added DevOps role'`).
5. Push to the branch (`git push origin feature/NewRole`).
6. Open a Pull Request.

---

## 📜 License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.

---

Made with ❤️ by [Rohit Kumar](https://www.google.com/search?q=https://github.com/rohitkr2005)
