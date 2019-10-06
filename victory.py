while True:
    answer = input('Хотите начать игру? ')
    if answer == 'да':

            count = 0;
            bPushkin = input('Какой год рождения А.С. Пушкина?')
            if bPushkin == '1799':
                count = count+1
            bMayak = input('Какой год рождения В.В. Маяковского?')
            if bMayak == '1893':
                count = count+1
            bTyut = input('Какой год рождения Ф.И. Тютчева?')
            if bTyut == '1803':
                count = count+1
            bBulg = input('Какой год рождения М.А. Булгакова?')
            if bBulg == '1891':
                count = count + 1
            bDost = input('Какой год рождения Ф.М. Достоевского?')
            if bDost == '1821':
                count = count + 1

            print('Количество верных ответов = ', count)
            print('Количество неверных ответов = ', 5 - count)
            print('Процент верных ответов = ', count * (100/5))
            print('Процент неверных ответов = ', (5 - count) * (100/5))

    if answer == 'нет':
        print('Досвиданья')
        break
