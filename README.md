# Introduction 

This application will scrap stock data from [Business Insider][1]

To run the application run ``` scrapy crawl spider-name ``` in _Anaconda terminal_





# Create a project

```
    scrapy startproject project-name
```

# Run spider

```
    scrapy crawl spider-name
    scrapy crawl spider-name -o output-file-name.json
    scrapy crawl spider-name -o output-file-name.jl #json lines
```

# Extracting data using Scrapy shell

``` 
    scrapy shell 'http://url.toscrape.com/page/1/'

 ```

 [1]:  https://markets.businessinsider.com/index/components/s&p_500 "Business Insider"