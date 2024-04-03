import random

# Function to parse definitions from the TangoChat file
def parse_definitions(line):
    if line.startswith("~"):
        parts = line.strip().split(":")
        if len(parts) == 2:
            variable = parts[0][1:].strip()
            options = [opt.strip().strip('"') for opt in parts[1][1:-1].split()]
            return variable, options
    return None, None

# Function to parse conversation rules from the TangoChat file
def parse_rule(line):
    parts = line.strip().split(":")
    if len(parts) == 3 and parts[0].lower().startswith("u"):
        user_input = parts[1].strip().lower()
        responses = [resp.strip().strip('"') for resp in parts[2][1:-1].split()]
        return user_input, responses
    return None, None

# Function to handle user input
def handle_user_input(user_input, variables):
    user_input = user_input.lower()
    if user_input in variables:
        return variables[user_input]
    for pattern in variables:
        if user_input == pattern:
            return variables[pattern]
    return None

# Function to replace variables in responses
def replace_variables(response, variables):
    for var, value in variables.items():
        response = response.replace('$'+var, value)
    return response

# Main function to process TangoChat file
def process_tango_chat(filename):
    definitions = {}
    rules = {}
    variables = {}

    # Read TangoChat file
    with open(filename, 'r') as file:
        for line in file:
            # Ignore comments
            if line.strip().startswith('#'):
                continue

            # Parse definitions
            variable, options = parse_definitions(line)
            if variable and options:
                definitions[variable] = options
                continue

            # Parse conversation rules
            user_input, responses = parse_rule(line)
            if user_input and responses:
                rules[user_input] = responses
                continue

    # Handle conversation
    while True:
        user_input = input("User: ").strip()
        if not user_input:
            continue

        matched_response = None

        # Check if user input matches any defined rule
        for pattern, responses in rules.items():
            if user_input == pattern:
                matched_response = random.choice(responses)
                break

        # If user input doesn't match any rule, check for variable assignments
        if not matched_response:
            matched_response = handle_user_input(user_input, variables)

        # If still no response, output default message
        if not matched_response:
            print("Robot: I'm sorry, I don't understand.")
            continue

        # Handle variables in the response
        matched_response = replace_variables(matched_response, variables)

        # Output robot's response
        print("Robot:", matched_response)

        # Update variables if necessary
        for var, value in [part.strip().split() for part in matched_response.split("$")[1:]]:
            variables[var] = value

# Example usage
if __name__ == "__main__":
    process_tango_chat("testing.txt")
