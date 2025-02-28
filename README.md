# CDP Support Chatbot

## Project Overview

This project is a **Customer Data Platform (CDP) Support Chatbot** designed to answer "how-to" questions related to four popular CDPs: **Segment**, **mParticle**, **Lytics**, and **Zeotap**. The chatbot extracts relevant information from the official documentation of these platforms to guide users on how to perform tasks or achieve specific outcomes.

The chatbot is built using **Streamlit**, **BeautifulSoup**, and **Python**, with the ability to fetch and parse documentation, index it, and respond to user queries.

## Features

- **Answer "How-to" Questions:** The chatbot provides answers related to setting up sources, creating user profiles, building audience segments, and more.
- **Information Extraction:** Retrieves relevant documentation content to respond accurately.
- **Cross-CDP Comparisons:** The chatbot can answer questions about differences in approaches and functionalities between the platforms.
- **Handle Variations in Questions:** Capable of handling variations in question phrasing, size, and irrelevant questions.
- **Real-Time Assistance:** Users can interact with the bot in real-time through a simple Streamlit interface.

## Data Sources

The chatbot fetches and parses documentation from the following sources:
- **Segment Documentation:** [https://segment.com/docs/?ref=nav](https://segment.com/docs/?ref=nav)
- **mParticle Documentation:** [https://docs.mparticle.com/](https://docs.mparticle.com/)
- **Lytics Documentation:** [https://docs.lytics.com/](https://docs.lytics.com/)
- **Zeotap Documentation:** [https://docs.zeotap.com/home/en-us/](https://docs.zeotap.com/home/en-us/)

## Core Functionalities

1. **Answering "How-to" Questions:**
    - The chatbot answers specific "how-to" questions related to each CDP. For example:
      - "How do I set up a new source in Segment?"
      - "How can I create a user profile in mParticle?"
      - "How do I build an audience segment in Lytics?"
      - "How can I integrate my data with Zeotap?"

2. **Extracting Information from Documentation:**
    - It retrieves and processes documentation content to provide instructions or steps to the user.
  
3. **Handling Variations in Questions:**
    - The chatbot is designed to understand different variations of phrasing and terminology, even if questions are long or complex.
    - It can also reject irrelevant or unrelated queries.

4. **Cross-CDP Comparisons:**
    - Example questions: 
        - "How does Segment’s audience creation process compare to Lytics?"
        - "How does mParticle handle data integration differently from Zeotap?"

## How It Works

1. **Fetching Documentation:**
    - The chatbot fetches data from official documentation pages of the four platforms.
  
2. **Indexing Content:**
    - It processes the fetched data by indexing keywords and their corresponding content.

3. **Responding to User Queries:**
    - When the user asks a question, the bot matches keywords and returns relevant documentation snippets to answer the question.

4. **Cross-Platform Functionality:**
    - It can compare features or processes across CDPs when the user asks for a comparison.

## Example Questions

Once the Streamlit app is running, you can interact with the chatbot by typing your questions into the input field. The bot will answer based on the documentation from **Segment**, **mParticle**, **Lytics**, and **Zeotap**. Below are some example questions you can ask the chatbot:

### **Platform-Specific "How-to" Questions:**
1. **Segment:**
   - "How do I set up a new source in Segment?"
   - "How can I track events in Segment?"
   - "How do I integrate Segment with Google Analytics?"

2. **mParticle:**
   - "How can I create a user profile in mParticle?"
   - "How do I set up a new data stream in mParticle?"
   - "How do I integrate mParticle with Facebook?"

3. **Lytics:**
   - "How do I build an audience segment in Lytics?"
   - "How do I integrate Lytics with a third-party platform?"
   - "How can I set up event tracking in Lytics?"

4. **Zeotap:**
   - "How can I integrate my data with Zeotap?"
   - "How do I create a custom audience in Zeotap?"
   - "How do I export data from Zeotap?"

### **Cross-CDP Comparison Questions:**
- "How does Segment’s audience creation process compare to Lytics?"
- "What is the difference between mParticle and Zeotap when it comes to data integration?"
- "How does the data tracking setup differ between Segment and mParticle?"

### **General "How-to" Questions:**
- "How do I connect Segment to my CRM system?"
- "How can I create a customer profile across different CDPs?"
- "How do I track user behavior in real-time using mParticle?"

### **Irrelevant or Unrelated Questions:**
If you ask questions that are outside the scope of the CDPs, like:
- "Which movie is releasing this week?"
- "What's the weather like today?"

The chatbot will respond with:
- "Sorry, I couldn't find relevant information."

  ## Visit my Project documentation here:https://gamma.app/docs/cdp-chatbotpy-3e0l4kxmhc0ctjh

