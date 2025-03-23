# Import necessary tools/libraries
import streamlit as st
import random
import time
import requests

# Set the title of our web app
st.title("Money Making Machine")

# Fallback business ideas
BACKUP_IDEAS = [
    "Start a dropshipping business",
    "Create an online course",
    "Start a YouTube channel",
    "Begin freelance writing",
    "Start a podcast",
    "Create digital products",
    "Offer consulting services",
    "Start a blog",
    "Become a social media manager",
    "Create a mobile app"
]

# Fallback quotes
BACKUP_QUOTES = [
    "The best investment you can make is in yourself. - Warren Buffett",
    "Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver. - Ayn Rand",
    "Investment in knowledge pays the best interest. - Benjamin Franklin",
    "The more you learn, the more you earn. - Frank Clark",
    "Don't work for money, make money work for you. - Robert Kiyosaki",
    "Success is not final; failure is not fatal. - Winston Churchill",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Time is more valuable than money. - Jim Rohn",
    "Money is a great servant but a bad master. - Francis Bacon",
    "The goal isn't more money. The goal is living life on your terms. - Chris Brogan"
]

# Function to create random amount of money
def generate_money():
    return random.randint(1, 1000)

# Function to get business ideas from multiple APIs
def fetch_side_hustle():
    try:
        # Try first API
        response = requests.get(
            "https://api.api-ninjas.com/v1/ideas?category=business",
            headers={'X-Api-Key': 'YHKs/MIT//ZX/sPQYojyYw==DUzNkUsnFJo4N8ab'}
        )
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[0]['idea']
                
        # Try second API
        response2 = requests.get("https://www.boredapi.com/api/activity?type=recreational")
        if response2.status_code == 200:
            data = response2.json()
            return f"Business idea: Turn '{data['activity']}' into a service"
            
        # If both APIs fail, use backup ideas
        return random.choice(BACKUP_IDEAS)
    except Exception as e:
        return random.choice(BACKUP_IDEAS)

# Function to get money-related quotes from multiple APIs
def fetch_money_quote():
    try:
        # Try first API
        response = requests.get("https://api.quotable.io/random?tags=success,business")
        if response.status_code == 200:
            data = response.json()
            return f"{data['content']} - {data['author']}"
            
        # Try second API
        response2 = requests.get("https://api.api-ninjas.com/v1/quotes?category=success",
            headers={'X-Api-Key': 'YHKs/MIT//ZX/sPQYojyYw==DUzNkUsnFJo4N8ab'}
        )
        if response2.status_code == 200:
            data = response2.json()
            if data:
                return f"{data[0]['quote']} - {data[0]['author']}"
                
        # If both APIs fail, use backup quotes
        return random.choice(BACKUP_QUOTES)
    except Exception as e:
        return random.choice(BACKUP_QUOTES)

# Create a section for generating money
st.subheader("Instant Cash Generator")
if st.button("💰 Generate Money 💰"):
    with st.spinner("Counting your money..."):
        time.sleep(random.uniform(1, 3))
        amount = generate_money()
        st.success(f"You made ${amount}!")

# Create a section for side hustle ideas
st.subheader("Side Hustle Ideas")
if st.button("🚀 Generate New Hustle Idea 🚀", key="hustle"):
    with st.spinner("Finding your next business idea..."):
        time.sleep(random.uniform(1, 2))
        idea = fetch_side_hustle()
        st.success(idea)

# Create a section for motivation quotes
st.subheader("Money-Making Motivation")
if st.button("✨ Get New Inspiration ✨", key="quote"):
    with st.spinner("Finding wisdom..."):
        time.sleep(random.uniform(1, 2))
        quote = fetch_money_quote()
        st.info(quote)

# Add a footer
st.markdown("---")
st.markdown("*Made with ❤️ by Ayesha Mughal(https://github.com/CodeVoyager007)*")
