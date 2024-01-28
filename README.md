# Spotifish Graphics

This package wrappes pyqt5 and implements an api for
creating a basic gui application.

The main object of the package is `AmnonApp`.
To run your application, create an instance of this class,
configure it according to your needs and run it with the method `run`.

## AmnonApp
`AmnonApp` implements a few basic methods to control the display and functionality of the app:

`add_button` - Receives an `AmnonButton` object and adds it to the app.\
`add_label` - Receives an `AmnonLabel` object and adds it to the app.\
`add_text_box` - Receives an `AmnonTextBox` object and adds it to the app.\

Each of the methods above returns an `element_id` (of type `str`) that is used to reference the element.

`change_label_text` - Changes the text of a label based on its `element_id`.\
`get_textbox_text` - Returns the current text inside of a text-box, based on its `element_id`.\
`remove_element` - Deletes an element (button/label/textbox) based on its `element_id`.

`run` - Runs the app

## AmnonButton
The `AmnonButton` object is used to add clickable buttons to the app.

The action that is performed when pressing the button is defined using the `on_click` parameter.\
Any parameters that you provide the `on_click` function, are defined in a list using the `on_click_params` parameter.

## AmnonLabel
The `AmnonLabel` object is used to display simple text/image labels to the app.

## AmnonTextBox
The `AmnonTextBox` object lets the user enter free text.\
Each change of the text-box's content triggers the function defined in the `on_change` parameter.\
This function receives its first parameter automatically, which contains the `element_id` of the text_box.
To access the current text inside of this text-box, use `app.get_textbox_text(<text_box_id>)`.

## Example Usage:

```python
from amnon_graphics import AmnonApp, AmnonButton, layouts, colors


def print_text(text):
    print(f'text: {text}')


# an app with two simple buttons that print different messages when clicked
app = AmnonApp(
    name='my_app',
    background_color=colors.BLUE
)

first_button = AmnonButton(
    position=layouts.Position(50, 50),
    size=layouts.Size(100, 50),
    on_click=print_text,
    on_click_params=['First text'],
    text='Press Here'
)
second_button = AmnonButton(
    position=layouts.Position(50, 110),
    size=layouts.Size(100, 50),
    on_click=print_text,
    on_click_params=['Second text'],
    text='Press Here'
)

app.add_button(first_button)
app.add_button(second_button)
app.run()
```

