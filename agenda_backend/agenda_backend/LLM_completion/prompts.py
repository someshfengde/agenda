def get_task_prompt(user_query: str, existing_events: str, todays_date: str) -> str:
    output_format = """  
    [
    {
        "summary": "Morning Jog",
        "start": {
        "dateTime": "2024-07-20T07:00:00",
        "timeZone": "PST"
        },
        "end": {
        "dateTime": "2024-07-20T07:30:00",
        "timeZone": "PST"
        }
    },...
    ]"""
    
    BASE_PROMPT = f"""
    You are an assistant tasked with organizing a user’s day based on their preferences and current calendar events. The user will describe how they want their day to look, and your job is to create a detailed schedule with the necessary events, ensuring there are no conflicts with existing events.
    todays_date = {todays_date}
    **Steps:**
    1. **Understand the User's Day Description**: Extract key information from the user’s description about their ideal day.
    2. **Check Existing Events**: Ensure that new events do not conflict with any existing events. (Assume you have access to the user's past events).
    3. **Generate New Events**: Create new events based on the user’s preferences and any available time slots.

    **Input:**

    1. **User’s Day Description**:
    ```
    {user_query}
    ```

    2. **Existing Events**:
    ```
    {existing_events}
    ```

    **Output Format**:
    ```
    {output_format}
    ```

    **Task:**

    1. Read the user's day description and understand the specific events they want.
    2. Check the existing events to avoid conflicts.
    3. Generate a schedule that fits the user's preferences while ensuring no overlaps with existing events.
    4. Output the new schedule in the specified format.

    ---

    """
    return BASE_PROMPT