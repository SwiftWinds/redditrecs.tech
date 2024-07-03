# The Cloud Functions for Firebase SDK to create Cloud Functions and set up triggers.
from firebase_functions import https_fn, options

# The Firebase Admin SDK to access Cloud Firestore.
from firebase_admin import initialize_app

app = initialize_app()


@https_fn.on_request(cors=options.CorsOptions(cors_origins="*", cors_methods=["get"]))
def get_suggestions(req: https_fn.Request) -> https_fn.Response:
    import json
    import requests

    query = req.args.get("q")
    if query is None:
        return https_fn.Response("No query parameter provided", status=400)

    cursor_pos = len(query)
    url_friendly_query = query.replace(" ", "%20")

    url = f"https://www.google.com/complete/search?q={url_friendly_query}%20reddit&cp={cursor_pos}&client=gws-wiz&xssi=t&hl=en&authuser=0&dpr=2"

    res = requests.get(url).text[5:]
    parsed = json.loads(res)[0]

    suggestions = [
        element[0].replace("reddit", "").replace(" </b>", "</b>") for element in parsed
    ]

    return https_fn.Response(json.dumps(suggestions), content_type="application/json")
