# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader, select_autoescape
import json
import os

env = Environment(loader=PackageLoader(__name__, 'templates'), autoescape=select_autoescape(['html', 'xml']), trim_blocks=True, lstrip_blocks=True)
json_dir = 'json'
html_dir = 'songs'
index_fname = 'index.html'

def generate_songs():
    song_dict = []
    json_filenames = sorted([x for x in os.listdir(json_dir) if x.endswith('.json')])

    for filename in json_filenames:
        with open(os.path.join(json_dir, filename)) as f:
            song_data = json.load(f)

        f.close()
        title = filename.split('.')[0]

        template = env.get_template('song.html')

        song_template = template.render(
            title=song_data['title'],
            artist=song_data['artist'],
            sections=song_data['song']['sections'],
            layout=song_data['song']['layout'],
            notes=song_data['notes'],
            link=song_data['link'],
            tags=song_data['tags']
        )
        song_path = os.path.join(html_dir, title + ".html")
        with open(song_path, 'w') as new_html:
            new_html.write(song_template)
        new_html.close()

        song_dict.append({ 'path': os.path.join("songs", (title + '.html')), 'title': song_data['title'], 'artist': song_data['artist'], 'tags': song_data['tags'] })

    sorted_song_dict = sorted(song_dict, key=lambda x: (x['artist'], x['title']));
    return sorted_song_dict

def generate_index(song_dict):
    template = env.get_template(index_fname)

    index_template = template.render(song_dict=song_dict)
    with open(index_fname, 'w') as new_index:
        new_index.write(index_template)
    new_index.close()

if __name__ == "__main__":
    song_dict = generate_songs()
    generate_index(song_dict)
