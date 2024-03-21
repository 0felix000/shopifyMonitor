# shopifyMonitor
Fully functional shopify monitor / product scraper with many additional features

## Features:

> Supporting multiple Stores at a time
> 
> full proxy support
> 
> Providing direct add-to-cart links
> 
> supporting multiple discord webhooks to prevent ratelimiting - just add "file" as value for webhook in json and the webhooks from your webhook file will be used
> 
> password page detection
> 
> "pingOnStartup" set to true will make it possible to scrape all loaded products + get the ATC Links

### I wrote this code about 1 year ago and found it rn when working on a school project, there are some things I would do different now (script is still fully functional):
> add localhost support - shopify ratelimiting seems not to be too big of an problem with high delay
> 
> dont use discordhook libraby, just send post request
> 
> redesign the webhook layout
> 
> add support for product restocks, currently only newly added products are pinged
