from django.shortcuts import render, redirect
from .models import Asset, Purchase
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required
def assets(request):
    user = request.user

    if not user.is_authenticated:
        return render(request, 'assets/assets_manage.html')

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add_asset':
            name = request.POST.get('asset_name')
            if name:
                Asset.objects.create(user=user, name=name)

        elif action == 'add_purchase':
            asset_id = request.POST.get('asset_id')
            quantity = float(request.POST.get('quantity'))
            price = float(request.POST.get('price'))
            asset = Asset.objects.get(id=asset_id, user=user)
            Purchase.objects.create(asset=asset, quantity=quantity, price=price)

        elif action == 'delete_asset':
            asset_id = request.POST.get('asset_id')
            Asset.objects.filter(id=asset_id, user=user).delete()

        return redirect('manage_assets')

    assets = Asset.objects.filter(user=user)
    return render(request, 'assets/assets_manage.html', {'assets': assets})