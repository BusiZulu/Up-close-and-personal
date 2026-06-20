# Busi Zulu - Personal Profile Program

name = "Busi Zulu"
role = "Software Engineering Student"
goal = "Aspiring Software Developer"
skills = [
    "HTML",
    "CSS",
    "Python",
    "JavaScript",
    "C#",
    "SQL"
]

about = """
Hello, my name is Busi Zulu.
I am a software engineering student passionate about technology
and creating solutions through code.

I am continuously learning and improving my development skills.
My goal is to grow into a software development role and contribute
to meaningful technology projects.
"""


def display_profile():
    print("===== Personal Profile =====")
    print(f"Name: {name}")
    print(f"Current Role: {role}")
    print(f"Career Goal: {goal}")
    
    print("\nSkills:")
    for skill in skills:
        print(f"- {skill}")
    
    print("\nAbout Me:")
    print(about)


display_profile()
