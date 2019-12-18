__author__ = 'Nikhil'
import scrapy
from MedIndia.items import MedindiaItem
html_headers = {
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-encoding" : "gzip, deflate, sdch, br",
    "accept-language" : "en-US,en;q=0.8,ms;q=0.6",
    "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
#to csv - scrapy runspider MedIndia.py -o file.csv -t csv

class MedSpider(scrapy.Spider):
    name = 'med'
    #MedindiaSpider.download_delay = 1
    allowed_domains = ["medindia.net"]
    start_urls = [#"https://www.medindia.net/drug-price/brand-index.asp?alpha=a",
                  #"https://www.medindia.net/drug-price/brand-index.asp?alpha=b",
                  #"https://www.medindia.net/drug-price/brand-index.asp?alpha=c",
                  #"https://www.medindia.net/drug-price/brand-index.asp?alpha=d",
                  #"https://www.medindia.net/drug-price/brand-index.asp?alpha=e",
                  #"https://www.medindia.net/drug-price/brand-index.asp?alpha=f",
                  #"https://www.medindia.net/drug-price/brand-index.asp?alpha=g",
                  #"https://www.medindia.net/drug-price/brand-index.asp?alpha=h",
                  #"https://www.medindia.net/drug-price/brand-index.asp?alpha=i",
                  #"https://www.medindia.net/drug-price/brand-index.asp?alpha=j",
                  #"https://www.medindia.net/drug-price/brand-index.asp?alpha=k",
                  #"https://www.medindia.net/drug-price/brand-index.asp?alpha=l",
                  #"https://www.medindia.net/drug-price/brand-index.asp?alpha=m",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=n",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=o",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=p",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=q",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=r",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=s",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=t",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=u",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=v",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=w",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=x",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=y",
                  "https://www.medindia.net/drug-price/brand-index.asp?alpha=z",
                  ]


    def parse(self, response):
        #drug_urls = response.css("table.table-bordered.table > tr > td > a::attr(href)").extract()
        #for letter_href in reponse.css("div.btn-group.btn-group-sm > a::attr(href)"):
        #    next_letter_page =
        for href in response.css("table.table-bordered.table > tr > td > a::attr(href)"):
             #print(href)
             yield response.follow(href, callback=self.parse_details)
        #for drug_url in drug_urls:
        #    drug_url = response.urljoin(drug_url)
        #    print(drug_url)
        #    yield scrapy.Request(url=drug_url,
        #                         #headers=html_headers,
        #                         callback=self.parse_details)
        next_page_url = response.css("a[title='Next Page']::attr(href)").extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            #print(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self,response):
        #print("we are here")
        item = MedindiaItem()

        item['drugName'] = response.css("td > h1::text").extract()
        item['drugForm'] = response.css("td > span::text")[0].extract()
        item['drugGenericName'] = response.css("td > span::text")[1].extract()
        item['price'] = response.css("div.ybox > b::text").extract()
        item['dosage'] = response.css("div.ybox > span > b::text")[0].extract()
        item['basicInfo'] = response.css("div.report-content::text").extract()
        item['conditions'] = response.css("div.caption > b > a::text").extract()
        item['sideEffects'] = response.xpath('.//p[@class="drug-content"][1]/text()').extract()
        item['dosageInfo'] = response.xpath('.//p[@class="drug-content"][2]/text()').extract()
        item['howToTake'] = response.xpath('.//p[@class="drug-content"][3]/text()').extract()
        item['contraindications'] = response.xpath('.//p[@class="drug-content"][4]/text()').extract()
        item['warningsAndPrecautions'] = response.xpath('.//p[@class="drug-content"][5]/text()').extract()
        item['otherPrecautions'] = response.xpath('.//p[@class="drug-content"][6]/text()').extract()
        item['StorageConditions'] = response.xpath('.//p[@class="drug-content"][7]/text()').extract()
        #get data of each drug
        yield item

#    {
#    'Host': 'www.medindia.net',
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'en-US,en;q=0.5',
#    'Referer': 'https://www.medindia.net/drug-price/brand-index.asp?alpha=a',
#    'Accept-Encoding': 'gzip, deflate, br',
#    #'Cookie': 'ASPSESSIONIDCASCCQQB=LAIEMMHCGFGJCIOHMDFGBBLP; ASPSESSIONIDACTARTCD=AEAGKDKCJADJAGILECIGFDDN; ASPSESSIONIDCATDSQBC=FGNMNKICLBCAIFIDJGDJGALL; ASPSESSIONIDCASBCSQD=LMEDKCOCNNJHPFKFDFLMAGME; ASPSESSIONIDCATBTTBC=AMLHCGIDDLAKKOFDLNDJHFCJ',
#    'Connection': 'keep-alive'
#   }