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
from tkinter import ttk, filedialog
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

        self.input_file_frame = ttk.Frame(self.input_frame)
        self.input_file_frame.grid(column=1, row=0, padx=5, sticky=(N, S, E, W))

        self.input_file_button = ttk.Button(self.input_file_frame, text='File')
        self.input_file_button.grid(column=0, row=0, sticky=(N, E, W), padx=5)

        self.re_frame = ttk.Labelframe(self.main_frame, text='Regular Expression')
        self.re_frame['relief'] = 'raised'
        self.re_frame['padding'] = 5
        self.re_frame.columnconfigure(0, weight=1, pad=20)
        self.re_frame.rowconfigure(0, weight=1, pad=20)
        self.re_frame.grid(column=0, row=1, sticky=(N, S, E, W))

        self.re_text = Text(self.re_frame, width=40, height=2)
        self.re_text.grid(column=0, row=0, sticky=(N, S, E, W))

        self.re_execute_frame = ttk.Frame(self.re_frame)
        self.re_execute_frame.grid(column=1, row=0, padx=5, sticky=(N, S, E, W))

        self.re_execute_button = ttk.Button(self.re_execute_frame, text='Execute')
        self.re_execute_button.grid(column=0, row=0, sticky=(N, E, W), padx=5)

        # There appears to be a bug with the checkbox.  Without a BooleanVar,
        # it always shows as the 'alternate' state, regardless of how the state is set.
        # Using a BooleanVar seems to fix this.
        self.re_ignore_case_var = BooleanVar()
        self.re_ignore_case_checkbox = ttk.Checkbutton(
            self.re_execute_frame, text='Ignore Case', variable=self.re_ignore_case_var)
        self.re_ignore_case_checkbox.grid(column=0, row=1, sticky=(N, W), padx=5)

        self.re_verbose_var = BooleanVar()
        self.re_verbose_checkbox = ttk.Checkbutton(
            self.re_execute_frame, text='Verbose', variable=self.re_verbose_var)
        self.re_verbose_checkbox.grid(column=0, row=2, sticky=(N, W), padx=5)

        self.re_multiline_var = BooleanVar()
        self.re_multiline_checkbox = ttk.Checkbutton(
            self.re_execute_frame, text='Multiline', variable=self.re_multiline_var)
        self.re_multiline_checkbox.grid(column=0, row=3, sticky=(N, W), padx=5)

        self.re_dotall_var = BooleanVar()
        self.re_dotall_checkbox = ttk.Checkbutton(
            self.re_execute_frame, text='Dotall', variable=self.re_dotall_var)
        self.re_dotall_checkbox.grid(column=0, row=4, sticky=(N, W), padx=5)

        self.re_operation_frame = ttk.Frame(self.re_frame)
        self.re_operation_frame.grid(column=2, row=0, padx=5, sticky=(N, S, E, W))

        self.match_operation_value = 'match'
        self.fullmatch_operation_value = 'fullmatch'
        self.search_operation_value = 'search'
        self.finditer_operation_value = 'finditer'

        self.operation_var = StringVar()
        self.operation_var.set(self.match_operation_value)

        self.match_button = ttk.Radiobutton(self.re_operation_frame, text='Match', variable=self.operation_var,
                                            value=self.match_operation_value)
        self.match_button.grid(column=0, row=0, sticky=(W,))

        self.fullmatch_button = ttk.Radiobutton(self.re_operation_frame, text='Fullmatch', variable=self.operation_var,
                                                value=self.fullmatch_operation_value)
        self.fullmatch_button.grid(column=0, row=1, sticky=(W,))

        self.search_button = ttk.Radiobutton(self.re_operation_frame, text='Search', variable=self.operation_var,
                                             value=self.search_operation_value)
        self.search_button.grid(column=0, row=2, sticky=(W,))

        self.finditer_button = ttk.Radiobutton(self.re_operation_frame, text='Finditer', variable=self.operation_var,
                                               value=self.finditer_operation_value)
        self.finditer_button.grid(column=0, row=3, sticky=(W,))

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

    def file_button_command(self, command):
        self.input_file_button['command'] = lambda: command(self)

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

    def input_text_set(self, text):
        self.input_text.delete('1.0', END)
        self.input_text.insert(END, text)

    def output_text_clear(self):
        self.output_text.delete('1.0', END)

    def output_text_append(self, text):
        self.output_text.insert(END, text)

    def do_match(self):
        return self.operation_var.get() == self.match_operation_value

    def do_fullmatch(self):
        return self.operation_var.get() == self.fullmatch_operation_value

    def do_search(self):
        return self.operation_var.get() == self.search_operation_value

    def do_finditer(self):
        return self.operation_var.get() == self.finditer_operation_value

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


