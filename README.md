# voice-ai-admissions-counselor

A voice AI agent built for an admissions office, capable of answering student questions using a tool-based architecture.

This repository contains the source code and documentation for a voice AI agent built for a university admissions office. The agent can answer prospective student questions about courses, fees, and program durations.

## 🚀 Live Demo

You can interact with the live version of this agent here:
*   **[Test the Voice AI Agent](https://vapi.ai?demo=true&shareKey=ce9f629b-9256-46f4-9604-a1a5f1621a9a&assistantId=1761dbb9-8e6b-48ce-a6ab-ff80647d64aa)**

## 🌟 Key Features

*   **Natural Conversation:** Understands user questions and handles follow-ups.
*   **Tool-Based Architecture:** Uses a Python (Flask) backend tool to retrieve accurate course data.
*   **Resilient Design:** Gracefully handles ambiguous queries and out-of-scope questions.
*   **Built with a Prompt-First Approach:** The agent's logic, personality, and safety guardrails are defined by a comprehensive system prompt.

## 🛠️ Tech Stack

*   **Voice Platform:** Vapi
*   **LLM:** Llama 3 8B (via Together AI)
*   **Backend Tool Server:** Python, Flask
*   **Hosting:** Replit


#### 1. Prompt & Conversation Flow

The agent's logic is governed by a detailed system prompt that defines its persona ("Alex," a professional admissions counselor) and its core rules.

*   **Goal-Oriented:** The primary goal is to assist students by providing accurate course information. A secondary goal is to gather the caller's name and course interest.
*   **Instruction-Driven:** The prompt uses strict instructions, such as mandating the use of the `get_course_info` tool for all data queries and enforcing an exact-phrase response for out-of-scope questions to prevent hallucination.
*   **Safety Guardrails:** The agent is explicitly forbidden from mentioning any real-world university details, ensuring confidentiality and focus.
*   **Conversation Flow:** The designed flow is logical and user-centric: **Greet -> Identify Intent -> Use Tool to Answer -> Handle Follow-ups / Out-of-Scope -> Conclude.**

#### 2. Tools & Technical Stack

This agent was built using a stack of reliable and performant tools.

*   **Platform:** **Vapi** (for real-time conversation management).
*   **Language Model (LLM):** **Llama 3 8B**, accessed via the **Together AI** API.
*   **Backend Server:** **Python (Flask)** server hosted on **Replit** to serve the primary tool.
*   **Speech-to-Text:** **Gladia** was explicitly configured for robust transcription.

#### 3. Data Storage & Retrieval

To ensure low latency and simplicity, the course data table was stored as an in-memory JSON object on the Replit server rather than in an external database.

*   **Retrieval Method:** A single tool, `get_course_info`, is exposed to the LLM. This function takes `course_name` or `level` (e.g., "bachelor," "master") as arguments, searches the JSON data, and returns the precise course details for the agent to articulate.

---
**A Note on Performance:** This agent is deployed entirely on free-tier services. As a result, you may experience a minor "cold start" latency on the first query if the agent has been idle. This is a known characteristic of the serverless architecture. Subsequent interactions will be significantly faster.


Created With Vibes & ❤️ by Ankit Singh
