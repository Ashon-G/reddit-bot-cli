# ml_models.py
from transformers import pipeline
import random

# Load the sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Define comment templates for different contexts
COMMENT_TEMPLATES = {
    'positive': [
        "That's great to hear! How did that make you feel?",
        "Awesome! I love when things go well. What was the highlight for you?",
        "It's wonderful to see positive experiences! What do you think contributed to this?",
    ],
    'neutral': [
        "Interesting perspective! Can you share more about it?",
        "Thanks for sharing! What do you think will happen next?",
        "I see your point. How do you feel about the current situation?",
    ],
    'negative': [
        "I'm sorry to hear that. What do you think could help improve the situation?",
        "That's tough. Have you thought about any solutions?",
        "I can understand how that might be frustrating. Have you considered talking to someone about it?",
    ]
}

def generate_response(post_text):
    # Basic keyword analysis to determine context
    keywords_positive = ['happy', 'great', 'awesome', 'love', 'fantastic']
    keywords_negative = ['bad', 'sad', 'frustrating', 'hate', 'worst']

    # Check if the post contains positive or negative keywords
    if any(keyword in post_text.lower() for keyword in keywords_positive):
        response_template = random.choice(COMMENT_TEMPLATES['positive'])
    elif any(keyword in post_text.lower() for keyword in keywords_negative):
        response_template = random.choice(COMMENT_TEMPLATES['negative'])
    else:
        response_template = random.choice(COMMENT_TEMPLATES['neutral'])
    
    return response_template
