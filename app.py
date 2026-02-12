import streamlit as st
from pypdf import PdfReader

# ==========================================
# 1. THE ROLE DATABASE
# ==========================================
ROLE_DB = {
    "Data Analyst": {
        "sql", "excel", "tableau", "powerbi", "python", "r", "statistics", 
        "data visualization", "cleaning", "modeling", "sas", "spss"
    },
    "Data Scientist": {
        "python", "r", "sql", "machine learning", "deep learning", "nlp", 
        "tensorflow", "keras", "pytorch", "scikit-learn", "pandas", "numpy", 
        "statistics", "big data", "spark", "hadoop"
    },
    "Web Developer (Frontend)": {
        "html", "css", "javascript", "react", "angular", "vue", "typescript", 
        "bootstrap", "tailwind", "figma", "git", "responsive design", "ui/ux"
    },
    "Web Developer (Backend)": {
        "python", "java", "node", "express", "django", "flask", "sql", "nosql", 
        "mongodb", "postgresql", "docker", "kubernetes", "aws", "api", "rest"
    },
    "Software Engineer": {
        "java", "c++", "python", "c#", "algorithms", "data structures", 
        "system design", "git", "agile", "sdlc", "testing", "debugging", "oop"
    },
    "Mechanical Engineer": {
        "solidworks", "autocad", "ansys", "catia", "matlab", "thermodynamics", 
        "fluid mechanics", "fea", "cad", "cam", "manufacturing", "prototyping"
    },
    "Civil Engineer": {
        "autocad", "civil 3d", "staad pro", "revit", "etabs", "structural analysis", 
        "surveying", "concrete", "steel", "project management", "estimation"
    },
    "Electrical Engineer": {
        "matlab", "simulink", "pcb design", "altium", "plc", "scada", "vlsi", 
        "verilog", "c", "embedded systems", "circuit design", "autocad"
    },
    "Digital Marketer": {
        "seo", "sem", "google analytics", "google ads", "social media", 
        "content marketing", "email marketing", "copywriting", "wordpress", "crm"
    },
    "Project Manager": {
        "agile", "scrum", "kanban", "jira", "confluence", "risk management", 
        "budgeting", "stakeholder management", "communication", "leadership", "pmp"
    }
}

# ==========================================
# 2. HELPER FUNCTION: READ PDF
# ==========================================
def read_pdf(uploaded_file):
    """
    Extracts text from a PDF file object
    """
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""  # Handle None returns
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

# ==========================================
# 3. THE UI SETUP
# ==========================================
st.set_page_config(page_title="Universal Resume Scanner", page_icon="🌎")

st.title("🌎 Universal Resume Scanner")
st.markdown("Select your target role, **upload your PDF resume**, and let the AI tell you what you're missing.")

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Select Target Role")
    selected_role = st.selectbox(
        "Which job are you applying for?",
        options=list(ROLE_DB.keys())
    )
    st.info(f"Looking for **{len(ROLE_DB[selected_role])}** standard skills.")

with col2:
    st.subheader("2. Upload Resume")
    # <--- THE NEW FILE UPLOADER
    uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

# ==========================================
# 4. THE LOGIC
# ==========================================
if st.button("Analyze Resume 🚀"):
    if not uploaded_file:
        st.warning("⚠️ Please upload a PDF file first!")
    else:
        # Extract text from the uploaded PDF
        resume_text = read_pdf(uploaded_file)
        
        if not resume_text.strip():
            st.error("Could not extract text from this PDF. Please try a different file.")
        else:
            # Get the required skills for the selected role
            required_skills = ROLE_DB[selected_role]
            
            # --- SKILL EXTRACTION LOGIC ---
            found_skills = set()
            resume_lower = resume_text.lower()
            
            # Clean punctuation for better matching
            import string
            for char in string.punctuation:
                resume_lower = resume_lower.replace(char, " ")
            
            # Check for each target skill
            for skill in required_skills:
                # Add spaces around skill to match whole words only
                if f" {skill} " in f" {resume_lower} ":
                    found_skills.add(skill)
            
            # Calculate missing skills
            missing_skills = required_skills - found_skills
            
            # Calculate Score
            score = (len(found_skills) / len(required_skills)) * 100
            
            # --- DISPLAY RESULTS ---
            st.divider()
            st.header("Analysis Results")
            
            # Progress Bar
            st.subheader(f"Match Score: {score:.0f}%")
            st.progress(min(score / 100, 1.0))
            
            # Columns for detailed lists
            c1, c2 = st.columns(2)
            
            with c1:
                st.success(f"✅ YOU HAVE ({len(found_skills)})")
                if len(found_skills) > 0:
                    for skill in sorted(found_skills):
                        st.write(f"🟢 {skill.upper()}")
                else:
                    st.write("No matching skills found.")
                    
            with c2:
                st.error(f"❌ MISSING SKILLS ({len(missing_skills)})")
                if len(missing_skills) > 0:
                    for skill in sorted(missing_skills):
                        st.write(f"🔴 **{skill.upper()}**")
                else:
                    st.balloons()
                    st.write("🎉 You have all the core skills!")