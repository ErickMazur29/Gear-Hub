from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from accounts.models import Profile


@receiver (post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''
    esta função gera de forma automática os dados de um perfil criado sem passar pelo profile, 
    seja como superuser ou direto no admin

    created: indica se o objeto foi criado para acionar
    instance: a intancia que sera passada ao profile
    '''
    if created and not hasattr(instance, 'profile'): # se o usuario foi criado e não possui perfil...
        Profile.objects.create(
            user=instance,
            age=30,
            gender="O",
            phone="00000000000",
            local="Avulso"  ,  
        )

    