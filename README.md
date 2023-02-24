TS Scrapper
---

Зависимости:
---

- selenium==4.8.2
- chromium-browser==111.0.5563.8


Запуск проекта
---
1.  Клонировать проект и перейти в его корень:

		git clone https://github.com/Kolobok99/TrendSalesScript
		cd TrendSalesScript

2. Создать и активировать виртуальное окружение
        
        python3 venv venv        
        source venv/bin/activate

3. Установить зависимости
        
        pip install -r req.txt

4. Установить chromium-browser
        
        sudo add-apt-repository ppa:saiarcot895/chromium-dev
        sudo apt-get update
        sudo apt install chromium-browser

5. Запусить 
        
        python main.py
