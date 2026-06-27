from app.services.internship_recommender import recommend_internships

sample_resume = """
Skills:
Java
SQL
HTML
CSS
JavaScript
"""

result = recommend_internships(sample_resume)

print("\n===== INTERNSHIP RECOMMENDATIONS =====\n")
print(result)