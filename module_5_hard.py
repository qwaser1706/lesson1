import hashlib
import time



class User:
    """
    класс пользователя, содержащий атрибуты: логин, hash.пароль, возраст.
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()# хешируем пароль

    def __eq__(self, other):
        return  self.nickname == other.nickname # проверка пользователя по нику


    def __str__(self):
        return f"{self.nickname}"# строковое представлениеИмениПользователя

class Video:
    """
    класс видеороликов
    """
    def __init__(self, title, duration, adult_mode = False):
        self.title = title #заголовок
        self.duration = duration #продолжительность
        self.adult_mode = adult_mode #возрастной режим
        self.time_now = 0 #текущее время просмотра

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()# проверка видео по заголовку

    def __str__(self):
        return f"video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"#строк.данныеОвидео

class UrTube:
    """
    класс создаёт платформу и предоставляет методы взамодействия с ним.
    """
    def __init__(self):
        self.users = [] #список пользователей
        self.videos  = [] #список роликов
        self.current_user = None #актуальный пользователь

    def lof_in(self, nickname, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()# проверка наличия в базе зарег.пользователя
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password: # если такой юзер есть,то курент.юзер меняется с нон на него
                print(f'Пользователь {nickname} вошёл в систему.')
                return  True
        print("Ошибка входа: неверный логин или пароль.")
        return False

    def register(self, nickname, password, age):# регаем нового и сразу логинимся
        new_user = User(nickname, password, age)
        if new_user in self.users:#если вводимый уже есть
            print(f'Пользователь {nickname} уже существует.')
        else:# после реги , вход автоматом.
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):#выход, сброс текущего на ноне
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
            self.current_user = None
        else:
            print("В системе нет активных пользователей")


    def add(self, *videos):# добавляет новое, если его ещё нет.
        for video in videos:
            if video not in  self.videos:#если нету
                self.videos.append(video)#добавляем


    def get_videos(self, search_term):# возращает список названий содержащих поисковое слово
        search_term_lower = search_term.lower()
        return [video.title for video in self.videos if search_term_lower in video.title.lower()]

    def watch_video(self, title):# смотрим видео если выполнен вход и есть доступ
        if not self.current_user:
            print("ввойдите в акккаунт, чтобы смотреть видео.")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("вам нет 18 лет, покиньте страницу.")
                    return

                for second in range(video.time_now + 1,video.duration + 1):
                    print(second, end = " ", flush = True)# смотрим видео
                    time.sleep(1)#по секунде
                print("конец видео")
                video.time_now = 0# сбрасываем таймер просмотра
                return




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
