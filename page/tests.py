from django.test import TestCase
from .models import Post
from django.urls import reverse
from django.contrib.auth import get_user_model

class PostTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'something',
            email = '',
            password = 'secret',
        )

        self.post = Post.objects.create(
            title = 'title',
            text = 'Something to say',
            author = self.user,
        )

    def test_string_representation(self):
        post = Post(title='chérie coco from Didi b')
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'title')
        self.assertEqual(f'{self.post.text}', 'Something to say')
        self.assertEqual(f'{self.post.author}','something')
    
    def test_post_list_works(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'title')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_post_detail_works(self):
        response = self.client.get('/detail/1/')
        no_response = self.client.get('/detail/-1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'title')
        self.assertTemplateUsed(response, 'post.html')