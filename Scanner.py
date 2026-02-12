import string

# ==========================================
# 1. PASTE YOUR DATA HERE
# ==========================================

# Paste the Job Description between the triple quotes
JOB_DESCRIPTION = """
We are looking for a Data Analyst with strong Python skills.
Experience with SQL and Tableau is required.
The candidate should be familiar with Machine Learning concepts
and data visualization tools like Matplotlib.
Must have good communication skills and problem-solving abilities.
"""

# Paste your Resume text between the triple quotes
MY_RESUME = """
I am a Computer Science student interested in Data Science.
I have built projects using Python and Pandas.
I created a robotic dog using computer vision.
I am a quick learner and hard worker.
"""

# ==========================================
# 2. THE SCANNER LOGIC
# ==========================================

def clean_text(text):
    """
    Converts text to a set of unique, lowercase words 
    without punctuation.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation (replace commas/dots with spaces)
    for char in string.punctuation:
        text = text.replace(char, " ")
        
    # Split into individual words and make unique
    words = set(text.split())
    
    # A small list of "stop words" to ignore (common English words)
    stop_words = {
        "and", "the", "is", "in", "at", "of", "a", "an", "to", "for", 
        "with", "on", "by", "be", "are", "we", "you", "that", "it", 
        "this", "or", "as", "if", "from", "can", "have", "has", "had",
        "candidate", "looking", "skills", "experience", "required", 
        "should", "familiar", "must", "good", "abilities", "tools", "like"
    }
    
    # Remove stop words from our set
    meaningful_words = words - stop_words
    return meaningful_words

def scan_resume(job_desc, resume):
    print("--- 🔍 STARTING SCAN ---")
    
    jd_words = clean_text(job_desc)
    resume_words = clean_text(resume)
    
    # Calculate the intersection (words in both)
    matched_words = jd_words.intersection(resume_words)
    
    # Calculate the missing words (words in JD but NOT in Resume)
    missing_words = jd_words - resume_words
    
    # Calculate score
    match_score = len(matched_words) / len(jd_words) * 100
    
    print(f"\n✅ Match Score: {match_score:.1f}%")
    print(f"📊 Found {len(matched_words)} matching keywords.")
    print(f"❌ Missing {len(missing_words)} keywords.")
    
    print("\n⚠️  CRITICAL MISSING KEYWORDS:")
    print("-----------------------------")
    # Sort them alphabetically so they are easy to read
    for word in sorted(missing_words):
        print(f" - {word.upper()}")

# ==========================================
# 3. RUN THE SCANNER
# ==========================================
if __name__ == "__main__":
    scan_resume(JOB_DESCRIPTION, MY_RESUME)