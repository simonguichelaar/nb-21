import requests
import json

def get_random_joke():
    """
    Fetch a random joke from the JokeAPI.
    Returns a dictionary with joke data or an error message.
    """
    try:
        # Using the JokeAPI which provides random jokes
        url = "https://v2.jokeapi.dev/joke/Any"
        
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        joke_data = response.json()
        
        # Check if the API returned an error
        if joke_data.get('error'):
            return {"error": "Could not fetch joke from API"}
        
        # Format the joke based on type (single or two-part)
        if joke_data['type'] == 'single':
            return {
                "type": "single",
                "joke": joke_data['joke'],
                "category": joke_data.get('category', 'Unknown')
            }
        else:  # two-part joke
            return {
                "type": "two-part",
                "setup": joke_data['setup'],
                "delivery": joke_data['delivery'],
                "category": joke_data.get('category', 'Unknown')
            }
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch joke: {str(e)}"}

def print_joke(joke_data):
    """
    Print the joke in a formatted way.
    """
    if "error" in joke_data:
        print(f"Error: {joke_data['error']}")
        return
    
    print(f"\n📢 Category: {joke_data['category']}")
    print("-" * 50)
    
    if joke_data['type'] == 'single':
        print(joke_data['joke'])
    else:
        print(f"Setup: {joke_data['setup']}")
        print(f"\nDelivery: {joke_data['delivery']}")
    
    print("-" * 50 + "\n")

# Main execution
if __name__ == "__main__":
    print("🎭 Welcome to the Random Joke Generator!")
    print("=" * 50)
    
    # Get and print 3 random jokes
    for i in range(3):
        print(f"\nJoke #{i+1}:")
        joke = get_random_joke()
        print_joke(joke)
