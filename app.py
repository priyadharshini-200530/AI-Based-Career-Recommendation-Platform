import streamlit as st

st.set_page_config(page_title="AI Career Recommendation Platform", page_icon="🎯", layout="centered")

# ---------------------------------------------------------
# CAREER PROFILE DATA
# Each career has a weight vector on 4 skills:
# communication, programming, academics, mathematics (scale 0-10)
# Higher weight = that skill matters more for this career
# ---------------------------------------------------------

CAREER_PROFILES = {
    "Software Developer": {
        "weights": {"communication": 4, "programming": 10, "academics": 6, "mathematics": 6},
        "roadmap": [
            "Learn a core programming language deeply (Python, Java, or JavaScript)",
            "Build 3-4 real projects (web app, API, or CLI tool) and host them on GitHub",
            "Learn Data Structures & Algorithms",
            "Learn Git/GitHub and basic software development lifecycle",
            "Apply for internships or entry-level developer roles"
        ],
        "resources": [
            "Book: 'Clean Code' by Robert C. Martin",
            "Course: freeCodeCamp - Full Stack Web Development",
            "YouTube: CS50 by Harvard (edX/YouTube)"
        ]
    },
    "QA Automation Engineer": {
        "weights": {"communication": 6, "programming": 7, "academics": 5, "mathematics": 4},
        "roadmap": [
            "Learn manual testing fundamentals (STLC, test case design, defect lifecycle)",
            "Learn Python and Selenium WebDriver basics",
            "Build an automation framework using Page Object Model",
            "Learn pytest/TestNG and CI/CD basics (GitHub Actions/Jenkins)",
            "Build 2-3 portfolio automation projects and publish on GitHub"
        ],
        "resources": [
            "Course: Selenium WebDriver with Python (Udemy)",
            "Book: 'Agile Testing' by Lisa Crispin & Janet Gregory",
            "YouTube: Naveen AutomationLabs"
        ]
    },
    "Data Scientist": {
        "weights": {"communication": 4, "programming": 8, "academics": 8, "mathematics": 10},
        "roadmap": [
            "Build strong foundations in statistics and linear algebra",
            "Learn Python libraries: NumPy, Pandas, Matplotlib, Scikit-learn",
            "Complete 2-3 real-world data analysis projects",
            "Learn SQL for data extraction",
            "Learn basics of Machine Learning algorithms and model evaluation"
        ],
        "resources": [
            "Course: Andrew Ng's Machine Learning (Coursera)",
            "Book: 'Python for Data Analysis' by Wes McKinney",
            "YouTube: StatQuest with Josh Starmer"
        ]
    },
    "Business Analyst": {
        "weights": {"communication": 9, "programming": 3, "academics": 7, "mathematics": 6},
        "roadmap": [
            "Learn business process modeling and requirement gathering techniques",
            "Get comfortable with Excel, SQL basics, and dashboarding tools (Power BI/Tableau)",
            "Practice writing clear Business Requirement Documents (BRDs)",
            "Learn Agile/Scrum methodology basics",
            "Build a portfolio project analyzing a real dataset and presenting insights"
        ],
        "resources": [
            "Course: Business Analytics Specialization (Coursera - Wharton)",
            "Book: 'Business Analysis for Practitioners' (PMI)",
            "YouTube: Analyst Builder"
        ]
    },
    "Digital Marketing Specialist": {
        "weights": {"communication": 10, "programming": 2, "academics": 5, "mathematics": 3},
        "roadmap": [
            "Learn SEO, SEM, and content marketing fundamentals",
            "Get hands-on with Google Analytics and Meta Ads Manager",
            "Run a small real or mock marketing campaign to build a case study",
            "Learn basic copywriting and social media strategy",
            "Get certified: Google Digital Garage / HubSpot Academy"
        ],
        "resources": [
            "Course: Google Digital Garage - Fundamentals of Digital Marketing",
            "Book: 'Contagious' by Jonah Berger",
            "YouTube: Neil Patel"
        ]
    },
    "Teacher / Educator": {
        "weights": {"communication": 10, "programming": 1, "academics": 9, "mathematics": 5},
        "roadmap": [
            "Strengthen subject-matter expertise in your chosen field",
            "Learn instructional design and classroom/online teaching techniques",
            "Practice public speaking and content simplification",
            "Create sample teaching content (videos, notes, or a small course)",
            "Pursue a B.Ed or relevant teaching certification if targeting formal education roles"
        ],
        "resources": [
            "Course: Coursera - 'Learning How to Learn'",
            "Book: 'Make It Stick' by Peter C. Brown",
            "YouTube: Kurzgesagt (for content simplification style reference)"
        ]
    },
    "Financial Analyst": {
        "weights": {"communication": 6, "programming": 3, "academics": 8, "mathematics": 9},
        "roadmap": [
            "Build strong fundamentals in accounting and financial statements",
            "Learn Excel modeling and valuation techniques",
            "Study for certifications like NCFM or CFA Level 1 (long-term)",
            "Practice analyzing real company financial reports",
            "Learn basic SQL for financial data analysis"
        ],
        "resources": [
            "Course: Corporate Finance Institute (CFI) - Financial Modeling",
            "Book: 'The Intelligent Investor' by Benjamin Graham",
            "YouTube: Aswath Damodaran (NYU Stern)"
        ]
    },
    "Civil Services Officer": {
        "weights": {"communication": 9, "programming": 1, "academics": 10, "mathematics": 5},
        "roadmap": [
            "Build a strong foundation in general studies (history, polity, geography, economy)",
            "Read newspapers daily for current affairs",
            "Practice answer writing for mains-style questions",
            "Choose and prepare an optional subject",
            "Join a structured UPSC/state PSC preparation plan or coaching if needed"
        ],
        "resources": [
            "NCERT textbooks (Class 6-12) as foundation",
            "Newspaper: The Hindu or Indian Express (daily)",
            "YouTube: StudyIQ, Unacademy UPSC channels"
        ]
    },
    "UI/UX Designer": {
        "weights": {"communication": 7, "programming": 4, "academics": 5, "mathematics": 3},
        "roadmap": [
            "Learn design fundamentals: color theory, typography, layout",
            "Learn tools like Figma or Adobe XD",
            "Study UX research and usability testing basics",
            "Redesign 2-3 existing apps/websites as portfolio case studies",
            "Build a portfolio website showcasing your design process"
        ],
        "resources": [
            "Course: Google UX Design Professional Certificate (Coursera)",
            "Book: 'Don't Make Me Think' by Steve Krug",
            "YouTube: The Futur"
        ]
    },
    "Network / Systems Administrator": {
        "weights": {"communication": 5, "programming": 5, "academics": 6, "mathematics": 5},
        "roadmap": [
            "Learn networking fundamentals (TCP/IP, DNS, subnetting)",
            "Get hands-on with Linux administration",
            "Pursue CompTIA Network+ or Cisco CCNA certification",
            "Practice setting up and troubleshooting home lab networks/servers",
            "Learn basic scripting (Bash/Python) for automation tasks"
        ],
        "resources": [
            "Course: CompTIA Network+ (Professor Messer - free YouTube series)",
            "Book: 'Networking All-in-One For Dummies'",
            "YouTube: NetworkChuck"
        ]
    },
}


