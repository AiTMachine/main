import os
from openai import OpenAI
import champ as FrontEnd

model_engine="gpt-3.5-turbo"

client = OpenAI(api_key=os.environ.get("CHAMP_BID_KEY"))


chatStream = client.chat.completions.create(
    model="gpt-3.5-turbo", # --> any other models we can use?
    messages=[
        {
            "role": "system", 
            "engine": "model",
            "content": f"You are a seasoned {FrontEnd.selectedCourse} who teaches at the, {FrontEnd.selectedGrade} level."
        },
        {
            "role": "user", 
            "engine": "model",
            "content": f"{FrontEnd.userQuery}"
        }
    ],
    temperature=0,
    max_tokens=200,
    n=1,
    stop=None
)



print(chatStream.choices[0].message.content)
exit()
