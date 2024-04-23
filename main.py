from fastapi import FastAPI  # pip install fastapi
from currency import CurrencyChecker
from fastapi.responses import HTMLResponse

app = FastAPI()
currency_checker = CurrencyChecker()


@app.get("/", response_class=HTMLResponse)
def get_currency_rates():
    rates = currency_checker.check_currency()
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Курсы валют</title>
    </head>
    <body>
        <h1>Курсы валют</h1>
        <table>
            <thead>
                <tr>
                    <th>Валюта</th>
                    <th>Курс</th>
                </tr>
            </thead>
            <tbody>
                {"".join([f"<tr><td>{
                         currency}</td><td>{rate}</td></tr>" for currency, rate in rates.items()])}
            </tbody>
        </table>
    </body>
    </html>
    '''
    return html


if __name__ == "__main__":
    import uvicorn  # pip install uvicorn
    PORT = int(input("PORT, default 8000: "))
    HOST = "0.0.0.0"
    uvicorn.run(app.api: : app, host=HOST, port=PORT, reload=True)
