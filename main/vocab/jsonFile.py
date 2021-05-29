import os, csv, json

csvFilePath = os.path.join('.', 'dutchApp', 'data', 'vocabulary.csv')
jsonFilePath = os.path.join('.', 'dutchApp', 'data', 'vocabulary.json')


def updateJson(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['polish']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


updateJson(csvFilePath, jsonFilePath)