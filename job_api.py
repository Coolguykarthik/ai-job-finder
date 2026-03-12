import requests
import os
from dotenv import load_dotenv

load_dotenv()

JOOBLE_API_KEY = os.getenv("JOOBLE_API_KEY")


class JoobleAPI:
    """Jooble API wrapper for job searching"""
    
    def __init__(self):
        self.api_key = JOOBLE_API_KEY
        self.base_url = "https://jooble.org/api/"
        
    def search_jobs(self, query, location="India"):
        """
        Search for jobs using Jooble API
        
        Args:
            query (str): Job search query/keywords
            location (str): Location to search in
            
        Returns:
            list: List of job dictionaries
        """
        if not self.api_key:
            raise ValueError("JOOBLE_API_KEY not found in environment variables")
            
        url = f"{self.base_url}{self.api_key}"
        
        payload = {
            "keywords": query,
            "location": location
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raise exception for bad status codes
            data = response.json()
            
            jobs = []
            
            for job in data.get("jobs", []):
                jobs.append({
                    "title": job.get("title"),
                    "company": job.get("company"),
                    "link": job.get("link"),
                    "description": job.get("snippet", job.get("description", "")),
                    "location": job.get("location", location),
                    "source": "Jooble"
                })
                
            return jobs
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching jobs from Jooble: {e}")
            return []
        except ValueError as e:
            print(f"Error parsing Jooble response: {e}")
            return []