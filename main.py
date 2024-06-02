from selenium import webdriver
from selenium.webdriver.common.by import By

def get_article_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    return paragraphs

def get_internal_links(browser):
    links = browser.find_elements(By.TAG_NAME, "a")
    return links

def main():
    browser = webdriver.Chrome()

    try:
        query = input("Введите запрос для поиска на Википедии: ")
        search_url = f"https://ru.wikipedia.org/wiki/{query.replace(' ', '_')}"
        browser.get(search_url)

        while True:
            action = input("Выберите действие:\n"
                           "1. Листать параграфы текущей статьи\n"
                           "2. Перейти на одну из связанных страниц\n"
                           "3. Выйти из программы\n"
                           "Введите номер действия: ")

            if action == "1":
                paragraphs = get_article_paragraphs(browser)
                for i, paragraph in enumerate(paragraphs):
                    print(f"{i+1}. {paragraph.text}\n")
                    if i % 5 == 4:
                        more = input("Нажмите Enter для просмотра следующих 5 параграфов или введите 'q' для выхода: ")
                        if more.lower() == 'q':
                            break
                continue

            elif action == "2":
                links = get_internal_links(browser)
                for i, link in enumerate(links):
                    print(f"{i+1}. {link.text} ({link.get_attribute('href')})")
                    if i % 10 == 9:
                        more = input("Enter - следующиt 10 ссылок или 'q' для выбора номера ссылки: ")
                        if more.lower() == 'q':
                            break

                link_number = int(input("Введите номер ссылки, чтобы перейти на связанную страницу: "))
                if 1 <= link_number <= len(links):
                    selected_link = links[link_number - 1].get_attribute("href")
                    browser.get(selected_link)
                    continue
                else:
                    print("Некорректный номер ссылки.")

            elif action == "3":
                print("Выход из программы.")
                break

            else:
                print("Некорректный ввод. Попробуйте еще раз.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        browser.quit()

if __name__ == "__main__":
    main()