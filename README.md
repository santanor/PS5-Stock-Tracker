# PS5 Stock Tracker

This is just a nice little project to track the PS5 stock in some of the stores that I'd buy it from. It runs on the terminal and it reports the stock availability of both PS5 versions (Even though I'm only after the Disk one :P )

I have connected my raspberry pi to this thing and it'll buzz if the PS5 is ever in stock. At this point I've lost **almost** all hope.


## How this works
There are 3 parts to this project, only one of which is included in this repo given that the other 2 need no code at all. 
* Python and [Scrapy](https://scrapy.org)
* [Splash, a javascript rendering service](https://github.com/scrapinghub/splash)
* And [Docker](http://Docker.com) (I don't think you need a link for this but consistency, amirite)

#### Scrapy
Scrapy is used to create spiders that crawl and monitor the sites I'm interested in, a simple xpath takes me to the desired element that I use to check the stock. Generally that'd be the `Add to Cart` button which usually says something along the lines of `Out of Stock`. So simply evaluating that does the trick

#### Splash
Some (most) modern websites use `Javascript` to render the content so `Scrapy` falls in a bit short when it comes to that, when a spider hits the site it's welcomed with a very basic blank (and maybe some branding) site. 
Splash solves this problem as it's a scriptable javascript rendering service that can return the result of a request. 

So the idea is simple, instead of letting `Scrapy` send the request and crawl the result, I use `Splash` to send the request, wait for it to render and return the result to `Scrapy` for it to crawl as if it was a regular site. 

**It works beautifully**

#### Docker
This is just used to host Splash and have it there out of mind :) 
