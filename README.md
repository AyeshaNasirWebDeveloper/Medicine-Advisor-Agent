# 🏥 Medical Store Assistant Chatbot

An AI-powered virtual assistant for medical stores that recommends appropriate over-the-counter medications based on customer symptoms.

## Features

- 💊 Recommends suitable medical products for common health issues
- 🗣️ Natural conversation interface
- 📝 Maintains conversation history
- ⚡ Fast response times using Gemini AI
- 🔒 Secure API key management

## Technologies Used

- [Chainlit](https://chainlit.io/) - Chat interface framework
- [Gemini AI](https://deepmind.google/technologies/gemini/) - Language model
- Python 3.10+
- AsyncIO - For asynchronous operations

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AyeshaNasirWebDeveloper/Agentic-AI-Assignment-1/smart-store-agent.git

2. Create and activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Create a .env file and add your Gemini API key:

env
GEMINI_API_KEY=your_api_key_here
Usage
Run the application:

bash
uv run chainlit run suggester.py
Open your browser to:

text
http://localhost:8000
Start chatting with the medical assistant!

Example Conversations
User: I have a headache
Assistant: For headache, I recommend Panadol Extra. It helps because it contains paracetamol and caffeine to relieve headaches quickly and effectively.

User: What was my last message?
Assistant: Your last message was about having a headache. Did you want more information about Panadol Extra?

Product Coverage
The assistant can recommend products for:

🤕 Headaches

🤒 Cold and flu

🤢 Stomach pain

🌡️ Fever

😷 Cough

🤧 Allergies

And more...

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## License
MIT License - See LICENSE

Created with ❤️ by [Ayesha Nasir] | https://linktr.ee/ayesha_nasir