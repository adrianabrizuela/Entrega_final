from django.test import TestCase

# Create your tests here.

from Post.models import Post
from django.utils import timezone
from django.contrib.auth.models import User
from Post.models import Post



class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create(
            destino='Destino de prueba',
            ciudad='Ciudad de prueba',
            comentarios='Esto es una prueba',
            fecha=timezone.now(),
            autor=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.destino, 'Destino de prueba')
        self.assertEqual(self.post.ciudad, 'Ciudad de prueba')
        self.assertEqual(self.post.comentarios, 'Esto es una prueba')
        self.assertEqual(self.post.autor, self.user)


