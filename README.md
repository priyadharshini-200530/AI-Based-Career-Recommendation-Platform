# AI-Based Career Recommendation Platform

A rule-based career recommendation web app built with Python and Streamlit. Users rate themselves on 4 core skills, and the app recommends the top 3 best-matching career paths along with a personalized roadmap and learning resources for each.

## How It Works

The app scores the user's self-rated skills (Communication, Programming, Academics, Mathematics) against weighted skill profiles for 10 different career paths. Each career has a "weight vector" — for example, Data Scientist weighs Mathematics and Programming heavily, while Digital Marketing weighs Communication heavily. The match percentage is calculated as a weighted score against each profile, and the top 3 highest-matching careers are displayed.

## Features

- Interactive skill self-assessment using sliders
- Match percentage scoring across 10 career paths
- Personalized roadmap (step-by-step guidance) for each recommended career
- Curated learning resources (courses, books, YouTube channels) per career

## Tech Stack

- Python 3.10
- Streamlit

## Setup & Running Locally

```bash
git clone https://github.com/priyadharshini-200530/ai-career-recommendation-platform.git
cd ai-career-recommendation-platform

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

## Project Structure

```
ai-career-recommendation-platform/
├── app.py
├── requirements.txt
└── README.md
```

## Future Improvements

- Replace rule-based scoring with a trained ML classification model
- Add more skill dimensions (creativity, leadership, technical writing)
- Allow users to save/export their recommendation report as a PDF
- Add more career profiles

## Author

**Bandi Priyadharshini** — [GitHub](https://github.com/priyadharshini-200530)
