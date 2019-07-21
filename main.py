"""


Input Text
Regular Expression
Result

Input text window, input text from file, get input text from file directly
Regular expression, regular expression options, match command button
Output text window, options for output results

Search, Match, Fullmatch, Split, Findall, Sub, Subn functionality options (radio buttons)

Display pattern information after compile

Escape functionality in Regular Expression section.  Show escaped string.

Verbose flag
Debug flag
IgnoreCase flag
Multiline flag
Dotall flag

No match output result separate from output text box.
Displaying match results will become more complex.
Match Expand results

Compile by default

Testing????

View Model???

Make into an object???


"""
from tkinter import *
from tkinter import ttk
import re

root = Tk()
root.title('Regular Expression Playground')
root['borderwidth'] = 5
root['background'] = 'yellow'
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

main_frame = ttk.Frame(root)
main_frame['relief'] = 'raised'
main_frame['padding'] = 5
main_frame.grid(column=0, row=0, sticky=(N,S,E,W))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)

input_frame = ttk.Labelframe(main_frame, text='Input')
input_frame['relief'] = 'raised'
input_frame['height'] = 50
input_frame['padding'] = 5
input_frame.columnconfigure(0, weight=1)

input_text = Text(input_frame, width=40, height=10)
input_text.grid(column=0, row=0, sticky=(N,S,E,W))


re_frame = ttk.Labelframe(main_frame, text='Regular Expression')
re_frame['relief'] = 'raised'
re_frame['height'] = 50
re_frame.columnconfigure(0, weight=1, pad=20)
re_frame.rowconfigure(0, pad=20)

re_text = Text(re_frame, width=40, height=2)
re_text.grid(column=0, row=0, sticky=(N,S,E,W))

re_execute_button = ttk.Button(re_frame, text='Execute')
re_execute_button.grid(column=1, row=0, sticky=(E,), padx=5)

output_frame = ttk.Labelframe(main_frame, text='Output')
output_frame['relief'] = 'raised'
output_frame['height'] = 50
output_frame.columnconfigure(0, weight=1)

output_text = Text(output_frame, width=40, height=10)
output_text.grid(column=0, row=0, sticky=(N,W,E,W))



input_frame.grid(column=0, row=0, sticky=(N,S,E,W))
re_frame.grid(column=0, row=1, sticky=(N,S,E,W))
output_frame.grid(column=0, row=2, sticky=(N,S,E,W))


def match_to_string(match):
    if match is None:
        return None
    str = ''
    print('match[0] len: ', len(match[0]))
    str = str + match[0] + '\n'
    for group in match.groups():
        str = str + 'group: ' + group + '\n'
    return str



def re_execute_button_command():
    # clear output results first
    output_text.delete('1.0', END)

    # make sure we have a valid regex
    regex = re_text.get('1.0', END)
    regex = regex[0:-1] # tk text widget seems to append an extra \n
    pattern = re.compile(regex)

    # get the input string
    text = input_text.get('1.0', END)
    text = text[0:-1]   # tk text widget seems to append an extra \n
    print('text len', len(text))
    # execute the regex
    print('execute')
    for match in pattern.finditer(text):
        match_as_string = match_to_string(match)
        # output the results
        if match_as_string is None:
            match_as_string = 'No match'
        output_text.insert(END, match_as_string)

re_execute_button['command'] = re_execute_button_command



root.mainloop()