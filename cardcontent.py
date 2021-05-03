
cardContent = {
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.1",
    "body": [
        {
            "type": "TextBlock",
            "text": "Some ways to collect user input",
            "size": "medium",
            "weight": "bolder"
        },
        {
            "type": "TextBlock",
            "text": "This **Input.Text** element collects some free from "
                    "text. Designers can use attributes like `isMutiline`, "
                    "`maxLength` and `placeholder to shape the way that users "
                    "enter text in a form.",
            "wrap": True
        },
        {
            "type": "Input.Text",
            "placeholder": "Text Field",
            "style": "text",
            "maxLength": 0,
            "id": "TextFieldVal"
        },
        {
            "type": "TextBlock",
            "text": "This **Input.Number** element collects a number. "
                    "Designers can use the `max`, `min` and `placeholder` "
                    "attributes to control the input options.",
            "wrap": True
        },
        {
            "type": "Input.Number",
            "placeholder": "Number",
            "min": -5,
            "max": 5,
            "id": "NumberVal"
        },
        {
            "type": "TextBlock",
            "text": "The **Input.ChoiceSet** element provides a variety of "
                    "ways that users can choose from a set of options. This "
                    "is the default view, but designers can use the `style` "
                    "and `isMutiSelect` attributes to change the way it "
                    "works. The choices are defined in an array attribute "
                    "called `choices`.",
            "wrap": True
        },
        {
            "type": "Input.ChoiceSet",
            "id": "ColorChoiceVal",
            "value": "Red",
            "choices": [
                {
                    "title": "Red",
                    "value": "Red"
                },
                {
                    "title": "Blue",
                    "value": "Blue"
                },
                {
                    "title": "Green",
                    "value": "Green"
                }
            ]
        },
        {
            "type": "Input.Toggle",
            "title": "This Input.Toggle element gets a true/false input.",
            "id": "Toggle",
            "wrap": True,
            "value": "false"
        }
    ],
    "actions": [
        {
            "type": "Action.Submit",
            "title": "Submit",
            "data": {
                "formDemoAction": "Submit"
            }
        }
    ]
}
