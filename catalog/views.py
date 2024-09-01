from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version


class ProductList(ListView):
    model = Product
    extra_context = {
        'title': 'Главная страница'
    }

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = self.get_queryset(*args, **kwargs)

        for product in products:
            # Фильтруем версии по текущему продукту и только текущие версии
            active_versions = Version.objects.filter(product=product, is_current=True)

            if active_versions.exists():
                # Берем последнюю из текущих версий
                product.active_version = active_versions.last()
            else:
                # Устанавливаем сообщение, если активных версий нет
                product.active_version = 'Нет активной версии'

        # Обновляем список объектов в контексте (потом добавляем в шаблоне if active_versions != 'Нет активной версии'
        context_data['object_list'] = products
        return context_data


class ProductCreate(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()  # сохраняем продукт
        # чтобы владелец был только авторизованный пользователь, добавляем LoginRequiredMixin.
        # авторизованного пользователя можно получить из запроса
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)

    # альтернативное решение по привязке owner к продукту
    # def form_valid(self, form):
    #     form.instance.owner = self.request.user
    #     return super().form_valid(form)


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(
            Product,  # модель, которую будем использовать для создания формы
            Version,  # модель, которую будем использовать для создания каждой версии
            VersionForm,  # форма для каждой версии
            extra=1  # сколько версий будем создавать
        )

        # из self мы можем получить request и из него узнать действие, которое будет происходить POST GET
        if self.request.method == 'POST':
            # мы обращаемся к нашей переменной context_data и добавляем к ней нашу форму
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            # сохраняем форму и форму-список версий
            self.object = form.save()  # сохраняем форму-объект в модель Product
            formset.instance = self.object  # устанавливаем форму
            formset.save()  # сохраняем форму-список версий
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("product.can_change_is_published") and user.has_perm(
                "can_change_description") and user.has_perm("can_change_category"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


def home(request):
    return render(request, 'home.html')


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} ({phone}): {message}')
#     return render(request, 'contacts.html')


class ContactsView(TemplateView):
    template_name = 'contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({email}): {message}')
        context_data['object_list'] = Product.objects.all()[:5]
        return context_data
