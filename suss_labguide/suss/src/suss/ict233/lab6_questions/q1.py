import re
import requests
from ...dev import x
from learntools.core import *
import os
import subprocess

class Question1(CodingProblem):

    def produce_expected(code):
        
        # clone .hot_100_mar
        clone = "git clone https://github.com/suss-vli/hot_100_mar.git .hot_100_mar"
        home_directory = os.path.expanduser('~')  # Get the user's home directory
        test_folder_directory = os.path.join(home_directory + "/ilabguide/.hot_100_mar")

        if os.path.isdir(test_folder_directory) == False:
            os.chdir(home_directory + "/ilabguide")
            subprocess.run(clone.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # remove git files
            os.chdir(home_directory + "/ilabguide/.hot_100_mar")
            os.remove(".gitignore")
            os.system("rm -rf .git")

        # change content of hot_100_list_spider.py
        os.chdir(home_directory + "/ilabguide/.hot_100_mar/hot_100_mar/spiders")
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, "hot_100_list_spider.py")

        # Write the new content to the file
        with open(file_path, 'w') as file:
            file.truncate(0)
            file.write(code)
            file.close()

        # check if hot100.json exists and create/truncate
        os.chdir(home_directory + "/ilabguide/.hot_100_mar")  # Change the working directory to the home directory
        current_directory = os.getcwd()

        hot100_file_path = os.path.join(current_directory, "hot100.json")
        if os.path.exists(hot100_file_path):
            with open(hot100_file_path, 'w') as file:
                file.truncate(0)  # Clears the content by truncating the file
 
        subprocess.run(["scrapy", "crawl", "hot100_list", "-o", "hot100.json"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # For consistency, still use this testcase but put `hot_100_mar` in it. please loop through one test case
    _test_cases = [
        ("""import scrapy

#### create a parse method and define the relevant xpaths to extract the data that we want

class Hot100Item(scrapy.Item):
    rank = scrapy.Field()
    song = scrapy.Field()
    artist = scrapy.Field()


#### create a parse method and define the relevant xpaths to extract the data that we want

class Hot100Spider(scrapy.Spider):
    name = 'hot100_list'
    allowed_domains = ['www.billboard.com']
    start_urls = ["https://www.billboard.com/charts/hot-100/"]

    def parse(self, response):
        list_100 = response.xpath('//div[@class="o-chart-results-list-row-container"]') 
        items = []
        for one_song in list_100:
            one_song_rank = one_song.xpath('descendant-or-self::span[@class = "c-label  a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"]/text()')[0].extract()
            one_song_lower = one_song.xpath('descendant-or-self::h3[1]')
            song_name = one_song_lower.xpath('text()')[0].extract()
            artist_name   = one_song_lower.xpath('following-sibling::span[1]/text()')[0].extract()
            items.append(Hot100Item(rank=one_song_rank,song=song_name,artist = artist_name))
        return items""")
    ]

    def check(self):
        for test in self._test_cases:
            Question1.produce_expected(test)

            home_directory = os.path.expanduser('~')  # Get the user's home directory
            os.chdir(home_directory + "/ilabguide")  # Change the working directory to the home directory

            folder_path = os.path.join(os.getcwd() + "/hot_100_mar")
            expected_folder = os.path.join(os.getcwd() + "/.hot_100_mar")
            x.grading_directory4(folder_path, expected_folder)