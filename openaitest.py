import os
import openai
from config import apikey

# Set the OpenAI API key
openai.api_key = apikey

try:
    # Make the API call to generate completions
    response = openai.Completion.create(
        model="gpt-3.5-turbo-1106",
        prompt="Write an email to my boss for my resignation",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the API response
    print(response)

except openai.error.RateLimitError as e:
    print(f"Rate limit exceeded: {str(e)}")
    # Handle rate limit error, e.g., inform the user or retry after some time

except Exception as e:
    print(f"Error encountered: {str(e)}")
    # Handle other errors as needed