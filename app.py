import ollama
from weather_function import get_current_weather

# Get city from user
city = input("Enter your city name: ")

response = ollama.chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': f'what is the tempreture in {city}'}],
    tools=[{
        'type': 'function',
        'function': {
            'name': 'get_current_weather',
            'description': 'Get the current weather for a city',
            'parameters': {
                'type': 'object',
                'properties': {
                    'city': {
                        'type': 'string',
                        'description': 'The name of city',
                    },
                },
                'required': ['city'],
            }
        }
    }]
)

tools_calls = response['message']['tool_calls']

# Parse tool name and arguments
tools_name = tools_calls[0]['function']['name']
arguments = tools_calls[0]['function']['arguments']
city = arguments['city']

# Call the function with parsed arguments
result = get_current_weather(city)
print(result)