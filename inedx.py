import csv
import git

# repo = git.Repo("C:\\Users\\User\\Desktop\\T15")
repo = git.Repo("C:\\Users\\User\\Desktop\\T15")
commits = list(repo.iter_commits("main"))


def output_to_csv_file():
    with open("git_command_1.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(["Дата", "Hash", "Автор", "Сообщение"])
        for i in range(len(commits)):
            file_writer.writerow([commits[i].committed_datetime, commits[i].hexsha, commits[i].author, commits[i].message])


def output_to_console():
    for i in range(len(commits)):
        print(commits[i].committed_datetime)
        print(commits[i].hexsha)
        print(commits[i].author)
        print(commits[i].message)
        print()


input_1 = input('Введите цыфру 1 и все коммиты покажутся в консоли или цыфру 2 и все коммиты загрузяться в виде csv таблицы: ')

if input_1 == '1':
    output_to_console()

elif input_1 == '2':
    output_to_csv_file()

else:
    print('Произошла ошибка в программе перезапустите её!!!')
