import random
import pyttsx3
import speech_recognition as sr
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

# Function to parse definitions from the TangoChat file
def parse_definitions(line):
    if line.startswith("~"):
        parts = line.strip().split(":")
        if len(parts) == 2:
            variable = parts[0][0:].strip()
            options = []
            temp = ""
            val = False
            for opt in parts[1][1:-1].split():
                if opt.startswith("\""):
                    temp += opt.strip("\"")
                    temp += " "
                    val = True
                    continue
                if val == True:
                    val = False
                    temp += opt.strip("\"")
                    options.append(temp)
                    continue
                options.append(opt.strip("["))
            return variable, options
    return None, None

# Function to parse conversation rules from the TangoChat file
def parse_rule(line, count):
    parts = line.strip().split(":")
    if len(parts) == 3 and parts[0].lower().startswith("u"):
        user_input = parts[1].strip().lower().strip("(").strip(")")
        temp = ""
        val = False
        responses = []
        if parts[2].startswith("[") != True:
            responses.append(parts[2].strip())
        else:
            for resp in parts[2][1:-1].split():
                if resp.startswith("\""):
                    temp += resp.strip("\"")
                    temp += " "
                    val = True
                    continue
                if val == True:
                    val = False
                    temp += resp.strip("\"")
                    responses.append(temp)
                    continue
                responses.append(resp.strip())
        return user_input, responses
    print(line + "\n You have an error on line" + " " + str(count))
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
        count = 0
        for line in file:
            count += 1
            # Ignore comments
            if line.strip().startswith('#'):
                continue

            # Parse definitions
            variable, options = parse_definitions(line)
            if variable and options:
                definitions[variable] = options
                continue

            # Parse conversation rules
            user_input, responses = parse_rule(line, count)

            if user_input and responses:
                rules[user_input] = responses
                continue

    # Handle conversation
    name = "I dont't know"
    age = "I dont know"
    namePatterns = []
    agePatterns = []
    temp = False
    while True:
        with sr.Microphone() as source:
            r= sr.Recognizer()
            r.adjust_for_ambient_noise(source)
            r.dyanmic_energythreshhold = 3000
            try:
                print("Human: ", end="")
                user_input = r.listen(source)            
                user_input = r.recognize_google(user_input)
                print(user_input)
            except sr.UnknownValueError:
                print("Don't know that word")
        user_input = input("User: ").strip()
        if not user_input:
            continue
        nameTest = False
        ageTest = False
        matched_response = ""
        if "my name is" in user_input:
            for x in user_input.split():
                if x == "is":
                    temp = True
                    continue
                if temp == True:
                    name = x
                    temp = False
        elif "years old" in user_input:
            for x in user_input.split():
                if x == "am":
                    temp = True
                    continue
                if temp == True:
                    age = x
                    temp = False
        # Check if user input matches any defined rule
        for pattern, responses in rules.items():
            if "$name" in responses[0]:
                namePatterns.append(pattern)
            if "$age" in responses[0]:
                agePatterns.append(pattern)
            while definitions.get(pattern) != None:
                if user_input in definitions.get(pattern):
                    matched_response = random.choice(responses)
                    break
                else:
                    break
            if user_input == pattern:
                if "$name" in responses[0]:
                    matched_response = name
                    break
                if "$age" in responses[0]:
                    matched_response = age
                    break
                if responses[0] in definitions.keys():
                    matched_response = random.choice(definitions.get(responses[0]))
                    break
                matched_response = random.choice(responses)
                break
        if matched_response == "":
            for pattern, responses in rules.items():
                if "$name" in responses[0].split():
                        for x in namePatterns:
                            if ' '.join(user_input.split()[:3]) in ' '.join(x.split()[:3]):
                                nameTest = True
                        if nameTest == True:
                            for x in responses[0].split():
                                if x == "$name":
                                    matched_response += name
                                    continue
                                matched_response += x + " "
                            break
                if "$age" in responses[0].split():
                    for x in agePatterns:
                        if ' '.join(user_input.lower().split()[:2]) in ' '.join(x.split()[:2]):
                            ageTest = True
                    if ageTest == True:
                        for x in responses[0].split():
                            if x == "$age":
                                matched_response += age + " "
                                continue
                            matched_response += x + " "
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
        SpeakText(matched_response)

# Example usage
if __name__ == "__main__":
    process_tango_chat("testing.txt")
