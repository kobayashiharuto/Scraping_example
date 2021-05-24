import pandas as pd
import requests
from bs4 import BeautifulSoup


def main():
    # httpリクエストでhtmlを取得する
    html = requests.get('http://books.toscrape.com/?')

    # 解析しやすいようBeautifulSoupに変換する
    html_soup = BeautifulSoup(html.content, "html.parser")

    # htmlからデータを取得
    titles = [e['title'] for e in html_soup.select('.row li article h3 a')]
    ratings = [e['class'][1] for e in html_soup.select('.row li .star-rating')]
    prices = [e.text for e in html_soup.select('.row li .price_color')]

    # データを辞書化
    book_datas = {'title': titles, 'rating': ratings, 'price': prices}

    # CSV書き出し用にデータ変換
    df = pd.DataFrame(book_datas)

    # 結果をCSVに書き出す
    df.to_csv('out/result.csv', encoding='utf_8_sig')


if __name__ == '__main__':
    main()
