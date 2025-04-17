import openai
import os
from dotenv import load_dotenv

# Load environment variable
load_dotenv() 
openai.api_key = os.getenv("OPENAI_API_KEY")

def plan_of_action(transcript, max_steps=5, initial_prompt=None):
    try:
        current_plan = initial_prompt or ""  # Start with initial prompt if provided
        for step in range(max_steps):
            # Construct the prompt for the current step
            prompt = (
                f"Based on the following meeting transcript, create a detailed 5 point of plan of action:\n\n"
                f"Meeting Transcript:\n{transcript}\n\n"
                f"Current Plan:\n{current_plan}\n\n"
                f"Refine and extend the plan with additional steps:"
            )

            # Call the OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=600,  
                n=1,
                stop=None,
                temperature=0.7,
            )

            # Extract the next steps from the response
            next_steps = response.choices[0].message['content'].strip()
            current_plan += next_steps + "\n"  # Append to the current plan

        return current_plan

    except Exception as e:
        return f"Error generating plan of action: {e}"

with open("transcription.txt", "r") as f:
       transcript = f.read()

print(plan_of_action(transcript, max_steps=1, initial_prompt=None))







