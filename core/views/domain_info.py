from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test, login_required
# from django.contrib.admin.views.decorators import staff_member_required


@login_required
@user_passes_test(lambda u: u.is_superuser)
def domain_info(request):
    dm_info = []

    dm_info.append(("DOMAIN", settings.DOMAIN))
    dm_info.append(("PROD_DEPLOY", settings.PROD_DEPLOY))
    dm_info.append(("DEBUG", settings.DEBUG))
    dm_info.append(("ADMINS", settings.ADMINS))
    dm_info.append(("DB_HOST", settings.DB_HOST))
    dm_info.append(("DB_NAME", settings.DB_NAME))
    dm_info.append(("MEDIA_URL", settings.MEDIA_URL))
    dm_info.append(("MEDIA_ROOT", settings.MEDIA_ROOT))

    context = {
        "dm_info": dm_info
    }

    return render(request, 'core/domain_info/domain_info.html', context)
