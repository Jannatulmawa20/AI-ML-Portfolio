# modern_portfolio_generator.py


html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jannatul Mawa - AI/ML Developer Portfolio</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #0d6efd;    /* Bootstrap blue */
            --dark: #121212;
            --darker: #0a0a0a;
            --light-text: #e0e0e0;
            --gray: #2d2d2d;
            --accent: #1d8cf8;
        }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--dark);
            color: var(--light-text);
            line-height: 1.7;
        }
        header {
            background: linear-gradient(135deg, var(--darker), #1a1a2e);
            padding: 4rem 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        header::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(circle at center, rgba(13, 110, 253, 0.2), transparent);
        }
        .profile-img {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            border: 5px solid var(--primary);
            object-fit: cover;
            box-shadow: 0 0 30px rgba(13, 110, 253, 0.5);
            position: relative;
            z-index: 1;
        }
        h1 {
            margin: 1rem 0 0.5rem;
            font-size: 2.8rem;
            color: white;
            position: relative;
            z-index: 1;
        }
        .tagline {
            font-size: 1.2rem;
            color: #a0aec0;
            position: relative;
            z-index: 1;
        }
        nav {
            background-color: var(--darker);
            padding: 1rem;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        nav ul {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }
        nav ul li {
            margin: 0.5rem 1rem;
        }
        nav ul li a {
            color: var(--light-text);
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s;
        }
        nav ul li a:hover {
            color: var(--primary);
        }
        section {
            padding: 4rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        h2 {
            color: var(--primary);
            text-align: center;
            margin-bottom: 2.5rem;
            font-size: 2.2rem;
            position: relative;
        }
        h2::after {
            content: '';
            width: 80px;
            height: 4px;
            background: var(--primary);
            display: block;
            margin: 1rem auto 0;
            border-radius: 2px;
        }
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
        }
        .skill-card {
            background: var(--gray);
            padding: 1.8rem;
            border-radius: 12px;
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .skill-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 30px rgba(13, 110, 253, 0.3);
        }
        .skill-card i {
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 1rem;
        }
        .experience-item, .project-card {
            background: var(--gray);
            padding: 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            transition: all 0.3s;
        }
        .experience-item:hover, .project-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 10px 30px rgba(13, 110, 253, 0.2);
        }
        .project-links {
            margin-top: 1.5rem;
        }
        .btn {
            display: inline-block;
            padding: 0.8rem 1.5rem;
            background: var(--primary);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin-right: 1rem;
            font-weight: 600;
            transition: background 0.3s;
        }
        .btn:hover {
            background: #0b5ed7;
        }
        .btn-secondary {
            background: transparent;
            border: 2px solid var(--primary);
        }
        .btn-secondary:hover {
            background: var(--primary);
        }
        footer {
            background: var(--darker);
            color: #888;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }
        .social-links a {
            color: var(--light-text);
            font-size: 1.5rem;
            margin: 0 1rem;
            transition: color 0.3s;
        }
        .social-links a:hover {
            color: var(--primary);
        }
        @media (max-width: 768px) {
            h1 { font-size: 2.2rem; }
            nav ul { flex-direction: column; }
        }
    </style>
</head>
<body>
    <header>
        <img src="images/img.jpg" alt="Jannatul Mawa" class="profile-img">
        <h1>Jannatul Mawa</h1>
        <p class="tagline">AI/ML/DL Developer</p>
    </header>

    <nav>
        <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#experience">Experience</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#education">Education</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <section id="about">
        <h2>About Me</h2>
        <p style="text-align:center; max-width:800px; margin:0 auto; font-size:1.1rem;">
            Motivated Computer Science graduate with hands-on experience in Machine Learning and Deep Learning. 
            Proven ability to develop, train, and evaluate models using Python, TensorFlow, and PyTorch. 
            Passionate about building intelligent systems, especially RAG pipelines and agentic AI.
        </p>
    </section>

    <section id="skills">
        <h2>Skills</h2>
        <div class="skills-grid">
            <div class="skill-card">
                <i class="fab fa-python"></i>
                <h3>Languages</h3>
                <p>Python, JavaScript (Node.js)</p>
            </div>
            <div class="skill-card">
                <i class="fas fa-brain"></i>
                <h3>ML/DL Frameworks</h3>
                <p>TensorFlow, PyTorch, scikit-learn, OpenCV</p>
            </div>
            <div class="skill-card">
                <i class="fas fa-database"></i>
                <h3>Data Tools</h3>
                <p>NumPy, pandas, Git</p>
            </div>
            <div class="skill-card">
                <i class="fas fa-cloud"></i>
                <h3>Cloud & Others</h3>
                <p>AWS (Basic), GitHub</p>
            </div>
            <div class="skill-card">
                <i class="fas fa-cloud"></i>
                <h3>ERP</h3>
                <p>Oracle ERP, odoo, Excel, Power BI, SQL</p>
                <p>Modules: Inventory, Procurement, Sales, Finance, HR</p>

            </div>
        </div>
    </section>

    <section id="experience">
        <h2>Work Experience</h2>
         <div class="experience-item">
            <h3>Intern-ERP</h3>
            <p>2024(2024-Present)</p>
            <ul>
                <li>Managed Purchase & Inventory modules using software ERP</li>
                <li>Automated stock tracking, reducing manual errors by 30%</li>
                <li>Generated vendor-wise purchase and sales reports</li>
                <li>Trained team members on ERP usage</li>
                <li>Supported Accounts & Sales team with ERP workflows</li>
            </ul>
        </div>
        <div class="experience-item">
            <h3>Annotator — Product Sense</h3>
            <p>2024(August to November)</p>
            <ul>
                <li>Annotating datasets to support AI and ML projects</li>
                <li>Ensured high data quality and accuracy for model training</li>
            </ul>
        </div>
        <div class="experience-item">
            <h3>Research Assistant — International Standard University</h3>
            <p>2024 – 2025</p>
            <ul>
                <li>Conducted literature reviews on emerging CS topics</li>
                <li>Assisted in developing and analyzing research models & algorithms</li>
                <li>Supported AI, ML, and data science faculty projects</li>
            </ul>
        </div>
    </section>

    <section id="projects">
        <h2>Projects</h2>

        <div class="project-card">
            <h3>RAG-based Company Policy Chatbot</h3>
            <p>Python • Streamlit • RAG • Vector Search</p>
            <p>Built an intelligent chatbot that answers questions from internal PDF/text documents using embeddings and retrieval-augmented generation with source citations.</p>
            <div class="project-links">
                <a href="https://github.com/Jannatulmawa20/company-policy-rag-chatbot" target="_blank" class="btn">View Code</a>
                <!-- Add live demo link here if deployed -->
            </div>
        </div>

        <div class="project-card">
            <h3>Ride Sharing Price Prediction System</h3>
            <p>Python • Scikit-learn • Streamlit</p>
            <p>Trained multiple ML models on 100k+ ride records and deployed an interactive price prediction tool.</p>
            <div class="project-links">
                <a href="https://github.com/Jannatulmawa20/ride-sharing-price-prediction" target="_blank" class="btn">View Code</a>
                <a href="https://github.com/Jannatulmawa20/Ride-Price-Prediction-App" target="_blank" class="btn btn-secondary">App Repo</a>
            </div>
        </div>

        <div class="project-card">
            <h3>Brain Tumour Detection (Medical Imaging)</h3>
            <p>Python • PyTorch/TensorFlow • CNN • YOLO</p>
            <p>Developed segmentation and detection models on medical imaging datasets with end-to-end training and hyperparameter tuning.</p>
            <div class="project-links">
                <a href="https://github.com/Jannatulmawa20/Brain-Tumour" target="_blank" class="btn">View Code</a>
            </div>
        </div>

        <p style="text-align:center; margin-top:3rem;">
            <a href="https://github.com/Jannatulmawa20" target="_blank" style="font-size:1.2rem; color:var(--primary);">
                Explore all projects on GitHub →
            </a>
        </p>
    </section>

    <section id="education">
        <h2>Education</h2>
        <div class="experience-item">
            <h3>B.Sc. in Computer Science & Engineering</h3>
            <p>International Standard University (ISU) • 2021 – 2025</p>
            <p>CGPA: 3.29</p>
        </div>
        <div class="experience-item">
            <h3>Higher Secondary Certificate (HSC)</h3>
            <p>Chototulagaon Mohila College • 2020</p>
            <p>GPA: 4.90</p>
        </div>
    </section>

    <section id="contact">
        <h2>Contact</h2>
        <p style="text-align:center;">
            <strong>Phone:</strong> 01826708635<br>
            <strong>Email:</strong> mawamukta1234@gmail.com<br>
            <strong>Location:</strong> Mohakhali, TB-Gate, Dhaka-1212<br><br>
            <a href="https://github.com/Jannatulmawa20" target="_blank">GitHub</a> • 
            <a href="https://www.linkedin.com/in/jannatul-mawa-mukta-0bb1142a5" target="_blank">LinkedIn</a>
        </p>
    </section>

    <footer>
        <p>© 2026 Jannatul Mawa. All rights reserved.</p>
        <div class="social-links">
            <a href="https://github.com/Jannatulmawa20" target="_blank"><i class="fab fa-github"></i></a>
            <a href="https://www.linkedin.com/in/jannatul-mawa-mukta-0bb1142a5" target="_blank"><i class="fab fa-linkedin"></i></a>
        </div>
    </footer>
</body>
</html>
"""

# Save your profile photo as 'profile.jpg' in the same folder
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Modern dark-blue portfolio generated! 🎉")
print("\nInstructions:")
print("1. Save your photo (the one you uploaded) as 'profile.jpg' in the same folder as index.html")
print("2. Run this script → it creates/overwrites index.html")
print("3. Open index.html in your browser – beautiful modern dark theme with blue accents")
print("4. All GitHub links are accurate based on your real repositories")
print("5. If you deploy any Streamlit apps, add the live demo URLs to the buttons")
print("\nHost it for free on:")
print("- GitHub Pages (create a repo and enable Pages)")
print("- Netlify (drag & drop the folder)")
print("- Vercel")
print("\nYour portfolio now looks professional, modern, and recruiter-friendly! 🚀")