class ViewModelAdapter:
    def __init__(self, view_model):
        self.view_model = view_model
        self.output_string = None

    def regex_flags(self):
        flags = 0
        if self.view_model.re_ignore_case_get():
            flags |= re.IGNORECASE
        if self.view_model.re_verbose_get():
            flags |= re.VERBOSE
        if self.view_model.re_multiline_get():
            flags |= re.MULTILINE
        if self.view_model.re_dotall_get():
            flags |= re.DOTALL
        return flags

    def begin_output(self):
        self.view_model.output_text_clear()
        self.output_string = ''

    def append_output(self, string):
        self.output_string += string

    def end_output(self):
        self.view_model.output_text_append(self.output_string)

    def match_to_string(self, match):
        match_start_string = ':::Match start\n'
        match_end_string = ':::Match end\n'
        numbered_start_string = '  :::Numbered groups start\n'
        numbered_end_string = '  :::Numbered groups end\n'
        named_start_string = '  :::Named groups start\n'
        named_end_string = '  :::Named groups end\n'
        string = ''
        if match is None:
            string += match_start_string
            string += '  None\n'
            string += match_end_string
            return string
        string += match_start_string
        string += numbered_start_string
        group_format = '    group {0}: -->{1}<--{2}\n'
        span_format = '    span: {0}\n'
        string += group_format.format(0, none_to_empty(match[0]), none_to_space_none(match[0]))
        string += '    span: ' + str(match.span(0)) + '\n'
        for index, group in enumerate(match.groups()):
            string += group_format.format(index + 1, none_to_empty(group), none_to_space_none(group))
            string += span_format.format(str(match.span(index + 1)))
        string += numbered_end_string

        string += named_start_string
        named_groups = match.groupdict()
        if len(named_groups) == 0:
            string += '    None\n'
        else:
            for key, value in named_groups.items():
                string += group_format.format(key, none_to_empty(value), none_to_space_none(value))
                string += span_format.format(str(match.span(key)))
        string += named_end_string
        string += match_end_string
        return string

    def output_match(self, match):
        match_as_string = self.match_to_string(match)
        self.append_output(match_as_string)


def re_execute_button_command(view_model):
    view_model_adapter = ViewModelAdapter(view_model)
    view_model_adapter.begin_output()

    regex = view_model.re_text_get()
    regex_flags = view_model_adapter.regex_flags()
    pattern = re.compile(regex, regex_flags)

    text = view_model.input_text_get()

    if view_model.do_match():
        match = pattern.match(text)
        view_model_adapter.output_match(match)

    if view_model.do_fullmatch():
        match = pattern.fullmatch(text)
        view_model_adapter.output_match(match)

    if view_model.do_search():
        match = pattern.search(text)
        view_model_adapter.output_match(match)

    if view_model.do_finditer():
        for match in pattern.finditer(text):
            view_model_adapter.output_match(match)

    view_model_adapter.end_output()


def file_button_command(view_model):
    file_name = filedialog.askopenfilename()
    file = open(file_name, 'r')
    contents = file.read()
    view_model.input_text_set(contents)


def main():
    app_view_model = ViewModel()
    app_view_model.execute_button_command(re_execute_button_command)
    app_view_model.file_button_command(file_button_command)
    app_view_model.main_loop()


main()
