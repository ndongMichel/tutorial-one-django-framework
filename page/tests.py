from django.test import TestCase
from .models import Post
from django.urls import reverse

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Oubliez Arafat, le nouveau roi est dans la place")
    
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text = 'Chérie coco, c\'est la magie !')
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name, 'Chérie coco, c\'est la magie !')
        