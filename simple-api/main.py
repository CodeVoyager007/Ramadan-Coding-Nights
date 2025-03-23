from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
    "Virtual Assistant - Help businesses with administrative tasks!",
    "Web Design - Create beautiful websites for clients!",
    "Photography - Sell your photos on stock photo websites!",
    "Podcast Production - Help others create and edit podcasts!",
    "Online Tutoring - Teach students virtually!",
    "Digital Art - Create and sell digital artwork!",
    "eBook Writing - Write and sell digital books!",
    "Voice Over Work - Narrate audiobooks and commercials!",
    "3D Printing Service - Create custom items for clients!",
    "Online Fitness Coaching - Help others stay healthy!",
    "Resume Writing - Help job seekers stand out!",
    "Translation Services - Help bridge language barriers!",
    "Data Entry - Work from home doing administrative tasks!",
    "Graphic Design - Create logos and marketing materials!",
    "NFT Creation - Design and sell digital collectibles!",
    "Online Research - Help businesses gather information!",
    "Transcription Services - Convert audio to text!",
    "Website Flipping - Buy, improve, and sell websites!",
    "Social Media Influencing - Build and monetize your following!"
]

money_quotes = [
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "If you don't find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "Opportunities don't happen. You create them. – Chris Grosser",
    "Don't stay in bed unless you can make money in bed. – George Burns",
    "Money often costs too much. – Ralph Waldo Emerson",
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett",
    "It's not about having lots of money. It's about knowing how to manage it. – Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Money grows on the tree of persistence. – Japanese Proverb",
    "The more you learn, the more you earn. – Frank Clark",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Investment in knowledge pays the best interest. – Benjamin Franklin",
    "Time is more valuable than money. You can get more money, but you cannot get more time. – Jim Rohn",
    "The best investment you can make is in yourself. – Warren Buffett",
    "Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver. – Ayn Rand",
    "Don't work for money, make money work for you. – Robert Kiyosaki",
    "The goal isn't more money. The goal is living life on your terms. – Chris Brogan",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Twenty years from now you will be more disappointed by the things you didn't do than by the ones you did. – Mark Twain",
    "The secret to getting ahead is getting started. – Mark Twain",
    "Success is walking from failure to failure with no loss of enthusiasm. – Winston Churchill",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt"
]


@app.get("/")
def read_root():
    return {
        "message": "Hello World, Go to /side_hustles or /money_quotes to get a random side hustle or money quote"
    }


@app.get("/side_hustles")
def get_side_hustles():
    """Returns a random side hustle idea"""
    return {"side_hustle": random.choice(side_hustles)}


@app.get("/money_quotes")
def get_money_quotes():
    """Returns a random money quote"""
    return {"money_quote": random.choice(money_quotes)}