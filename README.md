# ExecBox - Execute Python code from inside your Streamlit apps!

Execbox is basically a text editor plus `exec()`.


## Installation

First install Streamlit (of course!) then pip-install this library:

```bash
pip install streamlit
pip install st-execbox
```


## Example usage

```python
import streamlit as st
from st_execbox import execbox


# Draw a text editor and a "Run" button. When you press "Run", the code in the editor executes!
execbox()


# Makes the code run automatically on each keystroke.
execbox(autorun=False)


# Draw an execbox with some initial text.
execbox("""
a = 10
b = 20
st.write(a + b)
""")

```


## Parameters

The `execbox()` function accepts any of the following arguments:

- **body** (str. default: '')

    The initial code to show in the execbox.

- **button_label** (str. default: 'Run')

    The label to use for the "Run" button.

- **autorun** (bool. default: False)

    Whether the code should execute with each keystroke.

- **height** (int or None. default: None)

    The height of the execbox, in pixels. If `None`, calculates the height smartly to fill the
    content and a couple more lines.

- **line_numbers** (bool. default: False)

    Whether to show line numbers.

- **key** (str or None. default: None)

    An optional string to use as the unique key for the widget. If this is omitted, a key will
    be generated for the widget based on its content. Multiple widgets of the same type may not
    share the same key.

## To-do

Just one to-do:

- [ ] Write tests! Contributions accepted :wink:
