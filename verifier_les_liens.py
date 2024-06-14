#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from random import choice
from string import ascii_letters, digits
import telebot

bot = telebot.TeleBot('Ключ бота')

headers = {"User-Agent":
               "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

liens_de_travail = './liens_de_travail.txt'
def generate_random_string():
    letters = ascii_letters + digits
    return ''.join(choice(letters) for _ in range(16))


@bot.message_handler(content_types=['text'])

def start_message(message):
        if message.text == "/start":
            for i in range(100000000):
                url = (f'https://t.me/+{generate_random_string()}')
                response = requests.get(url,headers=headers)
                soup = BeautifulSoup(response.text, 'lxml')
                data = (soup.find('div',class_='tgme_page_description'))

                if str(data) != '<div class="tgme_page_description">\nYou are invited to a <strong>group chat</strong> on <strong>Telegram</strong>. Click to join:\n</div>':
                    response_true = requests.get(url, headers=headers)
                    soup_name = BeautifulSoup(response_true.text,'lxml')
                    name = (soup_name.find('span')).text
                    expression = (f'{name}  {url}')

                    bot.send_message(message.from_user.id, expression)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)





