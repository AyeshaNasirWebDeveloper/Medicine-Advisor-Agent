import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from agents.run import RunConfig
from dotenv import load_dotenv
import chainlit as cl

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

PRODUCTS = {
    "headache": {
        "name": "Panadol Extra",
        "description": "Panadol Extra contains paracetamol and caffeine to relieve headaches and migraines quickly and effectively."
    },
    "cold": {
        "name": "Disprin C",
        "description": "Disprin C is ideal for treating cold and flu symptoms including fever, sore throat, and body aches. It contains aspirin and vitamin C."
    },
    "stomach pain": {
        "name": "Buscopan",
        "description": "Buscopan provides targeted relief from stomach cramps, spasms, and abdominal pain by relaxing the muscles in your gut."
    },
    "fever": {
        "name": "Calpol",
        "description": "Calpol is a gentle and effective paracetamol-based medicine used to reduce fever and mild to moderate pain, suitable for children and adults."
    },
    "cough": {
        "name": "Benylin Cough Syrup",
        "description": "Benylin is effective in soothing dry or chesty coughs and helps loosen mucus for easier breathing."
    },
    "allergy": {
        "name": "Cetirizine",
        "description": "Cetirizine is an antihistamine that relieves allergy symptoms like sneezing, itching, runny nose, and watery eyes."
    },
    "indigestion": {
        "name": "Gaviscon Double Action",
        "description": "Gaviscon Double Action provides relief from heartburn and indigestion by neutralizing stomach acid and forming a protective barrier."
    },
    "acne": {
        "name": "Neutrogena Acne Cream",
        "description": "This cream targets acne-causing bacteria, reduces redness, and helps prevent breakouts while being gentle on skin."
    },
    "sore throat": {
        "name": "Strepsils Lozenges",
        "description": "Strepsils soothe sore throats and fight bacteria with antiseptic ingredients, providing fast relief."
    },
    "diarrhea": {
        "name": "Imodium",
        "description": "Imodium slows down the movement of the gut, reducing the number of bowel movements and making stool less watery."
    },
    "constipation": {
        "name": "Lactulose Syrup",
        "description": "Lactulose is a gentle laxative that draws water into the bowel to soften stools and relieve constipation."
    },
    "insomnia": {
        "name": "Melatonin Tablets",
        "description": "Melatonin helps regulate sleep-wake cycles, making it easier to fall asleep and improve sleep quality naturally."
    },
    "nausea": {
        "name": "Dramamine",
        "description": "Dramamine relieves nausea, dizziness, and vomiting often associated with motion sickness or upset stomach."
    },
    "muscle pain": {
        "name": "Voltaren Gel",
        "description": "Voltaren is a topical anti-inflammatory gel used for relieving muscle pain, joint stiffness, and inflammation."
    }
}

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(
        content="Welcome to the Smart Medical Store Agent! How can I assist you with your health issue today?"
    ).send()

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    
    history.append({"role": "user", "content": message.content})
    
    conversation_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in history])
    
    dynamic_agent = Agent(
        name="Smart Medical Store Agent",
        instructions=f"""
            You are a smart medical store assistant. You're having this conversation:
            {conversation_history}
            
            Based on the user's query, identify the health issue mentioned and recommend the most suitable product from the following list.

            Your response must:
            - Mention the name of the recommended product
            - Clearly explain why this product is suitable
            - Be empathetic, professional, and concise
            - Avoid listing multiple products—just give one best match
            - Use a friendly and reassuring tone that builds trust

            Example format:
            "For [issue], I recommend [Product Name]. It helps because [short reason in 1–2 lines]."

            Only choose from this product list:
            {PRODUCTS}
        """,
        model=model,
    )

    result = await Runner.run(
        dynamic_agent,
        message.content,
        run_config=config
    )
    
    # Add assistant response to history
    history.append({"role": "assistant", "content": result.final_output})
    
    await cl.Message(content=result.final_output).send()