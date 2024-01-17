from django.db import models


class Users(models.Model):
    fam = models.CharField(max_length=128, verbose_name='Фамилия')
    name = models.CharField(max_length=128, verbose_name='Имя')
    otc = models.CharField(max_length=128, verbose_name='Отчество')
    email = models.EmailField(max_length=128)
    phone = models.IntegerField(verbose_name='Телефон')

    def __str__(self):
        return f'fam: {self.fam}, name: {self.name}, otc: {self.otc}, email: {self.email}, phone: {self.phone}'


class Coords(models.Model):
    latitude = models.FloatField(max_length=20, verbose_name='Широта')
    longitude = models.FloatField(max_length=20, verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f'Широта: {self.latitude}, Долгота: {self.longitude}, Высота: {self.height}.'


class Level(models.Model):
    LEVEL = [
        ('1A', '1A'),
        ('1B', '1B'),
        ('1C', '1C'),
        ('2A', '2A'),
        ('2B', '2B'),
        ('2C', '2C'),
        ('3A', '3A'),
        ('3B', '3B'),
        ('3C', '3C'),
    ]
    summer = models.CharField(max_length=2, choices=LEVEL, verbose_name='Лето')
    autumn = models.CharField(max_length=2, choices=LEVEL, verbose_name='Осень')
    winter = models.CharField(max_length=2, choices=LEVEL, verbose_name='Зима')
    spring = models.CharField(max_length=2, choices=LEVEL, verbose_name='Весна')

    def __str__(self):
        return f'Уровни сложности: Зима: {self.winter}, Лето: {self.summer}, ' \
               f'Осень: {self.autumn}, Весна: {self.spring}.'


class SprActivitiesTypes(models.Model):
    CHOICES_TYPE = [
        ('foot', 'Пешком'),
        ('ski', 'Лыжи'),
        ('catamaran', 'Катамаран'),
        ('kayak', 'Байдарка'),
        ('raft', 'Плот'),
        ('alloy', 'Сплав'),
        ('bicycle', 'Велосипед'),
        ('car', 'Автомобиль'),
        ('sail', 'Парус'),
        ('horseback', 'Верхом'),
    ]

    title = models.CharField(max_length=10, choices=CHOICES_TYPE, verbose_name='Тип похода')


class Perevals(models.Model):
    CHOICES_STATUS = [
        ('new', 'Создано'),
        ('pending', 'Взято в модерацию'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено')
    ]

    beauty_title = models.CharField(max_length=200, verbose_name='Название перевала')
    title = models.CharField(max_length=200, verbose_name='Название перевала')
    other_titles = models.CharField(max_length=200)
    connect = models.CharField(max_length=200)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default='new', verbose_name="Статус заявки")

    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    coord = models.OneToOneField(Coords, on_delete=models.CASCADE)

    def __str__(self):
        return f'Перевал № {self.pk} - {self.beauty_title} находится в статусе "{self.status}".'


class Images(models.Model):
    pereval = models.ForeignKey(Perevals, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=200, verbose_name='Название изображения')
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата добавления')
    image = models.ImageField(upload_to='images', verbose_name='Изображение', blank=True, null=True)
