from fastapi import HTTPException
from src import prisma

async def register_seed():
    try:
        # User Table
        users = [
            {"id": "a", "email": "a@a.a", "password": "a", "name": "Intern", "role": "Member"},
            {"id": "c", "email": "c@c.c", "password": "c", "name": "Feedback user", "role": "Member"},
        ]
        # Project Table
        projects = [
            {"id": "aaa", 
                "name": "Making new songs", 
                "oneLiner": "Making next global hits", 
                "description": "Making next global hits worldwide", 
                "userId": "a"
            },
        ]
        # Submission Table
        submissions = [
            {"id": "aaa1", 
                "projectId": "aaa", 
                "week": 1,
                "progressRate": 5,
                "progressComment": "I have made the beat",
                "outputUrl": "https://www.youtube.com/watch?v=9bZkp7q19f0",
                "isActiveWeek": True,
                "submissionStatus": "Pending",
            },
            {"id": "aaa2", 
                "projectId": "aaa", 
                "week": 2,
                "progressRate": 8,
                "progressComment": "I have written the lyrics",
                "outputUrl": "https://www.youtube.com/watch?v=9bZkp7q19f0", 
                "isActiveWeek": False,
                "submissionStatus": "Pending",
            },
            {"id": "aaa3", 
                "projectId": "aaa", 
                "week": 3,
                "progressRate": 9,
                "progressComment": "I have recorded the song",
                "outputUrl": "https://www.youtube.com/watch?v=9bZkp7q19f0", 
                "isActiveWeek": False,
                "submissionStatus": "Pending",
            },
            {"id": "aaa4", 
                "projectId": "aaa", 
                "week": 4,
                "progressRate": 10,
                "progressComment": "I have mixed the song",
                "outputUrl": "https://www.youtube.com/watch?v=9bZkp7q19f0",
                "isActiveWeek": False, 
                "submissionStatus": "Pending",
            },
        ]
        # Feedback Table
        feedbacks = [
            {"submissionId": "aaa1", 
                "userId": "c",
                "evaluationRate": 5,
                "evaluationComment": "Sounds very cool! But I think you should make the sound quality a bit better, its hard to listen to with the other noise. Keep up the good work!",
                "isAnonymous": False,
            },
            {"submissionId": "aaa2", 
                "userId": "c",
                "evaluationRate": 4,
                "evaluationComment": "Good job! I like it:)",
                "isAnonymous": True,
            },
            {"submissionId": "aaa3", 
                "userId": "c",
                "evaluationRate": 3,
                "evaluationComment": "This is really impressive, however for me, it was too plain. I would love to hear the base sound more.",
                "isAnonymous": False,
            },
            {"submissionId": "aaa4", 
                "userId": "c",
                "evaluationRate": 5,
                "evaluationComment": "Excellent job",
                "isAnonymous": True,
            },
        ]

        # Insert data into the database
        result_users = await prisma.user.create_many(data=users, skip_duplicates=True)
        result_projects = await prisma.project.create_many(data=projects, skip_duplicates=True)
        result_submissions = await prisma.submission.create_many(data=submissions, skip_duplicates=True)
        result_feedbacks = await prisma.feedback.create_many(data=feedbacks, skip_duplicates=True)

        # Organize the results
        seed_data = {
            "users": result_users,
            "projects": result_projects,
            "submissions": result_submissions,
            "feedbacks": result_feedbacks,
        }

        return seed_data
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering users (Service)")
