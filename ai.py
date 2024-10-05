from openai import OpenAI
from database import getSchema, executeQuery
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the values
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)


def getQueryFromQuestion(question: str):

    try:
        completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"""I am giving you the following schema:
                    {getSchema()}

                    Using that schema, generate a sqlite query that I can use to answer and get information for this question:
                    {question}

                    Only give me the SQL the sql string:
                    ie Response: SELECT COUNT(*) FROM table;
                    """
                }
            ]
        )
    except Exception as e:
        print(e)

    return completion.choices[0].message.content

def getUserFriendlyResponseFromSQlResult(result):
    try:
        completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"""
                    Take this result from a SQL Query:
                    {str(result)}

                    And return a user friendly formatted response for it
                    """
                }
            ]
        )
    except Exception as e:
        print(e)

    return completion.choices[0].message.content



query = getQueryFromQuestion("Give me all superheroes on 'The Avengers' that have the power 'Laser Vision'")
print(query)
queryResult = executeQuery(query)
print(queryResult)
print(getUserFriendlyResponseFromSQlResult(queryResult))