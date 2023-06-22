import asyncio
from pyppeteer import launch
from sys import argv


async def main(url='http://localhost:5000/'):
    print("aaaaaaaaaaaaaa")

    browser = await launch(headless=True,    handleSIGINT=False,
                           handleSIGTERM=False,
                           handleSIGHUP=False, executablePath="/usr/bin/chromium", args= ['--no-sandbox'])
    print("aaaaaaaaaaaaaa")

    page = await browser.newPage()

    await page.goto('http://localhost:5000/login')

    await page.type('input[name="username"]', 'admin')
    await page.type('input[name="password"]', 'su3r5ecr3tp4ssw0rd85246')

    await page.click('#login')
    await page.goto(url)
    await asyncio.sleep(1)
    print("aaaaaaaaaaaaaa")
    await browser.close()


def run_pupp(url):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(url))
    loop.close()
