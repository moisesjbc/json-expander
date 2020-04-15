# json-expander

## Use example

        PYTHONPATH=.. python3 expand_json.py test.json out.json --var "name=Jon Doe" --var "n=3"
    
Where test.json:

        {
            "people": ["@repeat", "$n", {
                "name": "$name",
                "age": 17
            }]
        }
        
Output (`out.json`):

        {
            "people": [
                {
                    "name": "Jon Doe",
                    "age": 17
                },
                {
                    "name": "Jon Doe",
                    "age": 17
                },
                {
                    "name": "Jon Doe",
                    "age": 17
                }
            ]
        }
