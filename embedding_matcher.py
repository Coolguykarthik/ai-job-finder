from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def match_jobs(skills, jobs):

    skill_embed = model.encode([skills])

    job_embed = model.encode(jobs)

    scores = cosine_similarity(skill_embed, job_embed)[0]

    ranked = sorted(zip(jobs, scores), key=lambda x: x[1], reverse=True)

    return ranked[:10]