from urllib.request import urlopen
import json

data = json.loads(urlopen("https://api.github.com/repos/BlueArchiveArisHelper/BAAH/releases/latest").read())
tag_name = data["tag_name"]
body = data["body"]

with open("version.json", "r") as f:
    context = json.loads(f.read())

if tag_name == context["version"]:
    print("No change")
    exit(1)
else:
    context["version"] = str(tag_name).replace("BAAH","")
    context["context"] = str(body)

    with open("version.json", "w") as f:
        f.write(json.dumps(context))

    exit(0)