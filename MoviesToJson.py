import csv
import re

csvfile = open('ml-latest-small/movies.csv', 'r', encoding="utf8")

jsonOutput = open("demofile2.json", "a")

reader = csv.DictReader( csvfile )
for movie in reader:
        jsonOutput.write("{ \"create\" : { \"_index\": \"movies\", \"_id\" : \"" + movie['movieId']+ "\" } }\n")
        title = re.sub(" \(.*\)$", "", re.sub('"','', movie['title']))
        year = movie['title'][-5:-1]
        if (not year.isdigit()):
            year = "2016"
        genres = movie['genres'].split('|')
        jsonOutput.write("{ \"id\": \"" + movie['movieId'] + "\", \"title\": \"" + title + "\", \"year\":" + year + ", \"genre\":[")
        for genre in genres[:-1]:
            jsonOutput.write("\"" + genre + "\",")
        jsonOutput.write("\"" + genres[-1] + "\"")
        jsonOutput.write("] }\n")

jsonOutput.write("\n")
jsonOutput.close()