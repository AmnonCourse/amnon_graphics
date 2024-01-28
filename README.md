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
`set_background_image` - Define a background image for the app.\
`run` - Runs the app

## AmnonButton
The `AmnonButton` object represents a button on the application's gui. 
It contains the data about its positioning on the app's window and the action
that should be executed 

#### To create an `AmnonButton` you need to provide the following parameters:
*position* - an object of type `layouts.Position` that contains the x and y position of the button\
*size* - an object of type `layouts.Size` that contains the width and height of the button\
*on_click* - a `callable` object that will be called when the button is pressed\
*text* - an optional parameter of type `str` that can be provided to add text to the button\
*image_path* - an optional parameter of type `pathlib.Path`. Sets the button's background to the image found in the path

## AmnonLabel
The `AmnonButton` object represents a button on the application's gui.
Labels are similar to button but are not clickable - they are used to display data
or pictures on the application.
#### To create an `AmnonLabel` you need to provide the following parameters:
*position* - an object of type `layouts.Position` that contains the x and y position of the button\
*size* - an object of type `layouts.Size` that contains the width and height of the button\
*text* - an optional parameter of type `str` that can be provided to add text to the button\
*text_color* - an optional parameter of type `str` that can be provided to set the text color of the button\
*image_path* - an optional parameter of type `pathlib.Path`. Sets the button's background to the image found in the path\


## Example Usage:

```python
from amnon_graphics import AmnonApp, AmnonButton, layouts


def on_click():
    print('button_clicked')


app = AmnonApp(name='my_app')
button = AmnonButton(position=layouts.Position(0, 0),
                     size=layouts.Size(100, 50),
                     on_click=on_click,
                     text='Press Here')

app.add_button(button)
app.run()
```