def get_top_recommendations(user_scores, top_n=3):
    """Score each career profile against the user's self-rated skills and
    return the top N best-matching careers, ranked by match percentage."""
    results = []
    for career, profile in CAREER_PROFILES.items():
        weights = profile["weights"]
        max_possible = sum(w * 10 for w in weights.values())
        actual_score = sum(weights[skill] * user_scores[skill] for skill in weights)
        match_percent = round((actual_score / max_possible) * 100, 1)
        results.append((career, match_percent))

    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_n]


# ---------------------------------------------------------
# STREAMLIT UI
# ---------------------------------------------------------

st.title("🎯 AI-Based Career Recommendation Platform")
st.write(
    "Rate yourself honestly on each skill (1 = beginner, 10 = expert). "
    "Based on your profile, we'll recommend the top 3 career paths that best match your strengths, "
    "along with a roadmap and learning resources for each."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    communication = st.slider("Communication Skills", 1, 10, 5)
    programming = st.slider("Programming Skills", 1, 10, 5)

with col2:
    academics = st.slider("Academic Performance", 1, 10, 5)
    mathematics = st.slider("Mathematics Skills", 1, 10, 5)

user_scores = {
    "communication": communication,
    "programming": programming,
    "academics": academics,
    "mathematics": mathematics,
}

st.divider()

if st.button("🔍 Get My Career Recommendations", use_container_width=True):
    top_matches = get_top_recommendations(user_scores, top_n=3)

    st.subheader("Your Top 3 Career Matches")

    for rank, (career, match_percent) in enumerate(top_matches, start=1):
        with st.expander(f"#{rank} — {career}  ({match_percent}% match)", expanded=(rank == 1)):
            st.progress(match_percent / 100)

            st.markdown("**📍 Roadmap**")
            for step in CAREER_PROFILES[career]["roadmap"]:
                st.markdown(f"- {step}")

            st.markdown("**📚 Learning Resources**")
            for resource in CAREER_PROFILES[career]["resources"]:
                st.markdown(f"- {resource}")

    st.caption(
        "Note: This tool uses a rule-based scoring model comparing your self-rated skills "
        "against weighted skill profiles for each career. It's meant as a starting point for "
        "exploration, not a definitive career decision."
    )

st.divider()
st.caption("Built with Python & Streamlit | Personal Project by Dharshini")
