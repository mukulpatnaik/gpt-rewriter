import tkinter as tk
import tkinter.simpledialog as simpledialog
import openai

# Use the openai API key
openai.api_key = "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"

# Set the model to use
model = "text-davinci-003"

# Create the root window
root = tk.Tk()
root.title("Question Answering App")

# Create a frame to hold the left and right text areas
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Create a text area on the left
left = tk.Text(frame, bd=1, relief="sunken")
left.pack(side="left", fill="both", expand=True)

# Create a text area on the right
right = tk.Text(frame, bd=1, relief="sunken")
right.pack(side="right", fill="both", expand=True)

# Create a function to get the response from the model
def get_response():
    # Get the context from the left text area
    context = left.get("1.0", "end")

    # Get the prompt from the user
    prompt = simpledialog.askstring("Prompt", "Question:")
    prompt = "Given the context:\n" + context + "\nAnswer the following question:\n" + prompt + "\n"

    # Get the response from the model
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=500,
        n=1,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # Display the response in the right text area
    right.insert("1.0", response["choices"][0]["text"])

# Create a button to submit the text
button = tk.Button(root, text="Submit", command=get_response)
button.pack()

# Set the window size and position
root.geometry("800x600+300+300")

# Run the main event loop
root.mainloop()