from difflib import SequenceMatcher
from datetime import datetime


class ChatBot:
    def __init__(self, name:str, response_sentence:str)->float:
        self.name = name 
        self.responses = response_sentence

    @staticmethod
    def calculate_similarity(input_sentence: str, response_sentence: str)->float:
        sequence: SequenceMatcher = SequenceMatcher(a=input_sentence, b=response_sentence)
        return sequence.ratio()
    
    def get_best_response(self, user_input: str)->tuple[str, float]:
        highest_similarity: float = 0.0
        best_match: str = 'Sorry, I did\'t understand that'

        for response in self.responses:
            similarity: float = self.calculate_similarity(user_input, response)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match: str = self.responses[response] #type: ignore

        return best_match, highest_similarity
    
    def run(self)-> None:
        print(f'LUX PAPA : Hello! My name is {self.name}, how can I help you today?')
        
        while True:
            user_input: str = input('You: ')
            response, similarity = self.get_best_response(user_input)

            if response =='GET_TIME':
                response = f'The time is : {datetime.now():%H:%M}'

            print(f'{self.name}: {response}(similarity:{similarity:.2%})')




def main()->None:
    responses: dict[str, str] = {
        'hello': 'Hello! How are you today?',
        'how are you': 'Great, thanks! What about you?',
        'what time is it':'GET_TIME',
        'bye':'Goodbye! Have a great day!',
        'love you': 'love too',
        'what\'s your name ': 'I your ai assitant LUX PAPA',
        'What\'s your age ':'I am AI i don\'t have age please ask my creater Dr.venkat'
    }
    chatbot: ChatBot = ChatBot(name='venkat', response_sentence=responses)
    chatbot.run()


if __name__ == "__main__": 
    main()



"""
Homework:
1.Add more responses.
2.Add a way to exits the program through the chat.
3.Add some cool features, like cheacking for the weather forecaste.
4.Make it so that if the accuracy fall below 50%, it returns a default response.

"""