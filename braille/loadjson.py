def return_gist_id():
    return {
        "hin": "a467db04321a29414cd87e04b0c901d1"
    }


def download_json(lang):
    import json
    from collections import OrderedDict
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    http = urllib3.PoolManager()
    try:
        res = json.loads(http.request('GET', 'https://api.github.com/gists/' +
                                      return_gist_id()[lang], headers={'user-agent': 'brailler'}).data.decode("utf-8").replace("'", '"'), object_pairs_hook=OrderedDict)
        data = res["files"][list(res["files"].keys())[0]]['content']
        with open('{}_to_brl.json'.format(lang), 'w') as outfile:
            outfile.write(data)
    except Exception as e:
        print("There was an error downloading . .")
        print(e)


def get_json(lang="hin"):
    import json
    import os
    from collections import OrderedDict
    import urllib3
    try:
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, "{}_to_brl.json".format(lang)) 
        openfile = open(file_path, "r", encoding="utf8")
        jsonfile = json.loads(
            openfile.read(), object_pairs_hook=OrderedDict)[0]
        return jsonfile
    except FileNotFoundError:
        print("Language pack {} not found. Downloading...".format(lang))
        download_json(lang)
        openfile = open("{}_to_brl.json".format(lang), "r")
        jsonfile = json.loads(
            openfile.read(), object_pairs_hook=OrderedDict)[0]
        return jsonfile
