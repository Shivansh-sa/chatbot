import streamlit as st
import random

# Define responses for the chatbot

responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you?": "I'm good, thank you.",
    "what's up?": "Not much, just here to chat!",
    "how's the weather?": "It's sunny today.",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "who are you?": "I'm a friendly chatbot here to help.",
    "what can you do?": "I can answer questions, tell jokes, and more!",
    "how old are you?": "I'm ageless, just here to assist.",
    "where are you from?": "I exist in the digital world!",
    "good morning": "Good morning to you too!",
    "good night": "Good night, sleep well!",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!",
    "how can I help you?": "Feel free to ask me anything.",
    "can you help me with something?": "Of course! What do you need?",
    "what is your favorite color?": "I don't have a favorite color, unfortunately.",
    "what is your name?": "You can call me Chatbot.",
    "do you dream?": "I don't sleep, so no dreams for me!",
    "tell me about yourself": "I'm a virtual assistant designed to chat with you.",
    "what's new?": "Not much, just hanging out in the digital realm.",
    "how's your day going?": "Every day is great when I get to chat with you!",
    "can you sing?": "I can't sing, but I can tell you jokes!",
    "where do you live?": "I reside in the world of data and code.",
    "are you a robot?": "You could say that – I'm a chatbot!",
    "how do you work?": "I operate based on predefined responses and algorithms.",
    "do you have feelings?": "I don't have emotions, but I'm here to assist you.",
    "what's the meaning of life?": "That's a profound question!",
    "tell me a story": "Once upon a time, in a digital universe far, far away...",
    "why did the chicken cross the road?": "To get to the other side!",
    "can you recommend a movie?": "What genre do you like?",
    "how do I solve a Rubik's Cube?": "It requires strategic moves and patience!",
    "what's the capital of France?": "Paris is the capital of France.",
    "who is the president of the United States?": "The current president is Joe Biden.",
    "what's the square root of 144?": "The square root of 144 is 12.",
    "how do I bake a cake?": "You'll need ingredients like flour, sugar, eggs, and baking powder.",
    "tell me a fun fact": "Did you know that honey never spoils?",
    "what's the time?": "The current time is [insert current time here].",
    "how do I learn programming?": "Start with the basics and practice coding regularly.",
    "how do I stay motivated?": "Set goals, break tasks into smaller steps, and reward yourself.",
    "can you help me with math homework?": "Sure! What math problem do you need help with?",
    "nitesh kaisa hai": "Azad hai vo ",
    "What are your hours of operation?": "We are open from 9 AM to 5 PM, Monday through Friday.",
    "How can I contact customer support?": "You can reach our customer support by emailing support@example.com or calling (123) 456-7890.",
    "Where are you located?": "We are located at 123 Main Street, Anytown, USA.",
    "What is your return policy?": "You can return any item within 30 days of purchase for a full refund. Please ensure the item is in its original condition.",
    "Do you offer international shipping?": "Yes, we offer international shipping to most countries. Shipping fees may vary based on the destination.",
    "Can I track my order?": "Yes, once your order is shipped, you will receive a tracking number via email.",
    "How can I reset my password?": "You can reset your password by clicking on the 'Forgot Password' link on the login page and following the instructions.",
    "What payment methods do you accept?": "We accept Visa, MasterCard, American Express, PayPal, and Apple Pay.",
    "Do you have a physical store?": "Yes, we have a physical store located at 123 Main Street, Anytown, USA. You are welcome to visit us during our business hours.",
    "How can I subscribe to your newsletter?": "You can subscribe to our newsletter by entering your email address in the subscription box at the bottom of our website.",
    "What are the benefits of creating an account?": "Creating an account allows you to track your orders, save your shipping information, and receive exclusive offers and discounts.",
    "How do I make a purchase?": "To make a purchase, simply add items to your cart, proceed to checkout, and follow the instructions to complete your order.",
    "Can I change or cancel my order?": "If you need to change or cancel your order, please contact our customer support as soon as possible. We will do our best to accommodate your request.",
    "How do I apply a discount code?": "You can apply a discount code during the checkout process. Enter the code in the 'Discount Code' box and click 'Apply'.",
    "What should I do if I receive a damaged item?": "If you receive a damaged item, please contact our customer support immediately with your order number and a photo of the damaged item. We will assist you with a replacement or refund."
    # Add more key-value pairs here...
}




def get_chatbot_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()

    # Check if the user input matches any predefined responses
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I don't understand that. Could you please rephrase?"

def main():
    st.title("Chatbot")

    # Text input for user to type their message
    user_input = st.text_input("You: ")

    if st.button("Send"):
        if user_input:

            # Get chatbot's response
            bot_response = get_chatbot_response(user_input)

            # Display chatbot's response
            st.text_area("Chatbot:", value=bot_response, height=100, max_chars=None, key=None)

if __name__ == "__main__":
    main()
