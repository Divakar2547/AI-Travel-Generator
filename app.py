from flask import Flask, render_template, request, jsonify
import openai  # optional, only if using AI

app = Flask(__name__)

# Optional: Uncomment if using OpenAI API
# openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_itinerary():
    data = request.get_json()
    destination = data.get('destination', '')
    days = int(data.get('days', 1))
    interests = data.get('interests', 'general sightseeing')

    # Option 1: Simple mock AI (default)
    itinerary = f"🗺️ Here’s your {days}-day itinerary for {destination}, focusing on {interests}:\n\n"
    for i in range(1, days + 1):
        itinerary += f"Day {i}: Explore key attractions, enjoy local food, and relax.\n"

    # Option 2: Use AI model (uncomment if you have API key)
    """
    prompt = f"Create a detailed {days}-day travel itinerary for {destination} focused on {interests}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )
    itinerary = response.choices[0].text.strip()
    """

    return jsonify({"itinerary": itinerary})

if __name__ == '__main__':
    app.run(debug=True)
