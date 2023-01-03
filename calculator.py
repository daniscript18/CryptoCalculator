import tkinter
import tkinter.messagebox
import webbrowser

window = tkinter.Tk()
window.title("Calculator")
window.geometry("400x400")

difficulty_value = tkinter.StringVar()
hashrate_value = tkinter.StringVar()
reward_value = tkinter.StringVar()
price_value = tkinter.StringVar()
cripto_value = tkinter.StringVar()
currency_value = tkinter.StringVar()

difficulty_tag = tkinter.Label(window, text = "Difficulty per block"); difficulty_tag.grid(row = 0, column = 0)
hashrate_tag = tkinter.Label(window, text = "Miner hashrate"); hashrate_tag.grid(row = 1, column = 0)
reward_tag = tkinter.Label(window, text = "Block reward"); reward_tag.grid(row = 2, column = 0)
price_tag = tkinter.Label(window, text = "Coin price"); price_tag.grid(row = 3, column = 0)
crypto_tag = tkinter.Label(window, text = "Crypto prefix"); crypto_tag.grid(row = 4, column = 0)
currency_tag = tkinter.Label(window, text = "Currency prefix"); currency_tag.grid(row = 5, column = 0)

difficulty_field = tkinter.Entry(window, textvariable=difficulty_value); difficulty_field.grid(row = 0, column = 1)
hashrate_field = tkinter.Entry(window, textvariable=hashrate_value); hashrate_field.grid(row = 1, column = 1)
reward_field = tkinter.Entry(window, textvariable=reward_value); reward_field.grid(row = 2, column = 1)
price_field = tkinter.Entry(window, textvariable=price_value); price_field.grid(row = 3, column = 1)
crypto_field = tkinter.Entry(window, textvariable=cripto_value); crypto_field.grid(row = 4, column = 1); crypto_field.insert(0, "bitcoin")
currency_field = tkinter.Entry(window, textvariable=currency_value); currency_field.grid(row = 5, column = 1); currency_field.insert(0, "dollars")

def calculate(difficulty, hashrate, reward, price, cripto, currency):
    block_time = (difficulty / hashrate)
    coin_hour = ((3600 / block_time) * reward)
    coin_day = (coin_hour * 24)
    earnings_hour = (coin_hour * price)
    earnings_day = (coin_day * price)

    coin_hour_result = tkinter.Label(window, text = f"Earnings per hour in {cripto}: {coin_hour}"); coin_hour_result.grid(row = 7, column = 0)
    coin_day_result = tkinter.Label(window, text = f"Earnings per day in {cripto}: {coin_day}"); coin_day_result.grid(row = 8, column = 0)
    earnings_hour_result = tkinter.Label(window, text = f"Earnings per hour in {currency}: {earnings_hour}"); earnings_hour_result.grid(row = 9, column = 0)
    earnings_day_result = tkinter.Label(window, text = f"Earnings per day in {currency}: {earnings_day}"); earnings_day_result.grid(row = 10, column = 0)

def check_values():
    if difficulty_value.get() == "" or hashrate_value.get() == "" or reward_value.get() == "" or price_value.get() == "" or cripto_value.get() == "" or currency_value.get() == "":
        return tkinter.messagebox.showerror("Error", "No values ​​have been set in one or more fields.")
    else:
        try:
            calculate(float(difficulty_value.get()), float(hashrate_value.get()), float(reward_value.get()), float(price_value.get()), str(cripto_value.get()), str(currency_value.get()))
        except ValueError:
            return tkinter.messagebox.showerror("Error", "One or more variables may have an invalid value.")

button = tkinter.Button(window, text = "Calculate", command = check_values); button.grid(row = 6, column = 1)

github = tkinter.Label(window, text = "Created by Dᥲᥒιᥱᥣ", fg="blue", cursor="hand2"); github.grid(row = 11, column = 0)
github.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/daniscript18"))

window.mainloop()