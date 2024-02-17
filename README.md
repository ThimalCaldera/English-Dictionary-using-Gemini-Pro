# English Dictionary Application

## Overview

This is a simple dictionary application built using Streamlit. The app leverages Google's Generative AI and Google's Generative Language API to provide definitions for entered words. It also includes a text-to-speech feature to pronounce both the entered word and its definition.

## Setup

Before running the application, make sure to set up your environment with the required dependencies and API key. You need to have a Google API key, and the key should be stored in a `.env` file.

```bash
# Install required packages
pip install streamlit google python-dotenv gTTS

# Create a .env file and add your Google API key
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```
## Running the Application

To run the dictionary application, execute the following command in your terminal:

``` bash
streamlit run app.py
```

Replace `app.py` with the name of the Python file containing your application code.


## Features

- **Word Entry:** Enter a word in the text area.
- **Get Meaning:** Click the "Get Meaning" button to retrieve the definition of the entered word using the Google Generative AI model.
- **Text-to-Speech:** Listen to the pronunciation of the entered word and its definition by using the audio player.


## Credits

- **Built with Streamlit by [Thimal Caldera](https://github.com/ThimalCaldera)**
- **Powered by [Gemini-Pro](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/#sundar-note)**

## Disclaimer

This application is a demonstration of integrating Streamlit with Google's Generative AI and Generative Language API. Ensure you have the necessary permissions and comply with any terms of use when using external APIs.

Feel free to customize and enhance the prompts for the LLM  based on your preferences and requirements.

