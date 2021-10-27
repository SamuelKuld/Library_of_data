# Purpose

---

I have been wanting to make something like this for a bit just because I felt like having access to a lot of data and creating a reliable and adaptive data collection and interpretation software would be good.
I'm fairly unprofessional with my code writing skills. This comes mostly from a lack of experience in a work field.
I put in heavy efforts to optimize yet most of the time they're met with similar results as before I optimize.Anyway. I'm mostly just making this to make it and determine if there's any random correlations out there that are repeatable. I'm also planning to implement this into my [website](http://samuelkuld.com) and create simple JSON requests so that people can use it as a nice data collector for certain things.
There are defeinitely things that I could make better, the only thing is that it will take a large amount of time to implement these things. So no matter if you are new to coding or if you would just like to contribute a little, feel free to just optimize small sections or add a completely new one. I'm not that skilled (Especially since no one has taught me how to) at scraping or crawling, so this would be a good learning experience.
But with full expectation for this to go nowhere, here's my first well thought out program.

---

# How to Use

---

### Modules required

#### - [Beautiful Soup for Python 3](https://pypi.org/project/beautifulsoup4/)

#### - [Requests for Python 3](https://pypi.org/project/requests/)

### Use information

- #### Weather:

- - I understand the layout can be a bit daunting. There's a bunch of folders and it seems only 2 utilizable files that are both extremely incomprehensive without the internal files. But upon running a few files you'll notice that nothing will pop up except for the `consumer.py` and `server.py` files.

* These are the two primary files in the program. They take all those subfiles and puts them into data and then saves it. Once that data is collected, it can be read and analyzed by the `consumer.py` file. The `server.py` file pulls the data to be read and "consumed" by `consumer.py`.

* Upon opening `consumer.py` you'll try to read some form of data. This is met with either an error or a message stating that you didn't have any data inputted and that you have to run `server.py`. This is because since you didn't have any data already in the file system, it simply couldn't extrapolate or analyze any given data. In order to resolve this, simply just choose one of the given options in `server.py` and wait for a bit as the data is loaded.

* Once you have data, you're going to notice a few things. For one, lots of statistics. Standard deviations, distance between data points, averages, medians, those sorts of things. Don't be daunted by them. In order to understand what these things are, simply go to one of these sites : [Averages](https://www.skillsyouneed.com/num/averages.html), and [Standard deviations](https://www.scribbr.com/statistics/standard-deviation/). These will help you understand why I'm collecting this data.

* Moving on, you may look at option 4, `weather.py`. Now, I have yet to implement a feature to change the form of address in the interface itself (10/26/2021). If you'd like to have your own area measured in weather, simply go to [this website](https://www.wunderground.com/weather/) and locate your city and state. Then, paste the URL into the variable declaration of `weather_url` somewhere close to the top of `weather/weather.py`.
  &nbsp;It should look like:

* `pythonweather_url = "https://www.wunderground.com/weather/us/ca/alturas"`

* The server should automatically parse out the temperature despite your location being different. If this is not the case, don't hesitate to open an issue.
