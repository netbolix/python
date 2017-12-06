# _*_ coding:utf-8 _*_
#!/usr/bin/env python3.5

import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    

    name = 'git-hub_shiyanlou'

#    def start_requests(self):
#        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'

 #       urls = (url_tmpl.format(i) for i in range(1,23))

 #       for url in urls:
 #           yield scrapy.Request(url=url,callback=self.parse)
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5)) 

    def parse(self,response):
        
        for repo in response.css('div#user-repositories-list'):
            yield{
                    'name': repo.css('div.mb-1 a::text').extract_first(),
                    'update_time': repo.xpath('.//relative-time/@datetime').extract_first()
                }



