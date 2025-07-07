from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# This is our course database, with all 18 courses from the prompt.
COURSE_DATA = [
    {
        "Course": "BSc IT (with industry certificates)", "Duration": "3 yrs",
        "Annual Fee": "1,12,000", "Fee After 20% Scholarship": "89,600"
    },
    {
        "Course": "BCA (with industry certificates)", "Duration": "3 yrs",
        "Annual Fee": "1,12,000", "Fee After 20% Scholarship": "89,600"
    },
    {
        "Course": "BBA (with industry certificates)", "Duration": "3 yrs",
        "Annual Fee": "1,12,000", "Fee After 20% Scholarship": "89,600"
    },
    {
        "Course": "MSc IT (with industry certificates)", "Duration": "2 yrs",
        "Annual Fee": "1,12,000", "Fee After 20% Scholarship": "89,600"
    },
    {
        "Course": "BCom (with industry certificates)", "Duration": "3 yrs",
        "Annual Fee": "83,000", "Fee After 20% Scholarship": "66,400"
    },
    {
        "Course": "BCom (without certificates)", "Duration": "3 yrs",
        "Annual Fee": "64,000", "Fee After 20% Scholarship": "51,000"
    },
    {
        "Course": "BCom (Hons) (with industry certificates)", "Duration": "3 yrs",
        "Annual Fee": "90,000", "Fee After 20% Scholarship": "72,000"
    },
    {
        "Course": "BA (Hons) Journalism & Mass Com (no certificates)", "Duration": "3 yrs",
        "Annual Fee": "53,000", "Fee After 20% Scholarship": "43,000"
    },
    {
        "Course": "BA (Hons) Journalism & Mass Com (with AI/ML certificates)", "Duration": "3 yrs",
        "Annual Fee": "70,000", "Fee After 20% Scholarship": "56,000"
    },
    {
        "Course": "BSc Animation (with AI/ML certificates)", "Duration": "3 yrs",
        "Annual Fee": "1,00,000", "Fee After 20% Scholarship": "80,000"
    },
    {
        "Course": "BHM", "Duration": "3 + 1 yrs", "Annual Fee": "83,000",
        "Fee After 20% Scholarship": "67,000"
    },
    {
        "Course": "BLIS", "Duration": "1 yr", "Annual Fee": "43,000",
        "Fee After 20% Scholarship": "35,000"
    },
    {
        "Course": "MLIS", "Duration": "1 yr", "Annual Fee": "43,000",
        "Fee After 20% Scholarship": "35,000"
    },
    {
        "Course": "DHM", "Duration": "1 yr", "Annual Fee": "83,000",
        "Fee After 20% Scholarship": "67,000"
    },
    {
        "Course": "BA (English/Hindi/Eco/History/PolSci/Psych/Soc)", "Duration": "3 yrs",
        "Annual Fee": "38,000", "Fee After 20% Scholarship": "30,400"
    },
    {
        "Course": "BFA", "Duration": "4 yrs", "Annual Fee": "78,000",
        "Fee After 20% Scholarship": "63,000"
    },
    {
        "Course": "BSc (industry certificates)", "Duration": "3 yrs",
        "Annual Fee": "1,12,000", "Fee After 20% Scholarship": "89,600"
    },
    {
        "Course": "MSc Animation (with AI/ML certificates)", "Duration": "2 yrs",
        "Annual Fee": "1,00,000", "Fee After 20% Scholarship": "80,000"
    }
]

def get_course_info(course_name: str = None, level: str = None):
    """
    This function searches the course data based on name or level.
    """
    if not course_name and not level:
        return {"error": "Please provide a course name or a level to search for."}

    results = []

    # Search by course name (handles acronyms and partial matches)
    if course_name:
        # Special case for "BSc" to avoid matching "BSc IT" and "BSc Animation" accidentally
        if course_name.lower() == 'bsc':
            for course in COURSE_DATA:
                if course["Course"].lower() == "bsc (industry certificates)":
                    results.append(course)
        else:
            for course in COURSE_DATA:
                if course_name.lower() in course["Course"].lower():
                    results.append(course)

    # Filter by level (master's, bachelor's, diploma)
    if level:
        level_prefix = ""
        if "master" in level.lower():
            level_prefix = 'M'
        elif "bachelor" in level.lower() or "bachelors" in level.lower():
            level_prefix = 'B'
        elif "diploma" in level.lower():
            level_prefix = 'D'

        for course in COURSE_DATA:
            # Add 'and course not in results' to avoid duplicates if user asks for e.g. "bachelor's in bcom"
            if course["Course"].startswith(level_prefix) and course not in results:
                results.append(course)

    # If there are many results from a broad search, just return the names
    if len(results) > 3 and not course_name:
        course_names = [course['Course'] for course in results]
        return {"courses_found": course_names}

    if not results:
        return {"error": "Sorry, I couldn't find any course matching that description."}

    return results

# This is the main endpoint that Vapi will call
@app.route('/', methods=['POST'])
def handle_tool_call():
    data = request.json
    tool_outputs = []

    if 'tool_calls' in data:
        for tool_call in data['tool_calls']:
            function_name = tool_call['function']['name']
            # Make sure arguments exist before trying to access them
            args = tool_call['function'].get('arguments', {})

            if function_name == 'get_course_info':
                # Call our actual function with the arguments provided by the LLM
                output = get_course_info(course_name=args.get('course_name'), level=args.get('level'))

                tool_outputs.append({
                    "tool_call_id": tool_call['id'],
                    "output": json.dumps(output) # Vapi expects the output as a JSON string
                })

    return jsonify({"tool_outputs": tool_outputs})

if __name__ == '__main__':
    # Runs the server on host 0.0.0.0 and port 8080
    app.run(host='0.0.0.0', port=8080)
