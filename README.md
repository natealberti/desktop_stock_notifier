# desktop_stock_notifier
Alerts user of daily stock return through a windows notification

Quick little application; when run it scrapes the stock prices listed and calculates the average (unweighted) return of them over the course of the day. It retrieves the live share prices with Beautiful Soup, and creates the desktop notification with ToastNotifier. I added another function that lets you see the return from bitcoin as well, that's unimplemented right now.
