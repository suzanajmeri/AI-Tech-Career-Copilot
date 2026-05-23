#backend.py file

# ----- Career mappings -----
career_map = {
    "python": ["AI Engineer", "Data Scientist", "Backend Developer", "Python Developer"],
    "sql": ["Data Analyst", "BI Engineer", "Database Engineer"],
    "react": ["Frontend Developer", "Fullstack Developer"],
    "ai": ["AI Engineer", "Research Engineer"],
    "ml": ["ML Engineer", "AI Engineer"],
    "java": ["Java Developer", "Backend Engineer", "Android Developer"],
    "javascript": ["Frontend Developer", "Fullstack Developer", "Web Developer"],
    "c++": ["C++ Developer", "Game Developer", "Embedded Systems Engineer"],
    "c": ["C Developer", "Embedded Systems Engineer"],
}

# ----- Roadmaps -----
roadmaps = {
    "data scientist": [
        {"step": "Master Python & SQL"},
        {"step": "Statistics & Exploratory Data Analysis"},
        {"step": "Machine Learning Algorithms"},
        {"step": "Feature Engineering & Model Selection"},
        {"step": "Portfolio projects & Kaggle"},
        {"step": "Deploy models & cloud basics"}
    ],
    "ai engineer": [
        {"step": "Learn Python & ML basics"},
        {"step": "Deep Learning frameworks (TensorFlow, PyTorch)"},
        {"step": "NLP & Computer Vision"},
        {"step": "MLOps & deployment"},
        {"step": "Build AI projects & publish"}
    ],
    "frontend developer": [
        {"step": "Learn HTML, CSS, JavaScript"},
        {"step": "Master React or Angular"},
        {"step": "Responsive Design & UX"},
        {"step": "Version Control (Git)"},
        {"step": "Build portfolio projects"}
    ],
    "backend developer": [
        {"step": "Learn Python/Java/Node.js"},
        {"step": "Databases (SQL/NoSQL)"},
        {"step": "APIs & Microservices"},
        {"step": "Authentication & Security"},
        {"step": "Deploy apps to cloud"}
    ]
}

# ----- Learning resources -----
resources_map = {
    "python": [
        ("Official Python Docs", "https://docs.python.org/3/"),
        ("GeeksforGeeks Python", "https://www.geeksforgeeks.org/python-programming-language/"),
        ("W3Schools Python", "https://www.w3schools.com/python/"),
        ("TutorialsPoint Python", "https://www.tutorialspoint.com/python/index.htm")
    ],
    "java": [
        ("Oracle Java Docs", "https://docs.oracle.com/javase/tutorial/"),
        ("GeeksforGeeks Java", "https://www.geeksforgeeks.org/java/"),
        ("W3Schools Java", "https://www.w3schools.com/java/"),
        ("TutorialsPoint Java", "https://www.tutorialspoint.com/java/index.htm")
    ],
    "sql": [
        ("SQL Tutorial W3Schools", "https://www.w3schools.com/sql/"),
        ("GeeksforGeeks SQL", "https://www.geeksforgeeks.org/sql-tutorial/"),
        ("TutorialsPoint SQL", "https://www.tutorialspoint.com/sql/index.htm")
    ],
    "react": [
        ("React Official Docs", "https://react.dev/"),
        ("GeeksforGeeks React", "https://www.geeksforgeeks.org/reactjs-tutorials/"),
        ("W3Schools React", "https://www.w3schools.com/react/"),
        ("TutorialsPoint React", "https://www.tutorialspoint.com/reactjs/index.htm")
    ],
    "ai": [
        ("Hugging Face Course", "https://huggingface.co/course"),
        ("GeeksforGeeks AI", "https://www.geeksforgeeks.org/artificial-intelligence/"),
        ("TutorialsPoint AI", "https://www.tutorialspoint.com/artificial_intelligence/index.htm")
    ],
    "ml": [
        ("Scikit-Learn Docs", "https://scikit-learn.org/stable/user_guide.html"),
        ("GeeksforGeeks ML", "https://www.geeksforgeeks.org/machine-learning/"),
        ("TutorialsPoint ML", "https://www.tutorialspoint.com/machine_learning/index.htm")
    ],
    "javascript": [
        ("MDN JavaScript Docs", "https://developer.mozilla.org/en-US/docs/Web/JavaScript"),
        ("GeeksforGeeks JavaScript", "https://www.geeksforgeeks.org/javascript/"),
        ("W3Schools JavaScript", "https://www.w3schools.com/js/"),
        ("TutorialsPoint JavaScript", "https://www.tutorialspoint.com/javascript/index.htm")
    ],
    "c++": [
        ("C++ Reference", "https://en.cppreference.com/w/"),
        ("GeeksforGeeks C++", "https://www.geeksforgeeks.org/c-plus-plus/"),
        ("W3Schools C++", "https://www.w3schools.com/cpp/"),
        ("TutorialsPoint C++", "https://www.tutorialspoint.com/cplusplus/index.htm")
    ],
    "c": [
        ("GeeksforGeeks C", "https://www.geeksforgeeks.org/c-programming-language/"),
        ("W3Schools C", "https://www.w3schools.com/c/"),
        ("TutorialsPoint C", "https://www.tutorialspoint.com/cprogramming/index.htm")
    ]
}

# ----- Functions -----
def get_careers(skills: str):
    """Return careers with skill info instead of 'Matches your skill'."""
    careers = []
    for skill in skills.lower().split(","):
        skill = skill.strip()
        if skill in career_map:
            for career in career_map[skill]:
                careers.append({
                    "career": career,
                    "feature": f"skill is {skill}"
                })
    return careers

def get_roadmap(career: str):
    """Return roadmap steps for a given career."""
    return roadmaps.get(career.lower(), [{"step": "No roadmap available"}])

def explore_skill(skill: str):
    """Return careers and resources for a given skill."""
    return {
        "careers": career_map.get(skill.lower(), []),
        "resources": resources_map.get(skill.lower(), [])
    }

def process_chat(message: str):
    """Simple chatbot logic for career, roadmap, and skill explorer."""
    msg = message.lower()
    if msg.startswith("career for"):
        skill = msg.replace("career for", "").strip()
        careers = get_careers(skill)
        return "\n".join([f"{c['career']} ({c['feature']})" for c in careers]) or "No careers found."
    elif msg.startswith("roadmap for"):
        career = msg.replace("roadmap for", "").strip()
        steps = get_roadmap(career)
        return "\n".join([f"Step {i+1}: {s['step']}" for i, s in enumerate(steps)])
    elif msg.startswith("explore"):
        skill = msg.replace("explore", "").strip()
        data = explore_skill(skill)
        careers = ", ".join(data["careers"]) or "No careers"
        resources = ", ".join([r[0] for r in data["resources"]]) or "No resources"
        return f"Careers: {careers}\nResources: {resources}"
    else:
        return "Hello ! I'm TechPilot AI. Tell me your skills like 'python, sql' or ask 'roadmap for ai engineer'."