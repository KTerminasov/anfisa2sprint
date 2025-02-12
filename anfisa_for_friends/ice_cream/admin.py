from django.contrib import admin
from .models import Category, Topping, Wrapper, IceCream

# Вывод вместо пустого значения для всех приложений
admin.site.empty_value_display = 'Не задано'


class IceCreamAdmin(admin.ModelAdmin):
    """Настройки админ-зоны для модели iceCream."""

    # Поля, отображаемые на странице списка объектов
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )

    # Редактируемые поля
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )

    # Поля, по которым будет проводится поиск
    search_fields = (
        'title',
    )

    # Поля, по которым можно фильтровать записи
    list_filter = (
        'category',
    )

    # Поля, при клике на которые можно перейти на страницу просмотра и редактирования записи
    list_display_links = (
        'title',
    )

    # Вывод вместо пустого значения только для приложения IceCream
    # empty_value_display = 'Не задано'

    # Чтобы можно было перекладывать связанные записи из одного окошка в другое
    filter_horizontal = (
        'toppings',
    )


class IceCreamInline(admin.StackedInline):  # Еще можно TabularInline
    """Настроки вставки модели IceCream в другую модель."""

    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    """Настройки админ-зоны для модели Category."""

    # Вставляем на страницу редактирования категории все связанные с ней
    # виды мороженого.
    inlines = (
        IceCreamInline,
    )

    list_display = (
        'title',
    )


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.register(IceCream, IceCreamAdmin)


