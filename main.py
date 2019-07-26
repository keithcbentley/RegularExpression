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
Show/Hide trailing newlines
Show pattern info

Testing????

View Model???

Make into an object???


"""
from tkinter import *
from tkinter import ttk
import re


class ViewModel:
    def __init__(self):
        self.root = Tk()
        self.root.title('Regular Expression Playground')
        self.root['borderwidth'] = 5
        self.root['background'] = 'yellow'
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.main_frame = ttk.Frame(self.root)
        self.main_frame['relief'] = 'raised'
        self.main_frame['padding'] = 5
        self.main_frame.grid(column=0, row=0, sticky=(N, S, E, W))
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.rowconfigure(2, weight=1)

        self.input_frame = ttk.Labelframe(self.main_frame, text='Input')
        self.input_frame['relief'] = 'raised'
        self.input_frame['padding'] = 5
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.rowconfigure(0, weight=1)
        self.input_frame.grid(column=0, row=0, sticky=(N, S, E, W))

        self.input_text = Text(self.input_frame, width=40, height=10)
        self.input_text.grid(column=0, row=0, sticky=(N, S, E, W))

        self.re_frame = ttk.Labelframe(self.main_frame, text='Regular Expression')
        self.re_frame['relief'] = 'raised'
        self.re_frame['padding'] = 5
        self.re_frame.columnconfigure(0, weight=1, pad=20)
        self.re_frame.rowconfigure(0, weight=1, pad=20)
        self.re_frame.grid(column=0, row=1, sticky=(N, S, E, W))

        self.re_text = Text(self.re_frame, width=40, height=2)
        self.re_text.grid(column=0, row=0, sticky=(N, S, E, W))

        self.re_execute_frame = ttk.Frame(self.re_frame)
        self.re_execute_frame.grid(column=1, row=0, padx = 5, sticky = (N, S, E, W))

        self.re_execute_button = ttk.Button(self.re_execute_frame, text='Execute')
        self.re_execute_button.grid(column=0, row=0, sticky=(N,E,W), padx=5)

        # There appears to be a bug with the checkbox.  Without a BooleanVar,
        # it always shows as the 'alternate' state, regardless of how the state is set.
        # Using a BooleanVar seems to fix this.
        self.re_ignore_case_var = BooleanVar()
        self.re_ignore_case_checkbox = ttk.Checkbutton(self.re_execute_frame, text='Ignore Case', variable=self.re_ignore_case_var)
        self.re_ignore_case_checkbox.grid(column=0, row=1, sticky=(N, W), padx=5)

        self.re_verbose_var = BooleanVar()
        self.re_verbose_checkbox = ttk.Checkbutton(self.re_execute_frame, text='Verbose', variable=self.re_verbose_var)
        self.re_verbose_checkbox.grid(column=0, row=2, sticky=(N, W), padx=5)

        self.re_multiline_var = BooleanVar()
        self.re_multiline_checkbox = ttk.Checkbutton(self.re_execute_frame, text='Multiline', variable=self.re_multiline_var)
        self.re_multiline_checkbox.grid(column=0, row=3, sticky=(N, W), padx = 5)

        self.re_dotall_var = BooleanVar()
        self.re_dotall_checkbox = ttk.Checkbutton(self.re_execute_frame, text='Dotall', variable=self.re_dotall_var)
        self.re_dotall_checkbox.grid(column=0, row=4, sticky=(N, W), padx=5)

        self.output_frame = ttk.Labelframe(self.main_frame, text='Output')
        self.output_frame['relief'] = 'raised'
        self.output_frame['padding'] = 5
        self.output_frame.columnconfigure(0, weight=1)
        self.output_frame.rowconfigure(0, weight=1)
        self.output_frame.grid(column=0, row=2, sticky=(N, S, E, W))

        self.output_text = Text(self.output_frame, width=40, height=10)
        self.output_text.grid(column=0, row=0, sticky=(N, S, E, W))

    def execute_button_command(self, command):
        self.re_execute_button['command'] = lambda: command(self)

    def output_text_clear(self):
        self.output_text.delete('1.0', END)

    def re_text_get(self):
        re_text = self.re_text.get('1.0', END)
        re_text = re_text[0:-1]  # tk text widget seems to append an extra \n
        return re_text

    def re_ignore_case_get(self):
        return self.re_ignore_case_var.get()

    def re_verbose_get(self):
        return self.re_verbose_var.get()

    def re_multiline_get(self):
        return self.re_multiline_var.get()

    def re_dotall_get(self):
        return self.re_dotall_var.get()

    def input_text_get(self):
        text = self.input_text.get('1.0', END)
        text = text[0:-1]  # tk text widget seems to append an extra \n
        return text

    def output_text_append(self, text):
        self.output_text.insert(END, text)

    def main_loop(self):
        self.root.mainloop()


def none_to_empty(string):
    if string is None:
        return ''
    return string


def none_to_space_none(string):
    if string is None:
        return ' None'
    return ''


def match_to_string(match):
    string = ''
    string += 'Match:\n'
    if match is None:
        string += 'None\n'
        return string
    string += 'Numbered groups:\n'
    group_format = 'group {0}: -->{1}<--{2}\n'
    string += group_format.format(0, none_to_empty(match[0]), none_to_space_none(match[0]))
    string += 'span: ' + str(match.span(0)) + '\n'
    for index, group in enumerate(match.groups()):
        string += group_format.format(index+1, none_to_empty(group), none_to_space_none(group))
        string += 'span: ' + str(match.span(index+1)) + '\n'

    string += 'Named groups:\n'
    named_groups = match.groupdict()
    if len(named_groups) == 0:
        string += 'None\n'
    else:
        for key,value in named_groups.items():
            string += group_format.format(key, none_to_empty(value), none_to_space_none(value))
            string += 'span: ' + str(match.span(key)) + '\n'
    return string


def view_model_regex_flags(view_model):
    flags = 0
    if view_model.re_ignore_case_get():
        flags |= re.IGNORECASE
    if view_model.re_verbose_get():
        flags |= re.VERBOSE
    if view_model.re_multiline_get():
        flags |= re.MULTILINE
    if view_model.re_dotall_get():
        flags |= re.DOTALL
    return flags


def re_execute_button_command(view_model):
    view_model.output_text_clear()  # clear the output text first in case something goes wrong.

    regex = view_model.re_text_get()
    regex_flags = view_model_regex_flags(view_model)
    pattern = re.compile(regex, regex_flags)

    text = view_model.input_text_get()
    for match in pattern.finditer(text):
        match_as_string = match_to_string(match)
        view_model.output_text_append(match_as_string)


app_view_model = ViewModel()
app_view_model.execute_button_command(re_execute_button_command)
app_view_model.main_loop()
