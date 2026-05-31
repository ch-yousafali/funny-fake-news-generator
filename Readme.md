# Fake News Generator

A lightweight, web-based fake news headline generator built with Python (Flask) and Google Gemini AI. It randomly combines subjects, actions, and places to generate absurd political headlines, then uses Gemini 1.5 Flash to produce a dramatic fake analyst reaction.

## Features

- Random headline generation using subject + action + place lists.
- AI-powered fake analysis with credibility score and crisis level.
- Clean, minimal dark-mode UI with a breaking news ticker.
- Download all generated headlines as a text file.
- No database needed, stateless generation per request.

## Files

- `app.py` — Flask routes and application entry point.
- `main.py` — Headline generation logic and Gemini AI integration.
- `templates/index.html` — Single-page UI with inline styles and scripts.
- `.env` — Environment file for `GEMINI_API_KEY`.

## Requirements

- Python 3
- Flask
- python-dotenv
- google-genai

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install Flask python-dotenv google-genai
```

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```
python3 app.py
```

Then open:

```
http://127.0.0.1:5000
```

## Usage

1. Load the page to see the first generated headline and AI analysis.
2. Click **Generate Next Headline** to create a new random headline.
3. Click **Download Headlines** to save all generated headlines to a `.txt` file.

## Notes

- The app requires a valid Gemini API key to fetch the analyst reaction.
- If the AI service is unavailable, a fallback message is displayed.
- Headlines are stored in browser memory for the download feature.

## Architecture

```
+-----------+                +---------------------+                +-------------+
|  Web UI   | -------------> |       Backend       | -------------> |   Gemini    |
|           |  Generate      |      (Flask)        |  AI Analysis   |     AI      |
| (Browser) | <------------- |                     | <------------- |             |
+-----------+  Headline +    | - Random Headline   |                +-------------+
               Analysis      | - Gemini Prompt     |
                             +---------------------+
```