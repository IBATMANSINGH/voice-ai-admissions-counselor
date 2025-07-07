# voice-ai-admissions-counselor
A voice AI agent built for an admissions office, capable of answering student questions using a tool-based architecture.


### README: Admissions Counselor Voice AI Agent

**Submitted by: Ankit Singh**

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
