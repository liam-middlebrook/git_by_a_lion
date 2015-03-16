#!/bin/env python
import json
import pygal
import pprint
import sys

def generate_html():
    html_string = """
<!DOCTYPE html>
<html>
  <head>
    <!-- ... -->
  </head>
  <body>
    <figure>
      <embed type="image/svg+xml" src="author_tot_knowledge.svg" />
    </figure>
    <figure>
      <embed type="image/svg+xml" src="author_tot_risk.svg" />
    </figure>
    <figure>
      <embed type="image/svg+xml" src="file_tot_knowledge.svg" />
    </figure>
    <figure>
      <embed type="image/svg+xml" src="file_tot_risk.svg" />
    </figure>
  </body>
</html>
"""

    with open("index.html", "w+") as text_file:
        text_file.write(html_string)


def generate_pie(data, title, stat_str, out_file):
    list_data = []
    for name, stats in data.iteritems():
        if "\n" in name:
            continue
        list_data.append((name, stats[stat_str]))

    list_data.sort(key=lambda tup: tup[1], reverse=True)
    del list_data[25:]

    chart = pygal.Pie()
    chart.title = title
    for k in list_data:
        chart.add(k[0], k[1])

    chart.render_to_file(out_file)


def file_stat(data, stat_str):
    stat_data = []

    file_list = data["files"]

    for f in file_list:
        stat_data.append((f["name"], f[stat_str]))
    for f_dir in data["dirs"]:
        stat_data.extend(file_stat(f_dir, stat_str))

    return stat_data


def file_pie(file_data, title, stat_str, out_file):
    file_stats = []
    
    file_stats = file_stat(file_data, stat_str)
    
    file_stats.sort(key=lambda tup: tup[1], reverse=True)
    del file_stats[25:]

    chart = pygal.Pie()
    chart.title = title

    for k in file_stats:
        chart.add(k[0], k[1])

    chart.render_to_file(out_file)

def main():
    if len(sys.argv) <= 1:
        print "Error, must supply path of summary.json!"
        sys.exit(1)

    with open(sys.argv[1]) as data:
        gbab_data = json.load(data)
    
    author_risks = gbab_data["author_risks"]
    file_risks = gbab_data["root"]
    
    generate_pie(
        author_risks,
        "Estimated Total Knowledge by Author",
        "tot_knowledge",
        "author_tot_knowledge.svg"
    )
    
    generate_pie(
        author_risks,
        "Estimated Total Risk by Author",
        "tot_risk",
        "author_tot_risk.svg"
    )
    
    file_pie(
        file_risks,
        "Estimated Total Knowledge Per File",
        "tot_knowledge",
        "file_tot_knowledge.svg"
    )
    
    file_pie(
        file_risks,
        "Estimated Total Risk Per File",
        "tot_risk",
        "file_tot_risk.svg"
    )

    generate_html()

if __name__ == "__main__":
    main()
