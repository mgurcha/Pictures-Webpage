"""
Name: Manjit Gurcha
Date: 10/30/2017
Course: CST205
Description: Chooses and shows three random images on a webpage from a list of dictionary with 10 values;
When image is clicked, it shows the images and the format, mode, and width/height of it
"""
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
import random
from PIL import Image

image_info = [
    {
        "id" : "34694102243_3370955cf9_z",
        "title" : "Eastern",
        "flickr_user" : "Sean Davis",
        "tags" : ["Los Angeles", "California", "building"]
    },
    {
        "id" : "37198655640_b64940bd52_z",
        "title" : "Spreetunnel",
        "flickr_user" : "Jens-Olaf Walter",
        "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
    },
    {
        "id" : "36909037971_884bd535b1_z",
        "title" : "East Side Gallery",
        "flickr_user" : "Pieter van der Velden",
        "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
    },
    {
        "id" : "36604481574_c9f5817172_z",
        "title" : "Lombardia, september 2017",
        "flickr_user" : "Monica Pinheiro",
        "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
    },
    {
        "id" : "36885467710_124f3d1e5d_z",
        "title" : "Palazzo Madama",
        "flickr_user" : "Kevin Kimtis",
        "tags" : [ "Rome", "Italy", "window", "road", "building"]
    },
    {
        "id" : "37246779151_f26641d17f_z",
        "title" : "Rijksmuseum library",
        "flickr_user" : "John Keogh",
        "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
    },
    {
        "id" : "36523127054_763afc5ed0_z",
        "title" : "Canoeing in Amsterdam",
        "flickr_user" : "bdodane",
        "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
    },
    {
        "id" : "35889114281_85553fed76_z",
        "title" : "Quiet at dawn, Cabo San Lucas",
        "flickr_user" : "Erin Johnson",
        "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
    },
    {
        "id" : "34944112220_de5c2684e7_z",
        "title" : "View from our rental",
        "flickr_user" : "Doug Finney",
        "tags" : ["Mexico", "ocean", "beach", "palm"]
    },
    {
        "id" : "36140096743_df8ef41874_z",
        "title" : "Someday",
        "flickr_user" : "Thomas Hawk",
        "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
    }
]

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    global mylist, title_list, author_list
    counter = 0
    mylist = []
    title_list = []
    author_list = []
    while counter < 3:
        value = random.randint(0,9)
        for im in image_info:
            im = image_info[value]['id']
            for title in im:
                title = image_info[value]['title']
            for author in im:
                author = image_info[value]['flickr_user']
        counter +=1
        mylist.append(im)
        title_list.append(title)
        author_list.append(author)

    return render_template('index.html', img_1 = mylist[0], img_2 = mylist[1], img_3 = mylist[2],
                            title_1 = title_list[0], title_2= title_list[1], title_3 = title_list[2])


@app.route('/picture/<pic>/<int:num>')
def pictures(pic, num):
    path = "static/"
    im = Image.open(path + mylist[num] + ".jpg")
    return render_template('picture.html', pic = pic, id = mylist[num] + ".jpg", author = "by " + author_list[num],
                            mode = im.mode, title = '"' + title_list[num] + '"', format = im.format, width = im.width,
                            height = im.height)
