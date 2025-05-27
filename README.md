# Chat Bot Project

A simple interactive chatbot implementation in Python that uses sequence matching to provide appropriate responses to user inputs.

## Features

- Text similarity-based response matching using `difflib.SequenceMatcher`
- Real-time responses with similarity score display
- Current time query support
- Extensible response dictionary
- Type hints for better code readability

## Usage

```python
responses = {
    'hello': 'Hello! How are you today?',
    'how are you': 'Great, thanks! What about you?',
    'what time is it': 'GET_TIME',
    # Add more responses here
}

# Run the bot
chatbot = ChatBot(name='Bot Name', response_sentence=responses)
chatbot.run()
```

## Requirements

- Python 3.9 or higher
- No external dependencies required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chatbot.git
cd chatbot
```

2. Run the main script:
```bash
python main.py
```

## How it Works

The chatbot uses sequence matching to find the most similar predefined response to user input. It calculates similarity scores using Python's `difflib.SequenceMatcher` and returns the response with the highest match percentage.

## Contributing

Feel free to fork this project and submit pull requests with improvements. Some areas for enhancement:
- Adding more responses
- Implementing exit commands
- Adding weather forecast feature
- Improving response matching accuracy

## License

MIT License - Feel free to use this code for any purpose.