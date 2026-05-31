import random
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel("gemini-1.5-flash")

subjects = [
    "Imran Khan", "Nawaz Sharief", "Asif Ali Zardari",
    "Bilawal Bhutto Zardari", "Shahbaz Sharif", "Maryam Nawaz",
    "Pervez Musharraf", "Benazir Bhutto",
]

actions = [
    "spotted secretly eating a plate of anda shami burger at 3 AM",
    "was seen dancing to the tunes of a Punjabi song",
    "was caught red-handed stealing a piece of cake",
    "caught on camera trying to do a wheelie on a CD-70 bike",
    "accidentally joined a random baraat and started doing the Luddi dance",
    "challenged a street vendor to a chaat-eating contest",
    "mistook a politician's shoe for a microphone",
    "started teaching yoga to a group of goats",
    "took selfies with a flock of pigeons",
    "tried to referee a kabaddi game with a banana",
    "attempted to juggle laddoos while giving a speech",
    "ordered 20 samosas and declared them national currency",
    "hosted a surprise talent show for street monkeys",
    "rode a donkey to a formal dinner",
    "tried to grill kebabs on the parliament steps",
    "got lost chasing a runaway balloon",
    "started a conga line of tuk-tuks",
    "brought a carton of mangoes to a board meeting",
    "turned a press break into an impromptu singing session",
]

places = [
    "at a local dhaba",
    "in the middle of a cricket match",
    "during a press conference",
    "while giving a speech",
    "at a wedding ceremony",
    "inside a snazzy auto rickshaw",
    "in a crowded market selling jalebis",
    "near a roadside stall full of samosas",
    "on a rooftop watching the sunset",
    "at a neighborhood mehndi party",
    "at a midnight chai stall",
    "underneath a giant billboard of their own photo",
    "in the VIP lounge of a five-star hotel",
    "at the entrance of a cultural festival",
    "in the middle of a crowded food festival",
    "on the lawn outside a grand wedding palace",
]

def generate_headline():
    subject = random.choice(subjects)
    action  = random.choice(actions)
    place   = random.choice(places)
    return f"BREAKING NEWS: {subject} {action} {place}."

def get_ai_analysis(headline):
    prompt = f"""You are a dramatic Pakistani news analyst who takes everything extremely seriously.

Someone just sent you this breaking news:
"{headline}"

Respond in EXACTLY this format, nothing more, nothing less:

[Your dramatic 1-2 sentence reaction as an analyst. Use Urdu words naturally like yaar, bhai, Allah miya, subhanallah, aray waah.]

Credibility Score: X/10
National Crisis Level: [choose one: Low / Moderate / High / DEFCON 1]

Keep it funny and dramatic. Do not add any extra text outside this format."""

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception:
        return "Our analyst is currently unavailable. Please generate another headline."